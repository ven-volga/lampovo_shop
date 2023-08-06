from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from authentication.forms import LoginForm, RegisterForm
from django.views.generic import TemplateView


def login_user(request):
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_page')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'The user with name "{username}" was not found or password incorrect!',
                }
        else:
            context = {
                'login_form': login_form,
            }
    return render(request, 'auth/login.html', context)


class RegisterUser(TemplateView):
    template_name = 'auth/register.html'

    def get(self, request):
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'auth/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('main_page')

        context = {'register_form': register_form}
        return render(request, 'auth/register.html', context)



def user_page(request):
    return render(request, 'auth/user.html')


def logout_user(request):
    logout(request)
    return redirect('main_page')
