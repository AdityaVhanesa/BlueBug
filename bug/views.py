from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import RaiseBugForm, NewCommentForm
from .models import Bugs, Posts


class Index(View):
    def get(self, request):
        return render(request, 'bug_templates/bug_index.html', context={"bugs": Bugs.objects.all()})


class RaiseBug(View):
    def get(self, request):
        return render(request, 'bug_templates/bug_create.html', {"form": RaiseBugForm()})

    def post(self, request):
        form = RaiseBugForm(request.POST)
        if form.is_valid():
            bug_title = form.cleaned_data.get("bug_title")
            bug_description = form.cleaned_data.get("bug_description")
            bug_foundIn = form.cleaned_data.get("bug_foundIn")
            bug_severityLevel = form.cleaned_data.get("bug_severityLevel")

            Bugs(title=bug_title,
                 description=bug_description,
                 found_in=bug_foundIn,
                 severity_level=bug_severityLevel,
                 raised_by=User.objects.get(id=request.user.id)).save()

        return redirect('index')


class RemoveBugView(View):
    def get(self, request, **kwargs):
        Bugs.objects.filter(id=kwargs['bugID']).delete()
        return redirect('index')


class EditBugView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bug = None

    def get(self, request, **kwargs):
        self.bug = Bugs.objects.get(id=kwargs['bugID'])
        return render(request, "bug_templates/bug_edit.html", context={"bug": self.bug})

    def post(self, request, **kwargs):
        self.bug = Bugs.objects.get(id=kwargs['bugID'])
        form = RaiseBugForm(request.POST)
        if form.is_valid():
            self.bug.title = form.cleaned_data.get("bug_title")
            self.bug.description = form.cleaned_data.get("bug_description")
            self.bug.found_in = form.cleaned_data.get("bug_foundIn")
            self.bug.severity_level = form.cleaned_data.get("bug_severityLevel")
            self.bug.save()
        return redirect("bug_index")


class CloseBugView(View):
    def get(self, request, **kwargs):
        bug = Bugs.objects.get(id=kwargs["bugID"])
        bug.status = "Closed"
        bug.save()
        return redirect("bug_index")


class ReOpenBugView(View):
    def get(self, request, **kwargs):
        bug = Bugs.objects.get(id=kwargs["bugID"])
        bug.status = "Re-Opened"
        bug.save()
        return redirect("bug_index")


class CommentBugView(View):
    def get(self, request, **kwargs):

        posts = Posts.objects.filter(bug_id=kwargs["bugID"])
        print(posts)
        return render(request, "bug_templates/bug_comment.html",
                      context={
                          "posts": posts,
                          "bug": Bugs.objects.get(id=kwargs["bugID"])
                      })

    def post(self, request, **kwargs):
        form = NewCommentForm(request.POST)
        print(form.data)
        if form.is_valid():
            Posts(comment=form.cleaned_data.get("comment"),
                  user=User.objects.get(id=request.user.id),
                  bug=Bugs.objects.get(id=kwargs["bugID"])).save()

        return redirect(f"/bug/comment/{kwargs['bugID']}")


# Create your views here.
def redirectToBug(request):
    return redirect('/bug')
