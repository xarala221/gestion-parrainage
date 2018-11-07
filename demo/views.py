from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utils.http import is_safe_url
from .models import *
from .forms import LoginForm

@login_required(login_url='/sign_in/')
def index(request):
  context = {}
  return render(request, "demo/index.html", context)



User = get_user_model()
def sign_in(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['profile'] = User.objects.count()
            print('sesssion begin')
            # print(request.session['profile'])
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/')
    else:
        print("Error 3")
    return render(request, "auth/login.html", context)

def log_out(request):
    if 'profil' in request.session:
        del request.session['profil']

    logout(request)
    return redirect('/sign_in/')

@login_required(login_url='/sign_in/')
def homepage(request):
    total = Parraine.objects.all().count()
    context = {
        'total':total
    }
    return render(request, "demo/home.html", context)


@login_required(login_url='/sign_in/')
def analyse(request):
    total = Parraine.objects.all().count()
    # print("Total ", total)
    dakar = Parraine.objects.filter(region__iexact="Dakar").count()
    # print("dakar ", dakar)
    diourbel = Parraine.objects.filter(region__iexact="Diourbel").count()
    # print("Diourbel ", diourbel)
    fatick = Parraine.objects.filter(region__iexact="Fatick").count()
    # print("Fatick ", fatick)
    kaffrine = Parraine.objects.filter(region__iexact="Kaffrine").count()
    # print("Kaffrine ", kaffrine)
    kaolack = Parraine.objects.filter(region__iexact="Kaolack").count()
    # print("kaolack ", kaolack)
    kedougou = Parraine.objects.filter(region__iexact="Kédougou").count()
    # print("kedougou ", kedougou)
    matam = Parraine.objects.filter(region__iexact="Matam").count()
    # print("Matam ", matam)
    saint_louis = Parraine.objects.filter(region__iexact="Saint-Louis").count()
    # print("saint_louis ", saint_louis)
    sedhiou = Parraine.objects.filter(region__iexact="Sédhiou").count()
    # print("Sédhiou ", sedhiou)
    tambacounda = Parraine.objects.filter(region__iexact="Tambacounda").count()
    # print("Tambacounda ", tambacounda)
    thies = Parraine.objects.filter(region__iexact="Thiès").count()
    # print("thies ", thies)
    ziguinchor = Parraine.objects.filter(region__iexact="Ziguinchor").count()
    # print("Ziguinchor ", ziguinchor)
    kolda = Parraine.objects.filter(region__iexact="Kolda").count()
    # print("Kolda ", kolda)
    louga = Parraine.objects.filter(region__iexact="Louga").count()
    # print("Louga ", louga)
    context = {
        'dakar':dakar,
        'diourbel':diourbel,
        'fatick':fatick,
        'kaffrine':kaffrine,
        'kaolack':kaolack,
        'kedougou':kedougou,
        'matam':matam,
        'saint_louis':saint_louis,
        'sedhiou':sedhiou,
        'tambacounda':tambacounda,
        'thies':thies,
        'ziguinchor':ziguinchor,
        'kolda':kolda,
        'louga':louga,
        'total':total


    }
    return render(request, "dashboard/dashboard.html", context)


# search view 
def search(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:            
            results = Fichier.objects.filter(  
            	Q( numero_electeur__iexact = q ) |
                Q( numero_identification__iexact = q ) )  
            print("q", q)
            print("resula", results)        
            return render(request, 'demo/results.html', {'results': results})

def mon_electeur(request):
    keyword = request.POST.get('keyword')

    data = []
    try:
        electeur = Fichier.objects.get(numero_electeur=keyword)
        electeurs = Fichier.objects.filter(numero_electeur=electeur)
        print("electeur ", electeurs)
        data = serializers.serialize('json', [electeurs])

        print("data , data", data)

    except Exception as e:
        print(e)

    return JsonResponse(data,safe=False)

def get_person_info(request):
    person_id = request.GET.get('person_id')
    data = []
    try:
        electeur = Fichier.objects.get(pk=person_id)
        data = serializers.serialize('json', [electeur])
        print("data", data)
    except Exception as e:
        print(e)

    return JsonResponse(data,safe=False)

def create_person(request):
    values = {'error':'','has_error':0,}
    values['numero_electeur'] = request.POST.get('numero_electeur')
    values['numero_identification'] = request.POST.get('numero_identification')
    values['nom'] = request.POST.get('nom')
    values['prenom'] = request.POST.get('prenom')
    values['commune'] = request.POST.get('commune')
    values['departement'] = request.POST.get('departement')
    values['region'] = request.POST.get('region')

    try:
            #if len(values['first_name']) > 0 and len(values['last_name']) > 0  and len(values['phone']) > 0 and len(values['email']) > 0 and len(values['address']) > 0:

            electeur = Parraine.objects.create(
                nom=values['nom'],
                prenom=values['prenom'],
                numero_electeur=values['numero_electeur'],
                numero_identification=values['numero_identification'],
                commune=values['commune'],
                departement=values['departement'],
                region=values['region'],
                )
            electeur.save()
            #return redirect('/all_clients/')
            #values['clientId'] = client.id
            return JsonResponse(values)
            #else:
            #    values['error'] =  "Veuillez remplir tous les champs"
            #    values['has_error'] =  -1

    except Exception as e:
        values['error'] =  e
        values['has_error'] =  -1

        print("erreur ", e)

    return JsonResponse(values)