from typing import Any
from django.shortcuts import render
from django.conf import settings
import stripe
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Create your views here.


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
        line_items=[{
        'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': 'T-shirt',
            },
            'unit_amount': 2000,
        },
        'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/orders/charge'
  )

    return render(request, 'orders/charge.html')
