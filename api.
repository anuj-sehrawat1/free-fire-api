import requests

url = "https://client.ind.freefiremobile.com/GetPlayerPersonalShow"

jwt = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjMiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjo5MTcxNjE0MjM2LCJuaWNrbmFtZSI6IlRH4piE77iPQW5raXQiLCJub3RpX3JlZ2lvbiI6IklORCIsImxvY2tfcmVnaW9uIjoiSU5EIiwiZXh0ZXJuYWxfaWQiOiI3ZDBiMjgyYTk3M2Y1MzgwM2U0YTJjNzQ5ODczMDFiNSIsImV4dGVybmFsX3R5cGUiOjQsInBsYXRfaWQiOjAsImNsaWVudF92ZXJzaW9uIjoiIiwiZW11bGF0b3Jfc2NvcmUiOjEwMCwiaXNfZW11bGF0b3IiOnRydWUsImNvdW50cnlfY29kZSI6IkdCIiwiZXh0ZXJuYWxfdWlkIjozMTk3MDU5NTYwLCJyZWdfYXZhdGFyIjoxMDIwMDAwMDUsInNvdXJjZSI6MCwibG9ja19yZWdpb25fdGltZSI6MTcxMjk4OTk2NCwiY2xpZW50X3R5cGUiOjEsInNpZ25hdHVyZV9tZDUiOiIiLCJ1c2luZ192ZXJzaW9uIjowLCJyZWxlYXNlX2NoYW5uZWwiOiIiLCJyZWxlYXNlX3ZlcnNpb24iOiJPQjUxIiwiZXhwIjoxNzY4Mjc5MDA2fQ.vvcbiEXbMMIFWGDD3QSdU_aaYABsinhyNGIxlmtUGzs"
aes_hex = "e070fac316fb2cec94201cc6c13acc64"

headers = {
    "Authorization": f"Bearer {jwt}",
    "Content-Type": "application/x-www-form-urlencoded",
    "ReleaseVersion": "OB48",
    "X-Unity-Version": "2018.4.11f1",
    "User-Agent": "Dalvik/2.1.0"
}

data = bytes.fromhex(aes_hex)

r = requests.post(url, headers=headers, data=data, timeout=10)

print(r.status_code)
print(r.content.hex())
