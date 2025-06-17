from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('home')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })

    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'store/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order

@login_required
def checkout(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        product = get_object_or_404(Product, id=product_id)

        order = Order(
            user=request.user,
            product=product,
            quantity=quantity,
            address=address,
            phone=phone,
        )
        order.save()

        messages.success(request, 'Order placed successfully!')
        return redirect('home')

    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/checkout.html', {'product': product})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'store/order_history.html', {'orders': orders})

from django.shortcuts import render

def shop(request):
    return render(request, 'store/shop.html')
def about(request):
    return render(request, 'store/about.html')
def contact(request):
    return render(request, 'store/contact.html')
# store/views.py
def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })

    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

