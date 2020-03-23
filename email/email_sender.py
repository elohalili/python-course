import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'anyone'
email['to'] = 'bajaho5001@newe-mail.com'
email['subject'] = 'sub'

email.set_content('This is the email content')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mail', 'password')
    smtp.send_message(email)
