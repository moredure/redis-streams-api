import redis
from functools import partial
from http.server import ThreadingHTTPServer
from os import environ
from signal import signal, SIGTERM, SIGINT
from threading import Thread
from src.components.config import Config
from src.components.suicide import Suicide
from src.components.listener import Listener
from src.components.ad_events_controller import AdEventsController

if __name__ == '__main__':
    config = Config(environ)
    conn = redis.Redis(host=config.redis_host,
                       password=config.redis_password,
                       port=config.redis_port,
                       ssl=True,
                       ssl_ca_certs=config.redis_ssl_ca_certs,
                       ssl_certfile=config.redis_ssl_certfile,
                       ssl_keyfile=config.redis_ssl_keyfile)
    controller = AdEventsController(conn)
    ListenerWithController = partial(Listener, controller)
    server = ThreadingHTTPServer(config.address, ListenerWithController)
    server_thread = Thread(target=server.serve_forever)
    server_thread.start()
    suicide = Suicide(server)
    signal(SIGTERM, suicide.die)
    signal(SIGINT, suicide.die)
    server_thread.join()
