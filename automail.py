
import yagmail
import os
import datetime


date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
user_mail = "riks.rs18@gmail.com"
#user_password = input("enter user {}'s password:".format(user_mail))
user_password = "Google001"
yag = yagmail.SMTP(user=user_mail, password=user_password)
#yag = yagmail.SMTP("riks.rs18@gmail.com", oauth2_file="~/oauth2_creds.json")
#recipients = ['tafiquemd@gmail.com','sanskruti324@gmail.com','manisha.maharana1998@gmail.com']
recipients = input("Enter recivier's mail id: ").split(",")
yag.send(to=recipients,subject=sub,attachments= filename)
print("Email Sent!")
