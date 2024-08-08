import requests
import json
import time

MEROSS_IPADDR = "192.168.1.18" 

MESSAGE_ID = "b67865307e2f257ea7212a4705c66d7e"
UUID = "2012178798587751804448e1e942417d"
SIGH = "f09dbd80bc330a5aae20f82aa60ef245"
TIME_STAMP = 1677131441

def ac_onoff(on_off):
    url = f"http://{MEROSS_IPADDR}/config"
    head = {"Content-Type": "application/json"}
    #35行目にてdataをdumpsしてpostしてあげる
    data = {
        "payload": {
            "togglex": {
                "onoff": on_off,
                "channel": 0
            }
        },
        "header": {
            "messageId": MESSAGE_ID, 
            "method": "SET",
            "from": f"http:\/\/{MEROSS_IPADDR}\/config",
            "payloadVersion": 1,
            "namespace": "Appliance.Control.ToggleX",
            "uuid": UUID, 
            "sign": SIGH, 
            "triggerSrc": "iOSLocal",
            "timestamp": TIME_STAMP 
        }
    }
    payload = {'some': 'data'}
    r = requests.post(url, headers=head, data=json.dumps(data), json=payload)

    TorF = r.status_code == requests.codes.ok
    #reqがTrueならrをpost
    try:
        if TorF == True:
            print(r, "...True")
    except requests.exceptions.RequestException as e:
        if TorF == False:
            print(e, "False")
        return


if __name__ == '__main__':
    for n in range(4):
        ac_onoff(0)
        time.sleep(0.4)
        ac_onoff(1)
        time.sleep(0.4)
