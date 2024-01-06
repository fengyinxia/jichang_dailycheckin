import requests, json, re, os

session = requests.session()
# 配置用户名（一般是邮箱）
email = os.environ.get('EMAIL')
# 配置用户名对应的密码 和上面的email对应上
passwd = os.environ.get('PASSWD')


login_url = '/auth/login'
check_url = '/user/checkin'
info_url = '/user/profile'
origin_url = 'https://ikuuu.me'
ui = 'https://'
test_text = '官网域名已更改'

header = {
        'origin': 'https://ikuuu.me',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
        'email': email,
        'passwd': passwd
}

url_test = requests.get(origin_url)
op = re.compile(r'官网域名已更改') 
test = op.findall(url_test.text)
if test[0] !='':         
      a = re.compile(r'ikuuu.[a-z]{2,}') 
      b = a.findall(url_test.text)[0]
      response = json.loads(session.post(url=ui+b+login_url,headers=header,data=data).text)
      print(response['msg']) 
      info_html = session.get(url=ui+b+info_url,headers=header).text
      result = json.loads(session.post(url=ui+b+check_url,headers=header).text)
      print(result['msg'])
else:
     response = json.loads(session.post(url=origin_url+login_url,headers=header,data=data).text)
     print(response['msg']) 
     info_html = session.get(url=origin_url+info_url,headers=header).text
     result = json.loads(session.post(url=origin_url+check_url,headers=header).text)
     print(result['msg'])  

