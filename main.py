from tornado.web import Application
from tornado.ioloop import IOLoop
import settings


def main():
    app = Application(settings.ROUTES, debug=settings.DEBUG)
    app.listen(settings.PORT)
    IOLoop.current().start()


if __name__ == "__main__":
    print "Start serve at 127.0.0.1:{}~".format(settings.PORT)
    main()
