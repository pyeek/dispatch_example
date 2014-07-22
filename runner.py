"""
    runner.py

    This is the entry point to the example

    Uses werkzeug.wsgi.DispatcherMiddleware to combine the apps, mounting as
    follows:

        http://localhost/: root
        http://localhost/app1: app1
        http://localhost/app2: app2

    Then uses run_simple to serve it on localhost
"""
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from dispatch_example.root import app as root
from dispatch_example.app1 import app as app1
from dispatch_example.app2 import app as app2

if __name__ == '__main__':
    # DispatcherMiddleware requires a "root" application (named root in this case)
    app = DispatcherMiddleware(root, {
        '/app1': app1,
        '/app2': app2
    })

    run_simple('0.0.0.0', 8080, app, use_reloader=True, use_debugger=True)
