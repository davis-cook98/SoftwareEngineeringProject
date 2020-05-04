from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from Read.endpoints import read as ReadAPI
from Write.endpoints import write as WriteAPI

application = DispatcherMiddleware(ReadAPI, {
    '/WriteAPI': WriteAPI
})

if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=5000,
        application=application,
        use_reloader=True,
        use_debugger=True,
        use_evalex=True)