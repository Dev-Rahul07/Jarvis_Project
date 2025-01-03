import pyttsx3  # This module is help the system to speak
import speech_recognition as sr  #This module is help to recognise the speech that user said
import random
import webbrowser
import datetime
from api_data import api_key
from AI import generate_response


# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 190)  # Control the speed of Jarvis voice
# This function is used to speak out the system
def speak(audio):
    engine.say(audio)
    engine.runAndWait()




todo_file = 'todo.txt'

def add_task():
    task = input('Enter the task that you want to add to your to-do list:\n')
    if task.strip():  # Ensures the task is not empty
        with open(todo_file, 'a') as file:
            file.write(task + '\n')
        print(f'Task added: {task}')
        speak(f'Task added: {task}')
    return

 

def remove_task():
    with open(todo_file, 'r') as file:
        tasks = file.readlines()
    if not tasks:
        print('Your to-do list is empty.')
        speak('Your to-do list is empty.')

        return

    print('Your to-do list:')
    speak('Your to-do list:')
    
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task.strip()}')
        speak(f'{i}. {task.strip()}')

    try:
        task_number = int(input('Enter the number of the task you want to remove:\n'))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            with open(todo_file, 'w') as file:
                file.writelines(tasks)
            print(f'Task removed: {removed_task.strip()}')
            speak(f'Task removed: {removed_task.strip()}')
        else:
            print('Invalid task number.')
            speak('Invalid task number.')
    except ValueError:
        print('Please enter a valid number.')
        speak('Please enter a valid number.')
        return

# Obtain audio from the microphone
def command():
    content = ' '
    # content = input('enter the command ')
    while content == ' ':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listing....")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language ='en-in')
            print('You said :' + content)
        
        except Exception as e:
            print('Not understanding...')
            
    return content


def init_jarvis(request):
    if 'hello jarvis' in request:
        speak('welcome i am jarvis ,How are you..')
        print('welcome i am jarvis ,How are you..')


def main_process():
    while True:
        request  = command().lower()
        init_jarvis(request)
        if'open google' in request:
            webbrowser.open('https://www.google.com')

        elif'open LinkedIn' in request:
            webbrowser.open('https://www.linkedin.com/feed/')


        # play music
        elif 'play music' in request:
            speak('playing music..')
            song = random.randint(1,4)
            if song == 1:
                webbrowser.open('https://www.youtube.com/watch?v=QwL0rLScmyU')
            elif song == 2 :
                 webbrowser.open('https://www.youtube.com/watch?v=LaJqBhfcrhQ')
            elif song == 3:
                 webbrowser.open('https://www.youtube.com/watch?v=UdsO4SM4wKI')
            elif song == 4 :
                webbrowser.open('https://www.youtube.com/watch?v=eM8Mjuq4MwQ')
        # time
        elif 'time' in request:
            now_time = datetime.datetime.now().strftime('%H:%M:%S')
            speak('the current time is ' + str(now_time))
            print('the current time is ' + str(now_time))
        # date
        elif 'date' in request:
            now_date = datetime.datetime.now().strftime('%Y-%m-%d')
            speak('the current date is ' + str(now_date))
            print('the current date is ' + str(now_date))

        # day
        elif 'day' in request:
            now_day = datetime.datetime.now().strftime('%A')
            speak('the current day  is ' + str(now_day))
            print('the current day  is ' + str(now_day))



        # todo list adding task
        elif 'add new work' in request:
            add_task()
    


        # remove task form todo list
        elif 'remove work' in request:
            remove_task()
           




        elif 'to do list' in request:
             with open('todo.txt','r') as file:
                task = file.read()
                speak(task)
                print(task)


        elif 'generate response' in request:
            print('what is your question ..')
            speak('what is your question ..')
            qurrey = str(command())
            output = generate_response(qurrey)
            speak(output)

                


        elif 'goodbye jarvis' in request:
            print('jarvis :  Goodbye have a great day\n')
            speak('Goodbye! Have a great day')
            break

        





main_process()