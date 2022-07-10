from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import RaiseBugForm
from .models import Bugs


class Index(View):
    def get(self, request):
        return render(request, 'templates_Bugs/index.html')


class RaiseBug(View):
    def get(self, request):
        return render(request, 'templates_Bugs/create_bug.html', {"form": RaiseBugForm()})

    def post(self, request):
        form = RaiseBugForm(request.POST)

        if form.is_valid():
            user_Object = form.cleaned_data.get('user_name')
            if not user_Object:
                return redirect('index')

            bug_title = form.cleaned_data.get("bug_title")
            bug_description = form.cleaned_data.get("bug_description")
            Bugs(title=bug_title,
                 description=bug_description,
                 raised_by=user_Object).save()

        return redirect('index')


class RemoveBugView(View):
    def get(self, request, **kwargs):
        Bugs.objects.filter(uuid=kwargs['bugID']).delete()
        return redirect('index')


# Create your views here.
def redirectToBug(request):
    return redirect('/bug')
