import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def info_shower():
    try:
        with sr.Microphone() as source:
            print('listening--->')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        print("don't recognize anything--->")

email_id = {
    "nick name for reciever email id": "type email id here" # you add more email id creating nick name here
}

def send_email(send_to,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    server.login('type sender email id', password='type password here')
    email = EmailMessage()
    email['From'] = 'sender email id'
    email['To'] = send_to
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


def get_email_info():
    talk('hello lazy dude. i am your email sender bot . tell me the name to send email')
    #naming part
    name = info_shower()
    send_to = email_id[name]
    talk('you are sending email to:',)
    talk(send_to)
    print(send_to)

    #subject part
    talk('tell me the subject')
    subject = info_shower()

    #messeging part
    talk('tell me your message')
    message = info_shower()

    send_email(send_to,subject,message)
    talk(' your email is sent lazy dude')
    talk(' Thank you for using me dude')
    print('\n')
    print('Thanks for using.....')



get_email_info()