class Config:
    def __init__(self, env: dict):
        self.redis_host = env.get('REDIS_HOST', 'servers.microredis.com')
        self.redis_port = int(env.get('REDIS_PORT', 30014))
        self.redis_password = env.get('REDIS_PASSWORD', '3ab28036-34f3-4d18-9a0b-561e67c8d747')
        self.port = int(env.get('PORT', '3000'))

    @property
    def address(self) -> tuple:
        return '', self.port
