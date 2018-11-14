import requests
from lxml import etree
from source import *
from time import sleep

print('LOGIN=================================================================')
s = requests.session()
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Origin': 'http://ntucoder.net',
    'Upgrade-Insecure-Requests': '1'
}
s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'})
payload = {'Email': 'anhvjp123z@gmail.com', 'MatKhau': '123456', 'RememberMe': 'true', 'x': '52', 'y': '21'}
url = 'http://ntucoder.net/Account/LogIn'
p = s.post(url, data=payload)
# print(p.text)
for prl in idprl:
    print('processing: ', prl)
    # print('GET VERIFYTOKEN=================================================================')
    urlprl = 'http://ntucoder.net/Submission/Submit/?problemid=' + prl
    tokenRequest = s.get(urlprl)
    # print(tokenRequest.text)
    parser = etree.HTMLParser()
    tree = etree.fromstring(tokenRequest.text, parser)
    verificationToken = tree.xpath('//form//input[@name="__RequestVerificationToken"]/@value')[0]
    problemCode = tree.xpath('//form//input[@name="ProblemCode"]/@value')[0]
    sessionCookies = tokenRequest.cookies
    # print(verificationToken)
    # print(problemCode)
    f = open('./sourcecodes/' + prl + '.txt', 'r')
    temp = f.readline()
    temp = f.readlines()
    code = ''.join(temp)
    payload = {
        '__RequestVerificationToken': verificationToken,
        'ContestID': '',
        'ProblemCode': problemCode,
        'CompilerID': '1',
        'SubmitCode': code,
        'file': '',
        'button': 'Submit'
    }
    urlSubmit = 'http://ntucoder.net/Submission/Submit/?problemid=' + prl

    p2 = s.post(urlSubmit, data=payload, cookies=sessionCookies, headers=headers)
    print('done: ', prl, ' - ', p2.status_code)
    sleep(20)