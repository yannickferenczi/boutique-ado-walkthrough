from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NpRidGyVUvHk4DbDqxi9Qtg2fJNJoJe6XRo6xLTwmEdVsFJC6Ahu9IXQjKfxMjohpznrUpl1YlhVXFgQMHEeC8C00gtaUnvT8',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
