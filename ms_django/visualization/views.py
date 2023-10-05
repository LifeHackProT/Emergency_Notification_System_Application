from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Patient, fall
import bcrypt
import sysv_ipc
import threading


BUFF_SIZE = 16
TYPE_STRING = 1

def receiver(request):
    try:
        mq = sysv_ipc.MessageQueue(1234, sysv_ipc.IPC_CREAT)

        # This part can be run in a separate thread or as a periodic task using Celery, depending on your use case.
        while True:
            message, mtype = mq.receive()
            print("*** New message received ***")
            print(f"Raw message: {message}")
            if mtype == TYPE_STRING:
                str_message = message.decode()
                print(f"Interpret as string: {str_message}")
                if str_message == "sample string":
                    # Assuming you have a FallData model and a 'fall' method in your models.py
                    fall_data = FallData.objects.create(data=str_message)
                    fall_data.save()

    except sysv_ipc.ExistentialError:
        print("ERROR: message queue creation failed")

    # Return a response or render a template as needed
    return JsonResponse({'status': 'success'})

def start_receiver_thread():
    receiver_thread = threading.Thread(target=receiver)
    receiver_thread.daemon = True  # Set as a daemon thread so it exits when the main program ends
    receiver_thread.start()


def index(request):
    return render(request, 'index.html')

def alarm(request):
    fall_list = fall.objects.all()
    return render(request, 'alarm.html', context={'fall_list': fall_list})

def createform(request):
    if request.method == 'POST':
        name = request.POST['name']
        birth_date = request.POST['birth_date']
        location = request.POST['location']
        disease_name = request.POST['disease_name']
        # password = request.POST['password']
        # password = password.encode()
        # password = bcrypt.hashpw(password, bcrypt.gensalt())
        # password = password.decode()
        patient = Patient(name=name, birth_date=birth_date, location=location, disease_name=disease_name)
        patient.save()
    return redirect('index')

if __name__ == "__main__":
    start_receiver_thread()

    # ... your other code ...
