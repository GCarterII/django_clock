from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def word(request, len = 14):
    if 'count' in request.session:
        request.session['count'] += 1 #request.session.count + 1
    else:
        request.session['count'] = 1

    # len2 = str(len)


    unique_id = get_random_string(length=int(len), allowed_chars='abcdefghijklmnopqrstuvwxyz')
    

    context = {
        'random_word': unique_id 
    }

    return render(request, "random_word/index.html", context)

def clear(request):

    if 'count' in request.session:
        del request.session['count']

    return redirect('/random_word/')

# Create your views here.
