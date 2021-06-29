import smtplib

carriers = {'att':'@mms.att.net', 'tmobil': '@tmomail.net', 'verizon':
            '@vtext.com', 'sprint': '@page.nextel.com'} 
contact = list('PhoneNumber')

def Send(message):
    toNumb = contact[0]+'{}'.format(carriers['verizon'])
    auth = ('email', 'password')
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], toNumb, message)
