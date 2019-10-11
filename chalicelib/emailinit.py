import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Messenger:
    def smtpinit(self):
        try:
            emailhost = os.environ('EMAILHOST')
            emailport = os.environ('EMAILPORT')
            emailusername = os.environ('EMAILUSERNAME')
            emailpassword = os.environ('EMAILPASSWORD')
            server = smtplib.SMTP(emailhost,emailport)
            server.starttls() # Secure the connection
            server.login(emailusername, emailpassword)
            return server
        except Exception as e:
            print(e)
        finally:
            server.quit() 
    
    def sendplainemail(self, em_to, em_subject, em_from, em_msg):
        sender_email = em_from
        receiver_email = em_to
        subject = em_subject
        message = em_msg
        s = self.smtpinit()
        res = s.sendmail(sender_email, receiver_email, message)
        return res

    def sendhtmlemail(self, em_to, em_subject, em_from, em_msg):
        msg = MIMEMultipart()
        msg['From']= em_from
        msg['To']= em_to
        msg['Subject']= em_subject
        msg.attach(MIMEText(em_msg, 'html'))
        s = self.smtpinit()
        res = s.sendmail(msg)
        return res