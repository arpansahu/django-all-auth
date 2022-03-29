from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from djangoProjectAllAuth.forms import AccountUpdateForm


@method_decorator(login_required(redirect_field_name=''), name='dispatch')
class HomeClassView(View):
    def get(self, request):
        return render(request, 'Home.html')


def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context['account_form'] = form
    return render(request, 'account/account.html', context)
