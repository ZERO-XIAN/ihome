from flask import current_app
from . import api
from ihome import db, models
import logging


@api.route("/index")
def index():
    # logging.error("")   # 错误级别
    # logging.warn("")    # 警告级别
    # logging.info("")    # 消息提示级别
    # logging.debug("")   # 调试级别
    current_app.logger.error("error msg")
    current_app.logger.error("warn msg")
    current_app.logger.error("info msg")
    current_app.logger.error("debug msg")
    return "index page"