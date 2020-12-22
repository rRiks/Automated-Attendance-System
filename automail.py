import body as body
import yagmail
import os
import datetime
from Tools.demo.mcast import receiver

date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
user_mail = "ajitsahurandi@gmail.com"
user_password = input("enter user {}'s password:".format(user_mail))

yag = yagmail.SMTP(user=user_mail, password=user_password)
#yag = yagmail.SMTP("riks.rs18@gmail.com", oauth2_file="~/oauth2_creds.json")
recipients = ['tafiquemd@gmail.com']
yag.send(to=recipients,subject=sub,contents= "https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16",attachments= filename)
print("Email Sent!")
