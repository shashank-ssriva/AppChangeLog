from lxml import html
import requests
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Checking if user inputs a URL & feature or not.
if len(sys.argv) < 3:
    print("No URL & Feature specified. Kindly specify a valid PlayStore App URL and your chosen feature. Exiting now...")
    sys.exit()

enterURL = sys.argv[1]
featureRequest = sys.argv[2]
print(enterURL)
page = requests.get(enterURL)
tree = html.fromstring(page.content)
new = tree.xpath('//div[@class="recent-change"]/text()')
def notify(text):
    Notifier.notify(text)
print("Below is the change log :")
i = 1
for items in new:
    print(i, ":" , items)
    i += 1
    if featureRequest in items:
        print("Feature %s added!!" %featureRequest)
        
        #Setting up the SMTP Server
        smtpServer = smtplib.SMTP(host='YOUR_SMTP_SERVER', port=25)
        smtpServer.starttls()
        smtpServer.login("SMTP_SERVER_USERNAME", "SMTP_SERVER_PASSWORD")
        msg = MIMEMultipart()
        msg['From'] = "Shashank-Srivastava"
        msg['To'] = "you@your_email_address"
        msg['Subject'] = "Here is the Feature you were waiting for!"
        msg.attach(MIMEText(items, 'plain'))
        smtpServer.send_message(msg)
        smtpServer.quit()
        print("Mail has been sent to %s." %msg['To'])
    else:
        print("Feature %s not found in the change-logs. So, no mail was sent." %featureRequest)
