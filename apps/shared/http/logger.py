"""Logger. """

import json
import logging
from typing import Union


class Logger:

    def __init__(self):
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.Logger('http_logger')
        logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter(
            '{"level": "%(levelname)s", "time": "%(asctime)s", %(message)s}'
        )
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)
        return logger

    def info(self, app: str, type: str, detail: str, method: str = None,
             uri: str = None, payload: Union[dict, list] = None, status: int = None,
             code: str = None):
        msg = self.__message(app, type, detail, method, uri, payload, status, code)
        self.logger.info(msg)

    def debug(self, message: str, extra: dict = None):
        self.logger.debug(message, extra=extra)

    def warning(self, message: str, extra: dict = None):
        self.logger.warning(message, extra=extra)

    def error(self, app: str, type: str, detail: str, method: str = None,
              uri: str = None, payload: Union[dict, list] = None, status: int = None,
              code: str = None):
        msg = self.__message(app, type, detail, method, uri, payload, status, code)
        self.logger.error(msg)

    def critical(self, message: str, extra: dict = None):
        self.logger.critical(message, extra=extra)

    def __message(self, app: str, type: str, detail: str, method: str = None,
                  uri: str = None, payload: Union[dict, list] = None, status: int = None,
                  code: str = None):
        if payload:
            payload = payload.copy()
        if isinstance(payload, dict):
            if payload.get('access_token'):
                payload['access_token'] = payload['access_token'][0:20] + '...'
            if payload.get('password'):
                characters = len(payload.get('password'))
                payload['password'] = '*' * characters
        app = app.replace('gateway.', '')
        msg = dict(app=app, type=type)
        if status or type == 'app.response': msg['status'] = status if status else 200
        if code or type == 'app.response': msg['code'] = code if code else 0
        if detail: msg['detail'] = detail
        if method: msg['method'] = method
        if uri: msg['uri'] = uri
        if payload: msg['payload'] = payload
        return json.dumps(msg, ensure_ascii=False)[1:-1]