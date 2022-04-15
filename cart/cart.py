from decimal import Decimal

from django.shortcuts import get_object_or_404
from store.settings import base
from product.models import Variation


class Cart():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session  # pega as sessões
        # pega a sessão da chave "cart"
        cart = self.session.get(base.CART_SESSION_ID)
        # se não tiver a sessão com a chave "cart" então ela é criada
        if base.CART_SESSION_ID not in request.session:
            cart = self.session[base.CART_SESSION_ID] = {}
        self.cart = cart  # self.cart recebe a sessão já existente, ou que já foi criada

    def add(self, variation, quantity):
        """
        Adding and updating the users cart session data
        """
        variation_id = str(
            variation.id)  # pega o objeto variation que foi criado em view.py.CartAdd
        # e pega o id do objeto variation

        if variation_id in self.cart:  # se a variation_id que veio do ajax estiver
            # já na nossa sessão com chave "cart"
            # ele só passa dentro do dicionário onde tem a variation_id específico,
            #  pega o campo quantity e atualiza a quantidade que foi passada
            self.cart[variation_id]['quantity'] = quantity

        else:

            variation_product = get_object_or_404(
                Variation, id=variation_id)  # pega o produto(variação)
            # que já existe na tabela Variation onde o id desse produto é igual ao que
            #  foi passado pelo ajax
            if not variation_product.promotion_price:  # se não tiver um preço de promoção
                price = variation_product.price  # ele pega o preço normal

            else:
                price = variation_product.promotion_price  # senão, se tiver um preço
               # de promoção, ele pega esse preço de promoção
            """
            if Variation.id == variation_id:
                print("frjgfrepfr", variation_id)
                if not Variation.promotion_price:
                    price = Variation.price
                else:
                    price = Variation.promotion_price
            """
            self.cart[variation_id] = {  # a sessão do carrinho cria a chave com o id da variação
                # e nessa variação o valor dessa chave é um dicionário que vai conter
                #  a chave price que vai conter de valor o preço da variação produto
                #  que veio da variação que continha na variação que foi encontrado
                # dentro do objeto variações que sucedeu o que estava no banco de dados
                #  na tabela Variation
                # e depois cria outra chave com nome quantity, onde o valor é
                #  a quantidade que foi fornecidade pelo o cliente no ajax
                'price': str(price), 'quantity': quantity}

        self.save()  # chama a função self.save

    def __iter__(self):  # como o nome diz é um método mágico chamado iter onde sua função é de um iterator(iterar) sobre algo
        # ele vai pegar a sessãoo cart(carrinho) que é um dicionário e vai pegar todas as chaves dele
        product_ids = self.cart.keys()
        variations = Variation.availableVariation.filter(id__in=product_ids)
        # pega todos as variações que estão  disponíveis na tabela Variation filtrando
        #  também pela as chaves da sessão de self.cart que deveria conter o variation_id (ou algo do tipo)

        #products = get_object_or_404(Variation, id__in=product_ids)
        cart = self.cart.copy()  # copia todo o dicionário de sessão do self.cart

        for variation in variations:  # pra cada produto dos produtos filtrados de Variation
            cart[str(variation.id)]['variationproduct'] = variation
            # vai passar o id da variação que está sendo iterado de variation e passar na sessão esse
            #  id da variação como valor vai passar o objeto dessa variação(todos os campos da tabela)
            stock = []  # BUG checar finalização do projeto se tem de excluir essa parte do código ou se eu tenho que excluir a função listfy_stock
            # cria uma lista pra cada laço do for
            x = 0  # reseta o contador
            # pega o número atual de estoques que estão no produto(product)((que na verdade é a variação))
            while x <= variation.stock:
                # eu tenho que fazer esse loop ao invés de

                # simplesmente passar o estoque de uma vez
                # pois no success do ajax eu quero criar um select e cada option vai ter de
                #  0 até o número atual de produtos no estoque
                # por isso desse loop
                stock.append(x)
                x = x+1
            # nessa sessão de chave desse produto id crio um novo value, onde passo essa lista
            cart[str(variation.id)]['variationstock'] = stock

        for item in cart.values():  # pra cada value dessa sessão
            # que no caso se comportaria como outro dicionário de chave price vai
            # passar de value o preço Decimal do próprio preco
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            # pega o value total_price que na verdade é outro dicionário e vai adicionar
            #  o preço do item vezes a quantidade de cada item igual adicionado
            yield item

    def __len__(self):
        """
        pega os dado do cart(que seria a sessão) e conta a quantidade de itens

        """
        return sum(item['quantity'] for item in self.cart.values())

    # função de uptade pega a variation id  e quantity de um dos values(que na verdade é um dicionário que tem outras chaves e values)
    def update(self, variation, quantity):
        """

        """
        variation_id = str(variation)
        if variation_id in self.cart:  # se a variação existir na sessão
            # ele pega a chave dessa sessão como
            self.cart[variation_id]['quantity'] = quantity
            # o variation_id pega o value que seria outro dicionário que tem a chave quantity e
            # atualiza a quantidade
        self.save()  # chama a função save

    def variation_price(self, variation, quantity):
        variation_filtered = get_object_or_404(Variation, id=variation)
        if variation_filtered.promotion_price:
            return variation_filtered.promotion_price * quantity
        else:
            return variation_filtered.price * quantity

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        # pro item price(item preço) recebe vezes a quantidade de cada item que está dentro dos values do carrinho(cart)

    def delete(self, variation):
        """
       só deleta de dentro da sessão o item desejado
        """
        variation_id = str(variation)

        if variation_id in self.cart:  # se existir a variação dentro da sessão
            del self.cart[variation_id]  # exclui da sessão o produto
            self.save()  # chama a função save

    def listfy_stock(self, variation):
        variation = get_object_or_404(Variation, id=variation)

        stocknumbers = []

        x = 0
        stock = variation.stock  # do objeto de variações  pega o stock
        while x < stock:
            # vai adicionar de 0 até o número atual de itens no stock
            stocknumbers.append(x)

            x = x+1
        # manda a lista stocknumbers #BUG possivelmente excluir essa função
        self.listfy_value(stocknumbers)
        return stocknumbers

    def listfy_value(self, stocknumbers):
        return stocknumbers

    def clear(self):
        # Remove basket from session
        del self.session[base.CART_SESSION_ID]  # deleta a sessão
        self.save()  # chama a função save

    def save(self):
        self.session.modified = True  # salva a sessão quando for modificada

    def payment_stock_update(self):
        cart = self.cart
        for item in cart:

            variation_stock = get_object_or_404(
                Variation, id=item)
            stock = variation_stock.stock

            """
            Outra forma de pegar itens do carrinho

                    #carrinho = cart.values()
                    carrinho = cart.get(item)
                    carrinho = carrinho.get('quantity')
            """
            quantity = cart[item]['quantity']
            if stock >= quantity:

                newstock = stock - quantity
            else:
                newstock = stock
            Variation.objects.filter(
                id=variation_stock.id).update(stock=newstock)


"""
    def stock_update(self):

        for item in self.cart:
            stock_variation_id = item.keys()
            variation_stock = get_object_or_404(
                Variation, id=stock_variation_id)
            stock = variation_stock.stock
            stock = stock - int(item['quantity'])
            variation_stock.objects.update(stock=stock)

    LISTY STOCK VERSION WITH ALL VARIATIONS
        def listfy_stock(self, variation):
        variation = Variation.available.filter(id__in=variation)
        stocknumbers = []
        stock = []
        id = []
        matrix = []
        for x in variation.stock:
            stocknumbers.append(x)
            x = x+1
        stock.append(stocknumbers)
        id.append(self.id)
        matrix.append(id)
        matrix.append(stock)

        variationid = variation.id
        for i in matrix[0]:
            i = i+1
            print(matrix[0])
            print(matrix[0][i])
            if variationid == matrix[0][i]:
                print('funcionou', matrix[0][i])
                receivematrix = matrix[1][variationid]
                print('recebeu', receivematrix)
                return receivematrix

    def listfy_value(self, receivematrix):
        return receivematrix
    
    
    """
