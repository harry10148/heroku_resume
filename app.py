import json
import os 

#請改成自己律定API Server的container name
ip_location='chatbot_api'

# 載入基礎設定檔，本機執行所以路徑可以相對位置
secretFile=json.load(open("./secret_key",'r'))

# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別
from linebot import (
    LineBotApi, WebhookHandler
)

# channel_access_token是用於傳送封包去給line的認證使用類似這個是私鑰，而公鑰已經丟到line那邊，拿著這個就可以有VIP特權
line_bot_api = LineBotApi(secretFile.get("channel_access_token"))

# secret_key是用於當line傳送封包過來時確定line是否為本尊，沒有被仿冒
handler = WebhookHandler(secretFile.get("secret_key"))

# rich_menu_id用於將所指定的rich menu綁定到加好友的用戶上
menu_id = secretFile.get("rich_menu_id")
server_url = secretFile.get("server_url")

from flask import Flask, request, abort

# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別
from linebot import (
    LineBotApi, WebhookHandler
)

# 引用無效簽章錯誤
from linebot.exceptions import (
    InvalidSignatureError
)

# 載入json處理套件
import json


# 設定Server啟用細節，這邊使用相對位置
app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/")


# 啟動server對外接口，使Line能丟消息進來
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#製作一個測試用接口
@app.route('/hello',methods=['GET'])
def hello():
    return 'Hello World!!'

from linebot.models import (
    MessageEvent, FollowEvent, JoinEvent,
    TextSendMessage, TemplateSendMessage,
    TextMessage, ButtonsTemplate,
    PostbackTemplateAction, MessageTemplateAction,
    URITemplateAction,ImageSendMessage,CarouselTemplate,CarouselColumn,
    FlexSendMessage,BubbleContainer
)

# 載入requests套件
import requests
button_template_message = CarouselTemplate(
            columns=[
                CarouselColumn(
                    #置換成自己要用的照片
                    thumbnail_image_url="https://%s/images/trends.gif" %server_url,
                    #置換成自己的名字
                    title='歡迎使用履歷機器人\n請使用下方功能選單\n或是按下方按鈕',
                    text='基本介紹',
                    actions=[
                        MessageTemplateAction(
                            label='操作簡介',
                            text='關於操作'
                        ),
                        MessageTemplateAction(
                            label='關於本程式',
                            text='關於本程式'
                        )                     
                    ]
                ),
                CarouselColumn(
                    #置換成自己要用的照片
                    thumbnail_image_url="https://%s/images/cc103.jpg" %server_url,
                    title='歡迎使用履歷機器人\n請使用下方功能選單\n或是按下方按鈕',
                    text='實作專題與調研',
                    actions=[
                        URITemplateAction(
                            label='CC103 網工班專題-GitHub',
                            uri='https://github.com/iii-cutting-edge-tech-lab/Chatbot_Project_cc103'
                        ),
                        URITemplateAction(
                            label='Dropboxpaper',
                            #改成你的作業連結
                            uri="https://paper.dropbox.com/folder/show/15_-e.1gg8YzoPEhbTkrhvQwJ2zz3XHPtTjRSmLwFVUUaV3Fe7F4PztNNA" 
                        )
                    ]
                ),
                   ]
            )

