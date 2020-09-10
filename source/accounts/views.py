from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import CreateView, View
from django.conf import settings

from accounts.forms import MyUserCreationForm
from .models import AuthToken


# def login_view(request):
#     context = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             context['has_error'] = True
#     return render(request, 'registration/login.html', context=context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('index')


class RegisterView(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        if settings.ACTIVATE_USERS_EMAIL:
            return redirect('index')
        else:
            login(self.request, user)
            return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('index_project')
        return next_url


class RegisterActivateView(View):
    def get(self, request, *args, **kwargs):
        token = AuthToken.get_token(self.kwargs.get('token'))
        if token:
            if token.is_alive():
                user = token.user
                user.is_active = True
                user.save()
                login(request, user)
            token.delete()
        return redirect('index_project')
