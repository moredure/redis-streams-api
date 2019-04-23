from http.server import ThreadingHTTPServer

from redis import Redis


class Suicide:
    def __init__(self, server: ThreadingHTTPServer, conn: Redis):
        self.server = server
        self.conn = conn

    def die(self, signum: int, frame):
        self.server.shutdown()
        self.conn.connection_pool.disconnect()