flexBubbleContainerJsonString_INTRO ="""
{
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "text",
          "text": "個人資料",
          "size": "lg",
          "align": "center",
          "weight": "bold",
          "color": "#000000"
        }
      ]
    },
    "hero": {
      "type": "image",
      "url": "https://i.imgur.com/HMs3Uq8.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover"
    },
    "body": {
      "type": "box",
      "layout": "horizontal",
      "spacing": "md",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "flex": 1,
          "contents": [
            {
              "type": "image",
              "url": "https://i.imgur.com/Nfjdz1h.jpg",
              "flex": 0,
              "align": "center",
              "gravity": "top",
              "size": "sm",
              "aspectRatio": "3:4",
              "aspectMode": "cover"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "flex": 2,
          "contents": [
            {
              "type": "text",
              "text": "Chinese Resume",
              "flex": 2,
              "size": "md",
              "align": "center",
              "gravity": "bottom",
              "weight": "bold",
              "action": {
                "type": "uri",
                "uri": "https://drive.google.com/file/d/1iJ9a47J_7OczwT-mqNAoFT5kWg-5pHV6/view?usp=sharing"
              }
            },
            {
              "type": "separator",
              "margin": "md"
            },
            {
              "type": "text",
              "text": "English Resume",
              "flex": 2,
              "size": "md",
              "align": "center",
              "gravity": "bottom",
              "weight": "bold",
              "action": {
                "type": "uri",
                "uri": "https://drive.google.com/file/d/1iJ9a47J_7OczwT-mqNAoFT5kWg-5pHV6/view?usp=sharing"
              }
            },
            {
              "type": "separator",
              "margin": "md"
            },
            {              
              "type": "text",
              "text": "Github Link",
              "flex": 2,
              "size": "md",
              "align": "center",
              "gravity": "bottom",
              "weight": "bold",
              "action": {
                "type": "uri",
                "uri": "https://github.com/harry10148/Resume"
              }
            }
          ]
        }
      ]
    }
  }
"""

flexBubbleContainerJsonString_CONTACT ="""
{
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "text",
          "text": "聯絡資訊",
          "size": "lg",
          "align": "center",
          "weight": "bold",
          "color": "#000000"
        }
      ]
    },
    "hero": {
      "type": "image",
      "url": "https://i.imgur.com/4w0AnpN.gif",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover"
    },
    "body": {
      "type": "box",
      "layout": "horizontal",
      "spacing": "md",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "flex": 1,
          "contents": [
            {
              "type": "image",
              "url": "https://i.imgur.com/vFH3Ayc.jpg",
              "flex": 0,
              "align": "center",
              "gravity": "top",
              "size": "sm",
              "aspectRatio": "3:4",
              "aspectMode": "cover"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "flex": 2,
          "contents": [
            {
              "type": "text",
              "text": "電話號碼",
              "flex": 2,
              "size": "md",
              "align": "center",
              "gravity": "bottom",
              "weight": "bold",
              "action": {
                "type": "message",
                "text": "關於李家豪的電話號碼"
              }
            },
            {
              "type": "separator",
              "margin": "md"
            },
            {
              "type": "text",
              "text": "Email",
              "flex": 2,
              "size": "md",
              "align": "center",
              "gravity": "bottom",
              "weight": "bold",
              "action": {
                "type": "message",
                "text": "關於李家豪的email"
              }
            },
            {
              "type": "separator",
              "margin": "md"
            },
            {              
              "type": "text",
              "text": "FaceBook",
              "flex": 2,
              "size": "md",
              "align": "center",
              "gravity": "bottom",
              "weight": "bold",
              "action": {
                "type": "message",
                "text": "關於李家豪的facebook"
              }
            }
          ]
        }
      ]
    }
  }
"""

