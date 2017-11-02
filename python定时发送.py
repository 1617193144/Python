import smtplib
import email.mime.multipart
import email.mime.text
import time

def sleeptime (min,sec):
    return min*60+sec;
second = sleeptime(3,0)
while 1 == 1:
    time.sleep(second);
msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'DS757556644@126.com'
msg['to'] = '757556644@qq.com'
msg['subject'] = '杜双 你好'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com', '25')
smtp.login('DS757556644@126.com', 'ZXCVBNM121299')
smtp.sendmail('DS757556644@126.com', '757556644@qq.com', str(msg))
smtp.quit()
