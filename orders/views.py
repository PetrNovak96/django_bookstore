import stripe
from django.views.generic.base import TemplateView
from django.contrib.auth.models import Permission # new
from django.conf import settings # new
from django.shortcuts import render # new

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY # new

class OrdersPageView(TemplateView):

    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request): # new

    # tady se děje to, co za to dostane
    permission = Permission.objects.get(codename='special_status') # get permission
    u = request.user # get user
    u.user_permissions.add(permission) # pridat permission

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')