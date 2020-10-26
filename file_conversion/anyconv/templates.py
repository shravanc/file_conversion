upload_api = """
curl 'https://anyconv.com/api/action/add/%s/' \
  -H 'access-control-allow-origin: *' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'content-type: multipart/form-data' \
  -H 'cookie: _ga=GA1.2.1234396918.1602581718; _ym_uid=1596117912523737438; _ym_d=1602581723; XSRF-TOKEN=eyJpdiI6IlNxbDdXXC9BalhFVjdvYWNFQjZnZld3PT0iLCJ2YWx1ZSI6ImdyZkpPOXd6U0s0ZExmN09aWFFUNit4c1lhNmp    3QndsYzNJRkNoaWZxeXpMM3h5b0hXZXJnRnhtT2VkdE9neTAiLCJtYWMiOiI5ZTM1ZGUwMzAyNzMzMDNiYjNhMDkxMjVmMWNjNjMxMmJhOTEyZjVlMzg4MDFmMDRlY2E4NmFhNGU4N2Q1N2I5In0=; _gid=GA1.2.252471988.1603569339; _ym_wasSynced={"    time":1603569345626,"params":{"eu":1},"bkParams":{}}; _ym_isad=1; _ym_visorc_53329336=w; anyconvsession=eyJpdiI6IkhzTkt6U0RkVkZxV2FIM08wODhLakE9PSIsInZhbHVlIjoiOCtWMjlNUjhFM0V0MmJPZW5EckM2bkJvdEE2Z3I4    dlwvOWhUQTB3M3RyTFNhcURvY1wvSmpOaXNHSmlPMkxJcnZvIiwibWFjIjoiNWE2NTEzNTY1MTNlMTJkZWVjZGYyODE3YjRhNTU0MmRiODYyNzIxZDYzMGQxNTk5ZTc3MjZmYzA3MDhhNTJhNyJ9' \
  -F to=%s \
  -F file=@%s \
  --compressed \
"""




download_api = """
curl 'https://anyconv.com/api/action/download/%s/' \
  -H 'access-control-allow-origin: *' \
  -H 'cookie: _ga=GA1.2.1234396918.1602581718; _ym_uid=1596117912523737438; _ym_d=1602581723; XSRF-TOKEN=eyJpdiI6IlNxbDdXXC9BalhFVjdvYWNFQjZnZld3PT0iLCJ2YWx1ZSI6ImdyZkpPOXd6U0s0ZExmN09aWFFUNit4c1lhNmp    3QndsYzNJRkNoaWZxeXpMM3h5b0hXZXJnRnhtT2VkdE9neTAiLCJtYWMiOiI5ZTM1ZGUwMzAyNzMzMDNiYjNhMDkxMjVmMWNjNjMxMmJhOTEyZjVlMzg4MDFmMDRlY2E4NmFhNGU4N2Q1N2I5In0=; _gid=GA1.2.252471988.1603569339; _ym_wasSynced={"    time":1603569345626,"params":{"eu":1},"bkParams":{}}; _ym_isad=1; _ym_visorc_53329336=w; anyconvsession=eyJpdiI6IkhzTkt6U0RkVkZxV2FIM08wODhLakE9PSIsInZhbHVlIjoiOCtWMjlNUjhFM0V0MmJPZW5EckM2bkJvdEE2Z3I4    dlwvOWhUQTB3M3RyTFNhcURvY1wvSmpOaXNHSmlPMkxJcnZvIiwibWFjIjoiNWE2NTEzNTY1MTNlMTJkZWVjZGYyODE3YjRhNTU0MmRiODYyNzIxZDYzMGQxNTk5ZTc3MjZmYzA3MDhhNTJhNyJ9' \
  > %s \
"""

