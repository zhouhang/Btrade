# -*- coding: utf-8 -*-

import tornado.web
import session
from database import database
import json
from  datetime import date,datetime
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class WebBaseHandler(tornado.web.RequestHandler):
  
  def initialize(self):
      self.session = session.Session(self.application.session_manager, self)
      self.db = database.instance().get_session()

  def get(self):
      """捕获404"""
      self.send_error(404)

  def write_error(self, status_code, **kwargs):
      """重写404错误页
      """
      if status_code == 404:
          self.render('public/404.html')
      elif status_code == 500:
          self.render('public/500.html')
      else:
          self.write('error:' + str(status_code))

  def get_current_user(self):
       return None

  def success(self, message='操作成功', url=''):
        """操作成功提示
        """
        self.render('message/success.html', message=message, url=url)

  def failure(self, message="操作失败", url=''):
        self.render('message/failure.html', message=message, url=url)



  def api_response(self, data):
        """将数据转成json返回给客户端"""
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        data = json.dumps(data,cls=CJsonEncoder)
        self.finish(data)

  def on_finish(self):
      self.db.close()