flexBubbleContainerJsonString_WORK ="""
{
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "text",
          "text": "關於我",
          "size": "md",
          "align": "center",
          "gravity": "center",
          "weight": "bold",
          "color": "#000000"
        }
      ]
    },
    "hero": {
      "type": "image",
      "url": "https://i.imgur.com/2H6eo5b.jpg",
      "align": "center",
      "gravity": "center",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover"
    },
    "body": {
      "type": "box",
      "layout": "horizontal",
      "spacing": "md",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "flex": 1,
          "contents": [
            {
              "type": "image",
              "url": "https://i.imgur.com/fP2NvvY.jpg",
              "gravity": "bottom",
              "size": "sm",
              "aspectRatio": "4:3",
              "aspectMode": "cover"
            },
            {
              "type": "image",
              "url": "https://i.imgur.com/pKK7IBY.jpg",
              "margin": "md",
              "size": "sm",
              "aspectRatio": "4:3",
              "aspectMode": "cover"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "flex": 2,
          "contents": [
            {
              "type": "text",
              "text": "社團經歷",
              "flex": 1,
              "size": "xs",
              "align": "start",
              "gravity": "center",
              "weight": "bold",
              "color" : "#99ccff",
              "action": {
                "type": "message",
                "label": "mydata",
                "text": "我想看李家豪的社團經歷"
              }
            },
            {
              "type": "separator"
            },
            {
              "type": "text",
              "text": "職務經歷",
              "flex": 1,
              "size": "xs",
              "align": "start",
              "gravity": "center",
              "weight": "bold",
              "color" : "#99ccff",
              "action": {
                "type": "message",
                "label": "myhobby",
                "text": "我想看李家豪的職務經歷"
              }
            },
            {
              "type": "separator"
            },
            {
              "type": "text",
              "text": "證照",
              "flex": 1,
              "size": "xs",
              "align": "start",
              "gravity": "center",
              "weight": "bold",
              "color" : "#99ccff",
              "action": {
                "type": "message",
                "label": "mythought",
                "text": "我想看李家豪的證照"
              }
            },
            {
              "type": "separator"
            },
            {
              "type": "text",
              "text": "在資策會的學習狀況",
              "flex": 1,
              "size": "xs",
              "align": "start",
              "gravity": "center",
              "weight": "bold",
              "color" : "#99ccff",
              "action": {
                "type": "message",
                "label": "mythought",
                "text": "我想看李家豪在資策會的學習狀況"
              }
            },
             {
              "type": "separator"
            },
            {
              "type": "text",
              "text": "AWS組專題講解",
              "flex": 1,
              "size": "xs",
              "align": "start",
              "gravity": "center",
              "weight": "bold",
              "color" : "#99ccff",
              "action": {
                "type": "message",
                "label": "mythought",
                "text": "我想看李家豪AWS組專題講解"
              }
            },
            {
              "type": "separator"
            },
            {
              "type": "text",
              "text": "vSphere講解",
              "flex": 1,
              "size": "xs",
              "align": "start",
              "gravity": "center",
              "weight": "bold",
              "color" : "#99ccff",
              "action": {
                "type": "message",
                "label": "mythought",
                "text": "我想看李家豪vSphere講解"
              }
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "More",
            "uri": "https://www.facebook.com/chahao.li"
          },
          "gravity": "center"
        }
      ]
    },
    "styles": {
      "hero": {
        "backgroundColor": "#160D3A"
      }
    }
  }"""

from linebot.models import(
    FlexSendMessage,BubbleContainer,
)

import json

#INTRO樣板封裝
bubbleContainer_intro= BubbleContainer.new_from_json_dict(json.loads(flexBubbleContainerJsonString_INTRO))
flexBubbleSendMessage_INTRO =  FlexSendMessage(alt_text="個人介紹", contents=bubbleContainer_intro)

# #WORK樣板封裝
bubbleContainer_work= BubbleContainer.new_from_json_dict(json.loads(flexBubbleContainerJsonString_WORK))
flexBubbleSendMessage_WORK =  FlexSendMessage(alt_text="學習經歷", contents=bubbleContainer_work)

# #SKILLS樣板封裝
bubbleContainer_contact= BubbleContainer.new_from_json_dict(json.loads(flexBubbleContainerJsonString_CONTACT))
flexBubbleSendMessage_CONTACT =  FlexSendMessage(alt_text="聯絡資訊", contents=bubbleContainer_contact)

