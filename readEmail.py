import smtplib
import time
import imaplib
import email
import base64

def readEmail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('email', 'password')
    mail.select('inbox')

    response,data = mail.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])

    response,data = mail.fetch(str(latest_email_id), '(RFC822)')

    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[-1].decode())
            email_subject = msg['subject']
            email_from = msg['from']
            print('From: ' + email_from + '\n')
            print('Subject: ' + email_subject + '\n')
                
    while msg.is_multipart():
        msg = msg.get_payload(-1)

    content = msg.get_payload(decode=True)
    content = str(content)

    
    try:
        content = content.split('>')
        content = content[1].split('<')
        print(content[0])

    except IndexError:
        content = content[0].split("'")
        content = content[1].split('\\')
        print(content[0])
