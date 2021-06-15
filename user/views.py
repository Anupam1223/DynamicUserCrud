from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import User
from django.http.response import HttpResponse

# Create your views here.
class UserAdd(TemplateView):
    template_name = "useradd.html"

    def post(self, request):
        user = User()
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.address = request.POST.get("address")
        user.password = request.POST.get("password")
        user.image = request.POST.get("image")
        user.save()

        return HttpResponse("thank you for your Registration")


class UserView(TemplateView):
    template_name = "userread.html"

    def get(self, request):

        user = User.objects.all()
        return render(request, self.template_name, {"user": user})
