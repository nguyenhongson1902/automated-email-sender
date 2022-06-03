import requests # http requests
from bs4 import BeautifulSoup # web scraping
import smtplib # send the email
from email.mime.multipart import MIMEMultipart # email body
from email.mime.text import MIMEText # email body
import datetime

now = datetime.datetime.now()

content = ''

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = '' # to contain email content
    cnt += '<b>HN Top Stories :</b>\n' + '<br>' + '-'*50 + '<br>'
    response = requests.get(url) # send a http request
    content = response.content # get the content from the http
    soup = BeautifulSoup(content, 'html.parser')
    # find all tags 'td' with the attribute 'class' is 'title' and 'valign' is empty 
    for i, tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign':''})):
        cnt += (str(i+1) + ' :: ' + tag.text + '\n' + '<br>') if tag.text != 'More' else ""
    return cnt


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += '<br>------<br>'
content += '<br><br>End of message'


print('Composing email...')

SERVER = 'smtp.office365.com'
PORT = 587
FROM = 'your email address' # change this
TO = 'to which we want to send email' # change this, it can be a list if you want to send email to many people
PASS = 'password of your email address' # change this



msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))


print('Initializing server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1) # 0 to not see the error messages
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email sent...')
server.quit()

