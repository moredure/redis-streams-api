class Config:
    def __init__(self, env: dict):
        self.redis_host = env.get('REDIS_HOST', 'localhost')
        self.redis_port = int(env.get('REDIS_PORT', 6379))
        self.port = int(env.get('PORT', '3000'))

    @property
    def address(self) -> tuple:
        return '', self.port
