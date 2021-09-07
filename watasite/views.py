from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    
    if request.method == 'POST':
        namaCL = request.POST.get('nama')
        emailCL = request.POST.get('email') 
        msgCL = request.POST.get("message")
        
        formCL = {
            'name' : namaCL,
            'email' : emailCL,
            'message' : msgCL
        }

        message = '''
            Name : {}
            Message : {}
            
            From : {}
        '''.format(formCL['name'],formCL['message'],formCL['email'])
        send_mail(formCL['message'],message,'',['nekocyber3@gmail.com'])
        
    return render(request,'index.html')
    