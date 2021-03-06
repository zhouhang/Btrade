# -*- coding: utf-8 -*-
import os.path
from handler.main import *
from handler.login import *
from handler.purchase import *
from handler.monitor import *
from handler.supplier import *
from handler.pushrecord import *
from handler.transaction import *
from handler.identity import *
from globalconfig import *



settings = {
    "app": app,
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "xsrf_cookies": True,
    "login_url": "/login",
    "cookie_secret": "e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
    "session_secret": "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
    "session_timeout": 60*60,
    "store_options": {
        'redis_host': 'localhost',
        'redis_port': 6379,
        'redis_pass': '',
    },
}

handlers = [
    (r"/", MainHandler),
    (r"/users/userlist", UserListHandler),
    (r"/admin/reset",AdminResetHandler),
    #(r"/users/userlist/page/([0-9]+)", UserListHandler),
    (r"/user/identify",IdentifyUserHandler),
    (r"/quality/upload",QualityUploadHandler),
    (r"/record/update",UpdateRecordHandler),
    (r"/user/upgrade", UpgradeUserHandler),
    (r"/member/updatestatus", UpdateMemberHandler),
    (r"/users/adminlist", AdminListHandler),
    (r"/admin/userinfo",AdminUserHandler),
    (r"/admin/update", UpdateAdminStatusHandler),
    (r"/users/userinfo", UserInfoHandler),
    (r"/users/userinfo/([0-9]+)", UserInfoHandler),
    (r"/users/recover/([0-9]+)", UserRecoverHandler),
    (r"/users/remove/([0-9]+)", UserRemoveHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    #(r"/purchase/purchaselist/type/(-?[0-9]+)/starttime/(.*)/endtime/(.*)/page/([0-9]+)", PurchaseHandler),
    #(r"/purchase/purchaselist/type/(-?[0-9]+)/starttime/(.*)/endtime/(.*)", PurchaseHandler),
    (r"/purchase/purchaselist", PurchaseHandler),
    (r"/purchase/transactionlist", TransactionHandler),
    (r"/purchase/transaction", TransactionDetailHandler),
    (r"/purchase/transactionedit", TransactionEditHandler),
    (r"/purchase/transactionsuccess", TransactionSuccessHandler),
    (r"/uploadimage", UploadImageHandler),
    (r"/cropimage", CropImageHandler),
    (r"/delfile", DelFileHandler),
    (r"/purchase/transactiondelete", TransactionDeleteHandler),
    (r"/purchase/purchaseinfo/([0-9]+)", PurchaseInfoHandler),
    (r"/updatequotestate", UpdateQuoteStateHandler),
    (r"/removepurchase", RemovePurchaseHandler),
    (r"/pushpurchase", PushPurchaseHandler),
    (r"/stat/statistics", MonitorStatisticsHandler),
    (r"/stat/business", MonitorBusinessHandler),
    (r"/stat/pushrecord", PushRecordHandler),
    (r"/stat/pushrecord/detail", RecordDetailHandler),
    (r"/supplier/supplierdetail", SupplierDetailHandler),
    (r"/supplier/supplierlist", SupplierHandler),
    (r"/supplier/supplieradd", SupplierInsertHandler),
    (r"/supplier/supplieredit", SupplierEditHandler),
    (r"/supplier/getByMobile", SupplierMobileHandler),
    (r"/supplier/search", SupplierSearchHandler),
    (r"/supplier/area", SupplierAreaHandler),
    (r"/supplier/variety", SupplierVarietyHandler),
    (r"/supplier/result", SupplierResultHandler),
    (r"/users/payment", UserPaymentHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static"}),
];

#参数配置项
#如果设置为0则不现实，此处的更改为全局设置，但仍然可以单独设置某处的显示选项
conf = {
    #主页显示的文章数目
    'POST_NUM': 10,
}

"""日志设置
开启多个实例时请使用 -log_file_prefix='log@8000.txt' 命令参数，
每个端口需要单独定义。
此时该设置将无任何作用
"""
#开启日志文件记录，默认为 False
log = True
#日志记录位置
log_file = 'Btrade-boss/log/tornado.log'

imgmap1={
    1:u"本人头像",
    2: u"身份证正面",
    3:u"种植基地照片"
}
imgmap2={
    1: u"企业全景",
    2: u"联系人身份证正面",
    3: u"法人身份证正面",
    4: u"营业执照",
    5: u"GSP证书",
    6: u"中草药收购证",
    7: u"授权书2.0"
}
