import smtplib
from email.message import EmailMessage
app_password='ykqa fzbh hvjy htaw'
def send_mail(to,body,subject):
  server=smtplib.SMTP_SSL('smtp.gmail.com',465)
  server.login('bathulamanojkumar11@gmail.com',app_password)
  msg=EmailMessage()
  msg['FROM']='bathulamanojkumar11@gmail.com'
  msg['TO']=to
  msg['SUBJECT']=subject
  msg.set_content(body)
  server.send_message(msg)
  server.close()
  