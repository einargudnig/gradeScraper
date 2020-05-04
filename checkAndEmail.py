import os

from bs4 import BeautifulSoup
import smtplib

EMAIL_ADDRESS =  os.environ.get('GRADE_EMAIL_SENDER')
EMAIL_PASSWORD = os.environ.get('GRADE_EMAIL_SENDER_PW')
RECIEVER = 'einargudnig@gmail.com'

with open('uglaHTML.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

if str(soup).count("olokid gildir_kanski_til_gradu info") < 2:

    print('Do I have new grade??')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'You have new grade!?!!!!!!!!!!!!!!!1!'
        body = 'The gradeScraper3000 thinks you should check your grades.'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, RECIEVER, msg)


else:
    # We do not have a new grade.
    print('You do not have new grade!')

