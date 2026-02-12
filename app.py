from flask import Flask, jsonify, request
import requests
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from protobuf_decoder.protobuf_decoder import Parser
from datetime import datetime
import json

app = Flask(__name__)

# ================= FF INFO ACCOUNT =================
DEFAULT_UID = "4507805470"
DEFAULT_PASS = "BB1C81A6C71CD62F4EEB62E8958B7BFA239D2876FEE03D7A050AF0A2DE8FFFED"


# ================= JWT LOGIN =================
def get_jwt():
    try:
        url = f"https://freefireserver.c0m.in/oauth/account:login?data={DEFAULT_UID}:{DEFAULT_PASS}"
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return None
        return res.json().get("8")  # JWT
    except:
        return None


# ================= DONT EDIT =================
def Encrypt_ID(x):
    x = int(x)
    dec = ['80','81','82','83','84','85','86','87','88','89','8a','8b','8c','8d','8e','8f',
           '90','91','92','93','94','95','96','97','98','99','9a','9b','9c','9d','9e','9f',
           'a0','a1','a2','a3','a4','a5','a6','a7','a8','a9','aa','ab','ac','ad','ae','af',
           'b0','b1','b2','b3','b4','b5','b6','b7','b8','b9','ba','bb','bc','bd','be','bf',
           'c0','c1','c2','c3','c4','c5','c6','c7','c8','c9','ca','cb','cc','cd','ce','cf',
           'd0','d1','d2','d3','d4','d5','d6','d7','d8','d9','da','db','dc','dd','de','df',
           'e0','e1','e2','e3','e4','e5','e6','e7','e8','e9','ea','eb','ec','ed','ee','ef',
           'f0','f1','f2','f3','f4','f5','f6','f7','f8','f9','fa','fb','fc','fd','fe','ff']
    xxx = ['1','01','02','03','04','05','06','07','08','09','0a','0b','0c','0d','0e','0f',
           '10','11','12','13','14','15','16','17','18','19','1a','1b','1c','1d','1e','1f',
           '20','21','22','23','24','25','26','27','28','29','2a','2b','2c','2d','2e','2f',
           '30','31','32','33','34','35','36','37','38','39','3a','3b','3c','3d','3e','3f',
           '40','41','42','43','44','45','46','47','48','49','4a','4b','4c','4d','4e','4f',
           '50','51','52','53','54','55','56','57','58','59','5a','5b','5c','5d','5e','5f',
           '60','61','62','63','64','65','66','67','68','69','6a','6b','6c','6d','6e','6f',
           '70','71','72','73','74','75','76','77','78','79','7a','7b','7c','7d','7e','7f']

    x = x / 128
    if x > 128:
        x = x / 128
        if x > 128:
            x = x / 128
            if x > 128:
                x = x / 128
                y = (x - int(x)) * 128
                z = (y - int(y)) * 128
                n = (z - int(z)) * 128
                m = (n - int(n)) * 128
                return dec[int(m)] + dec[int(n)] + dec[int(z)] + dec[int(y)] + xxx[int(x)]
            else:
                y = (x - int(x)) * 128
                z = (y - int(y)) * 128
                n = (z - int(z)) * 128
                return dec[int(n)] + dec[int(z)] + dec[int(y)] + xxx[int(x)]


# ================= AES ENCRYPT =================
def encrypt_api(plain_hex):
    key = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
    iv  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(bytes.fromhex(plain_hex), 16)).hex()


# ================= PROTO PARSER =================
def parse_results(results):
    out = {}
    for r in results:
        if r.wire_type == "length_delimited":
            out[r.field] = {"data": parse_results(r.data.results)}
        else:
            out[r.field] = {"data": r.data}
    return out


def decode_proto(hex_data):
    parsed = Parser().parse(hex_data)
    return json.dumps(parse_results(parsed))


# ================= ENCRYPT ONLY API =================
@app.route("/encrypt", methods=["GET"])
def encrypt_only():
    uid = request.args.get("uid")
    if not uid or not uid.isdigit():
        return jsonify({"status": "error", "message": "valid uid required"}), 400

    enc_id = Encrypt_ID(uid)
    proto = f"08{enc_id}1007"
    aes = encrypt_api(proto)

    return jsonify({
        "status": "success",
        "uid": uid,
        "encrypted_id": enc_id,
        "protobuf_hex": proto,
        "aes_encrypted_payload_hex": aes
    })


# ================= PLAYER INFO API =================
@app.route("/player-info", methods=["GET"])
def player_info():
    pid = request.args.get("id")
    if not pid:
        return jsonify({"status": "error", "message": "id required"}), 400

    jwt = get_jwt()
    if not jwt:
        return jsonify({"status": "error", "message": "jwt failed"}), 500

    payload = bytes.fromhex(encrypt_api(f"08{Encrypt_ID(pid)}1007"))

    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Dalvik/2.1.0",
        "ReleaseVersion": "OB48"
    }

    r = requests.post(
        "https://client.ind.freefiremobile.com/GetPlayerPersonalShow",
        headers=headers,
        data=payload,
        verify=False
    )

    if r.status_code != 200:
        return jsonify({"status": "error", "code": r.status_code})

    data = json.loads(decode_proto(binascii.hexlify(r.content).decode()))

    return jsonify({
        "status": "success",
        "name": data["1"]["data"]["3"]["data"],
        "level": data["1"]["data"]["6"]["data"],
        "likes": data["1"]["data"]["21"]["data"],
        "server": data["1"]["data"]["5"]["data"]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
