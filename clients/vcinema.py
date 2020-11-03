import time

from clients.base import BaseClient


class VcInEma(BaseClient):

    def __init__(self):
        super(VcInEma, self).__init__()
        self.base_url = 'https://o-api.vcinema.cn/v5.0/user/{}/send_code'

    def run(self, **kwargs):
        phone = kwargs.get('phone')
        current_time = time.time()
        current_time = int(round(current_time * 1000))
        code_data = {"is_wap": 1, "_": current_time}
        response = self.fetch(self.base_url.format(phone), params=code_data)
        self.logger.info(response.text)
