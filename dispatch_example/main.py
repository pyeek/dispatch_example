# main.py
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from root import app as root
from app1 import app as app1
from app2 import app as app2

if __name__ == '__main__':
    app = DispatcherMiddleware(root, {
        '/app1': app1,
        '/app2': app2
    })

    run_simple('0.0.0.0', 8080, app, use_reloader=True, use_debugger=True)
