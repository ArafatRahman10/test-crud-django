from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from listings.models import Band
from listings.forms import ContactUsForm, BandForm
from django.shortcuts import render
from django.core.mail import send_mail

def contact(request):
   if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
    form = ContactUsForm(request.POST)

    if form.is_valid():
        send_mail(
            subject=f'Message de {form.cleaned_data["nom"] or "anonyme"} via Merchex Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
          # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
          # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
       
        #return redirect('email-envoye')
    else:
         form = ContactUsForm()

    return render(request,
        'listings/contact.html',
        {'form': form})    


def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return HttpResponseRedirect(reverse('band-list'))
    
    return render(request,
        'listings/band_delete.html',
        {'band': band})


def band_list(request):
    bands = Band.objects.all()
    return render(request,'listings/band_list.html',
        {"bands" : bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html',
        {'band': band})         



def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm(instance=band)
    return render(request,
        'listings/band_update.html',
        {'form' : form})



def about(request):
    return render(request,'listings/about.html')  

def listings(request):
    return render(request,'listings/listings.html') 

 
