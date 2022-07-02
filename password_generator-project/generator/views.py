from django.shortcuts import render
import random

# Create your views here.

def Home(request):
    fix_password = request.GET.get('')
    context = {'fix_password':fix_password}
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')    

def password(request):

    alp_list = list('qwertyuiopasdfghjklzxcvbnm')
    chr_list = list('!@#$%^&*+-')
    upp_list = list('QWERTYUIOPASDFGHJKLZXCVBNM')
    num_list = list('1234567890')

    fin_password = ''

    length_password = int(request.GET.get('lenght'))

    if request.GET.get('uppercase'):
        alp_list = alp_list + upp_list
    if request.GET.get('number'):
        alp_list = alp_list + num_list
    if request.GET.get('character'):
        alp_list = alp_list + chr_list    

    for i in range(length_password):
        fin_password += random.choice(alp_list)
    fix_password = fin_password    

    context = {'fin_password':fin_password, 'fix_password':fix_password}
    return render(request, 'generator/password.html', context)    