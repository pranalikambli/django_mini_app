from django.shortcuts import render

def index(request):
    context= {'name': 'Emma SILVA', 'about':'SOFTWARE DEVELOPER & GAME ADDICT'}
    return render(request, "index.html",  context)

def about(request):
    context = {'name': 'Emma SILVA', 'skills': ['Python','Java','PHP','.Net'], 'user_id':'emma123',
               'email':'emma@gmail.com', 'about':'SOFTWARE DEVELOPER & GAME ADDICT', 'phone': '0000000000', 'profession': 'Software Developer'}
    return render(request, "about.html", context)