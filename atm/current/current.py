import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def current():
    balance=int(7000)
    print(r'1)check balance 2)cash Withdrawl')
    speak('Choose your option')
    opp=int(input(''))
    if opp==1:
        print('your balance is Rs.',balance)
        speak(r'Your balance is rupees')
        speak(balance)
    elif opp==2:
        speak('Enter amount to withdraw')
        raise ZeroDivisionError(Exception)
          
        print('please! collect your cash')
        speak('Please! collect your cash...')
        print('Now your balance is Rs.',balance)
        speak('Now your balance is Rupees')
        speak(balance)
    else:
        speak('Invalid option')
    return
