from django.shortcuts import render
from django.http import HttpResponse
import time



# Create your views here.

def home(request):
    '''
    start_time = time.time()

    # Get input from the user
    response = input("Start the counter? (Y/N)")

    # If the user inputs 'Y', continue running the counter
    while response == 'Y':
        response = input("Continue the counter? (Y/N)")

        # When the user inputs 'N', stop the counter and print the elapsed time
    if response == 'N':
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")'''

    return render(request,'home.html')

def tests(request):
    return render(request,'tests.html')