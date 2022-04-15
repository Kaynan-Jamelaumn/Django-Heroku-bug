from .cart import Cart


def cart(request):
    # vai retonar os dados default de quando é inicializado __init__ os dados do Cart
    return {'cart': Cart(request)}
