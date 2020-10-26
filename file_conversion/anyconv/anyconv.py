import string
import random
from anyconv.templates import upload_api, download_api
import os
import time

class Anyconv:

    def __init__(self, info): #source_file="", target_file="", to="obj"):
        self.source_file = info['source_file']
        self.target_file = info['target_file']
        self.to = info['to']
        self.uniq_id = self._get_random_number(32)


    def convert(self):
        print("**11**")
        self._upload()
        print("**12**")
        time.sleep(1)
        print("**13**")
        self._check_status()
        print("**14**")
        self._download()
        print("**15**")

    def _get_random_number(self, id_len):
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(id_len)])

    def _upload(self):
        template =upload_api
        template = template % (self.uniq_id, self.to, self.source_file)
        print(template)
        resp = self._post(template)
        print(resp)

    def _check_status(self):
        status_api = f"curl -XGET https://anyconv.com/api/action/status/{self.uniq_id}/"
        resp = os.system(status_api)
        print(resp)


    def _download(self):
        template = download_api
        template = template %(self.uniq_id, self.target_file)
        resp = self._post(template)
        print(resp)

    def _post(self, template):
        return os.system(template)


#source_file = "~/Downloads/Vine.glb"
#source_file = "/home/shravan/Downloads/Vine.glb"
#target_file_name = "/home/shravan/noplacelike/data_conversion/shortcut/output.obj"
#to = "obj"
#ac = Anyconv(source_file, target_file, to)
#ac.convert()
