__version_info__ = ('0', '2', '1')
__version__ = '.'.join(__version_info__)

def django_app():
    import django
    import django.core.handlers.wsgi
    import tornado.wsgi

    django.setup()
    app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
    app = ('.*', tornado.web.FallbackHandler, dict(fallback=app))

    return app
