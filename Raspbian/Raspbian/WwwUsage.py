def getWeb(url):
    import urllib2
    contents = urllib2.urlopen(url).read()
    print(contents)

def sendMail():
    import smtplib
    import getpass    

    print("Podaj nazwe uzytkownika gmail")
    GMAIL_USER = raw_input()
    print("Podaj haslo")
    GMAIL_PASSWD = getpass.getpass()
    SMPT_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    smtpserver = smtplib.SMTP(SMPT_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(GMAIL_USER, GMAIL_PASSWD)
    print("Podaj odbiorce")
    RECIPIENT = raw_input()
    print("Podaj tytuł")
    SUBJECT = raw_input()
    print("Podaj wiadomosc")
    CONTENT = raw_input()
    header = "Do: {}\nOd: {}\nTemat: {}\n".format(RECIPIENT, GMAIL_USER, SUBJECT)
    message = header+"\n"+CONTENT
    smtpserver.sendmail(GMAIL_USER, RECIPIENT)
    smtpserver.close()

def HostWebService():
    #use on environment with installed python-bottle
    from bottle import route, run, template
    from datetime import datetime
    @route('/')
    def index(name='time'):
        dt = datetime.now()
        time="{:%Y-%m-%d %H:%M:%%S}".format(dt)
        return template('<b>Date now: {{t}}</b>', t=time)
    run(host='10.0.0.222', port=80)
    

def __init__():
    #getWeb("https://www.google.pl")
    #sendMail()    
    HostWebService()

__init__()