@handler.add(FollowEvent)
def reply_text_and_get_user_profile(event):
    
    # 取出消息內User的資料
    user_profile = line_bot_api.get_profile(event.source.user_id)
        
    # 將用戶資訊做成合適Json
    user_info = {  
        "user_open_id":user_profile.user_id,
        "user_nick_name":user_profile.display_name,
        "user_status" : "",
        "user_img" : user_profile.picture_url,
        "user_register_menu" : menu_id
    }
    
    # 將json傳回API Server
    Endpoint='http://%s:5000/user' % (ip_location)
    
    # header要特別註明是json格式
    Header={'Content-Type':'application/json'}
    
    # 傳送post對API server新增資料 
    Response=requests.post(Endpoint,headers=Header,data=json.dumps(user_info))
    
    #印出Response的資料訊息
    print(Response)
    print(Response.text)
    
    # 將菜單綁定在用戶身上
    # 要到Line官方server進行這像工作，這是官方的指定接口
    linkMenuEndpoint='https://api.line.me/v2/bot/user/%s/richmenu/%s' % (user_profile.user_id, menu_id)
    
    # 官方指定的header
    linkMenuRequestHeader={'Content-Type':'image/jpeg','Authorization':'Bearer %s' % secretFile["channel_access_token"]}
    
    # 傳送post method封包進行綁定菜單到用戶上
    lineLinkMenuResponse=requests.post(linkMenuEndpoint,headers=linkMenuRequestHeader)
                         
    #針對剛加入的用戶回覆文字消息、圖片、旋轉門選單
    reply_message_list = [
                    TextSendMessage(text="歡迎%s\n感謝您加入履歷機器人\n想多了解我請使用下方功能選單\n或是按下方按鈕" % (user_profile.display_name) ),    
                    TemplateSendMessage(alt_text="履歷功能選單，為您服務",template=button_template_message),
                ]
    
    #推送訊息給官方Line
    line_bot_api.reply_message(
        event.reply_token,
        reply_message_list    
    )
    

from linebot.models import PostbackEvent

#parse_qs用於解析query string
from urllib.parse import urlparse,parse_qs

#用戶點擊button後，觸發postback event，對其回傳做相對應處理
@handler.add(PostbackEvent)
def handle_post_message(event):
    #抓取user資料
    user_profile = event.source.user_id
    
    #抓取postback action的data
    data = event.postback.data
    
    #用query string 解析data
    data=parse_qs(data)
               
    #給按下"yourName自我介紹"，"yourName工作經驗"，"yourName的專長"，推播對應的flexBubble
    if (data['type'] ==['Introduction']):
            line_bot_api.reply_message(
                event.reply_token,
                flexBubbleSendMessage_INTRO
            )
    elif (data['type']==['Work']):
            line_bot_api.reply_message(
                event.reply_token,
                flexBubbleSendMessage_WORK
            )
    elif (data['type']==['Contact']):
            line_bot_api.reply_message(
                event.reply_token,
                flexBubbleSendMessage_CONTACT
            )
    #其他的pass
    else:
        pass
