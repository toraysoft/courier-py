courier-py
==========

Courier (A SMS Broker) Client for Python


安装
--------

    pip install courier-py

使用
-------

首先，需要获取一个应用代码(app)及密钥(key)

初始化客户端：

    >>> from courier import CourierClient
    >>> cli = CourierClient(app, key)

获取验证码，同时会向目标手机发送短信：

    >>> code = cli.get_code('13800138000')
    >>> code
    '832233'

校验验证码：

    >>> cli.verify_code('13800138000', '832233')
    True

