import connexion
from waitress import serve
# import logging.config
# logging.config.fileConfig('./log.conf', disable_existing_loggers=False)
# logger = logging.getLogger(__name__)

# logger.info('Server is up')

app = connexion.App(__name__, specification_dir='./')
app.add_api('../interface/swagger_admin.yml')
# app.add_api('./rest_predictor/swagger_client.yml'.)

if __name__ == '__main__':

    # serve(app, host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000, debug=False)


# import multiprocessing
# import gunicorn.app.base
#
#
# def number_of_workers():
#     return (multiprocessing.cpu_count() * 2) + 1
#
#
# def handler_app(environ, start_response):
#     response_body = b'Works fine'
#     status = '200 OK'
#
#     response_headers = [
#         ('Content-Type', 'text/plain'),
#     ]
#
#     start_response(status, response_headers)
#
#     return [response_body]
#
#
# class StandaloneApplication(gunicorn.app.base.BaseApplication):
#
#     def __init__(self, app, options=None):
#         self.options = options or {}
#         self.application = app
#         super().__init__()
#
#     def load_config(self):
#         config = {key: value for key, value in self.options.items()
#                   if key in self.cfg.settings and value is not None}
#         for key, value in config.items():
#             self.cfg.set(key.lower(), value)
#
#     def load(self):
#         return self.application
#
#
# if __name__ == '__main__':
#     options = {
#         'bind': '%s:%s' % ('127.0.0.1', '8080'),
#         'workers': number_of_workers(),
#     }
#     StandaloneApplication(handler_app, options).run()