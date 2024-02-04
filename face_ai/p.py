# import os
# current_dir = os.getcwd()
# print(f"{current_dir}/r_img")

import requests

url = 'http://127.0.0.1:8000/accounts/hello/'
headers = {'Authorization': 'Token 1f6a359d88219785a8e481490e5efb78dd6ffde7'}
r = requests.get(url, headers=headers)
print(r.json())