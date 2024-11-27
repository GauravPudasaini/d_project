from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_dashboard(request):
    """
    User-specific dashboard view.
    """
    context = {
        'username': request.user.username,
        'email': request.user.email,
    }
    return render(request, 'users/dashboard.html', context)