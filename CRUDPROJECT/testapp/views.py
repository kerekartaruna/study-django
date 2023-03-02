from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView
from .forms import ClientRegistration
from .models import Client
from django.views import View
# Create your views here.

#class for add and show
class ClientAddShow(TemplateView):
    template_name = 'testapp/addshow.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = ClientRegistration()
        a = Client.objects.all()
        context = {'a':a, 'form':fm}
        return context
    def post(self, request):
        fm = ClientRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['Name']
            em = fm.cleaned_data['Email']
            lm = fm.cleaned_data['Location']
            reg = Client(Name=nm, Email=em, Location=lm)
            reg.save()
            return HttpResponseRedirect('/')

# this class will update data
class update_data(View):
    def get(self, request,id):
         pi = Client.objects.get(pk=id)
         fm = ClientRegistration(instance=pi)
         return render(request,'testapp/update.html', {'form':fm})

    def post(self, request, id):
        pi=Client.objects.get(pk=id)
        fm = ClientRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request,'testapp/update.html', {'form':fm})





# this class will delete data

class delete_data(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        #kwargs is one dictionary and id is the primary key
        del_id = kwargs['id']
        Client.objects.get(pk=del_id).delete()

        return super().get_redirect_url(*args, **kwargs)
