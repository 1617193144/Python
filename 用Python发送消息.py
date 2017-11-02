import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'DS757556644@126.com'
msg['to'] = '757556644@qq.com'
msg['subject'] = 'test'
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