@handler.add(MessageEvent, message=TextMessage)
#將這次event的參數抓進來
def handle_message(event):
    user_profile = event.source.user_id
    
    # 當用戶輸入VMware時判斷成立
    if (event.message.text.find('我想看李家豪vSphere講解')!= -1):
        # 提供VMware作業網址
        url1='https://www.youtube.com/watch?v=0pDMV9MJQc0'
        url2='https://www.youtube.com/watch?v=rVSBTbm9ytU'
        # 將上面的變數包裝起來
        reply_list = [
            TextSendMessage(text="VMware Network 講解:\n%s" % (url1)),
            TextSendMessage(text="VMware vMotion 講解:\n%s" % (url2))
        ]
        # 回覆訊息
        line_bot_api.reply_message(
            event.reply_token,
            reply_list
            )
    
    # 當用戶輸入Linux Server時判斷成立
    elif (event.message.text.find('我想看李家豪AWS組專題講解')!= -1):
        # 提供Linux Server作業網址
        url1='https://www.youtube.com/watch?v=--hwH3vGtjE'
        # 將上面的變數包裝起來
        reply_list = [
            TextSendMessage(text="專題AWS部分講解:\n%s" % (url1))
        ]
        # 回覆訊息
        line_bot_api.reply_message(
            event.reply_token,
            reply_list
            )
         # 當用戶輸入Linux Server時判斷成立
    elif (event.message.text.find('我想看李家豪的社團經歷')!= -1):
        # 提供Linux Server作業網址
        url1='https://www.youtube.com/watch?v=CBr6N1gstLA&t=8'
        # 將上面的變數包裝起來
        reply_list = [
            TextSendMessage(text="在社團擔任樂團吉他手，此為表演影片:\n%s" % (url1))
        ]
        # 回覆訊息
        line_bot_api.reply_message(
            event.reply_token,
            reply_list
            )
    elif (event.message.text.find('我想看李家豪在資策會的學習狀況')!= -1):
        # 提供Linux Server作業網址
        url1='https://drive.google.com/open?id=1rjXgxCQqCuDkoRTYSBp4xs2cD61MUJVnHgRhp3f-epQ'
        url2='https://drive.google.com/open?id=1aojm8B2yc37tFX0QaGReYCO9Cy-lU8lnQwzP4LofoGs'
        # 將上面的變數包裝起來
        reply_list = [
            TextSendMessage(text="在資策會裡學習了關於大量網路相關知識，其中也包括大量的實作"),
            TextSendMessage(text="TLS1.2與TLS1.3之差別:\n%s" % (url1)),
            TextSendMessage(text="DNSSEC調研:\n%s" % (url2))
        ]
        # 回覆訊息
        line_bot_api.reply_message(
            event.reply_token,
            reply_list
            )
        
    # 當用戶輸入"資安簡報"時判斷成立
    elif (event.message.text.find('我想看李家豪的證照')!= -1):
        # 提供資安實作簡報網址
        url1='https://www.redhat.com/rhtapps/services/verify?certId=140-011-735'
        # 將上面的變數包裝起來
        reply_list = [
            TextSendMessage(text="RHCE:\n%s" % (url1))
        ]
        # 回覆訊息
        line_bot_api.reply_message(
            event.reply_token,
            reply_list
            )
    
    # 結合旋轉門選單中的"yourName自我介紹"，進到flexbubble選單，按下"yourName 平時興趣"，會有文字"我想看yourName的平時興趣"的輸入，當符合字串時判斷成立
    elif (event.message.text.find('關於李家豪的電話號碼')!= -1):
        # 回覆訊息
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="0903123347")
            )
    
    # 結合旋轉門選單中的"yourName自我介紹"，進到flexbubble選單，按下"yourName 能為公司做的貢獻"，會有文字"我想看yourName的想法"的輸入，當符合字串時判斷成立
    elif (event.message.text.find('關於李家豪的email')!= -1):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="harry10148@gmail.com")
            )
    
    # 結合旋轉門選單中的"yourName工作經驗"，進到flexbubble選單，按下"yourName 在資策會的學習狀況"，會有文字"我想看yourName在資策會的學習狀況"的輸入，當符合字串時判斷成立
    elif (event.message.text.find('我想看李家豪的職務經歷')!= -1):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="在in墅館餐廳工作了大約4年的時間，在這段時間裡擔任外場管理以及培育新人的部分。\n在此環境下讓我深刻的理解，在與同事間的溝通的重要性，其中要與內場溝通並了解其運作狀況，在即時調整外場點餐接客狀況等等")
            )
        
    # 結合旋轉門選單中的"yourName的專長"，進到flexbubble選單，按下"yourName 的外語能力"，會有文字"我想看yourName的外語能力"的輸入，當符合字串時判斷成立
    elif (event.message.text.find('關於李家豪的facebook')!= -1):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="https://www.facebook.com/chahao.li")
            )
        
    # 結合旋轉門選單中的"yourName的專長"，進到flexbubble選單，按下"yourName 的IT專長"，會有文字"我想看yourName的IT專長"的輸入，當符合字串時判斷成立
    elif (event.message.text.find('關於李家豪的github')!= -1):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="https://github.com/harry10148/Resume")
            )
    
    # 結合旋轉門選單中的"yourName的專長"，進到flexbubble選單，按下"yourName 的其他專長"，會有文字"我想看yourName的其他專長"的輸入，當符合字串時判斷成立
    elif (event.message.text.find('關於操作')!= -1):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="下方四個圖示分別為\n中英文履歷、聯絡資訊、更多個人資訊、回到開始")
            )
    elif (event.message.text.find('關於本程式')!= -1):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="本程式為中壢資策會網工班cc103的AWS考古題機器人專題之延伸\n利用專題所學將原本專題的機器人簡化，加入一些紙本履歷上未提及的個人資訊")
            )
   
    # 收到不認識的訊息時，回覆原本的旋轉門菜單    
    else:         
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text="感謝您加入履歷機器人\n想多了解我請使用下方功能選單\n或是按下方按鈕\n",
                template=button_template_message
            )
        )          

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

