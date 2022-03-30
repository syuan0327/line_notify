import requests
import climb
import time
import os
token = ''
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code

def lineNotify(token, msg, stickerPackageId, stickerId):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
   
    payload = {"message": msg, "stickerPackageId": stickerPackageId, 'stickerId': stickerId}
    r = requests.post(url, headers = headers, params = payload)
    return r.status_code
 
if __name__=="__main__":
    
# 你要傳送的訊息內容
    message = climb.c_compare()+'現價'+climb.cdibh()
    message2 = climb.f_compare()+'現價'+climb.foxconn()
# 將剛剛複製下來的Token取代以下''中的內容即可 
    lineNotifyMessage(token, message)
    lineNotifyMessage(token, message2)
    '''
    msg = "Hello Python"
    stickerPackageId = 2
    stickerId = 38
 
    lineNotify(token, msg, stickerPackageId, stickerId)'''
    time.sleep(60)



