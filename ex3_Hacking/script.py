# passwords.csv provided by Codecademy learning platform

# Reading In The Passwords
import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

compromised_users = []
with open(os.path.join(__location__,'passwords.csv')) as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    password_row = row
    compromised_users.append(password_row['Username'])
    
with open(os.path.join(__location__,'compromised_users.txt'), 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)
    
# Notifying the Boss
import json

with open(os.path.join(__location__, 'boss_message.json'), 'w') as boss_message:
  boss_message_dict ={
    "recipient" : "The Boss",
    "message" : "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)
  
# Scrambling the Password
with open(os.path.join(__location__, 'new_passwords.csv'), 'w') as new_passwords_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)
  
  
  