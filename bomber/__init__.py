import smtplib
import time, os, json

"""
Email Bomber
- Quick
- Easy, Reliable | adolf#6900 + bongo#0564
"""

class EmailBomber:
      def __init__(
          self,
          email,
          password
      ):
          self.email    = email
          self.password = password
          
          self.server   = smtplib.SMTP('smtp-mail.outlook.com', 587)
      
      def setup(
          self,
          subject = "",
          content = "",
      ): 
          self.server.ehlo()
          self.server.starttls()

          self.body = ""
          self.body = "From: %s\nMessage: %s" % (
               self.email,
               content,
          )
      
      def send(
          self,
          target = ""
      ): 
          self.server.login(
               self.email, self.password
          )
          
          if self.body != None or "":
             self.server.sendmail(
                  self.email,

                  target,
                  self.body
             ), self.server.quit()
