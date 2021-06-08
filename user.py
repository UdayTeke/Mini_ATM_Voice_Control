from Atm.Saving.saving import*
from Atm.current.current import*
import pyttsx3
from datetime import datetime
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

print('^'*50)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today=datetime.today()
print('Bank of India',today)
print('^'*50)
def user_Info():
    temp='1234'
    print('Please Enter your password')
    speak('Please Enter your password!')
    password=input('')
    print('^'*50)
    try:
        if password!=temp:
            raise ValueError("Invalid Password")
            
    except ValueError as ve:
        print(ve) 
    else:   
        
        print(r'1)saving 2)current')
        speak('choose your account type')
        op=int(input(''))
        print('^'*50)
        if op==1:
            saving()
        elif op==2:
            current()
        else:
            speak('Invalid Option')


    print('^'*50)
    print('Thank you for using this ATM')
    speak('Thank you for using this ATM')
    return
if __name__=="__main__":
    speak("Welcome to this Atm")
user_Info()

