
class main:

    shop= shop = {
    "book": [
        {"product": "harry potter", "price": 1234},
        {"product": "robinson crusoe", "price": 2444},
        {"product": "mathi", "price": 4893}
        
    ],
    "fish": [
        {"product": "mathi", "price": 4893},
        {"product": "sardine", "price": 3200}
        
    ],
    "electronics": [
        {"product": "mobile phone", "price": 15000},
        {"product": "laptop", "price": 55000}
    ],
    "clothing": [
        {"product": "t-shirt", "price": 800},
        {"product": "jeans", "price": 2200},
        
    ],
    "grocery": [
        {"product": "rice", "price": 100},
        {"product": "milk", "price": 50},

    ]
}


    cart ={"book":[{"product" :"harry potter" ,"price": 1234},{"product": "robinson crusoe" , "price" : 2444}],"fish":[{"product":"mathi","price":4893}]}

    def __init__(self,product,category,price):

        self.product = product
        self.category = category
        self.price = price
       


class item(main):   #main class

    def __init__(self,product=None,category=None,price=None):
        
        super().__init__(product,category,price)



    def add_item(self):   # adding items


        if self.category in self.shop:

            self.shop[self.category].append({"product" : self.product, "price" : self.price})

            print(f"{self.product} added price {self.price}")

        else:

            print("enter a valid category")
            

    def remove_item(self, category):   # remove items

        found = False

        for item1 in self.shop[category]:

            if item1["product"] == self.product:

                removed_price = item1["price"]  

                self.shop[category].remove(item1)

                print(f"Removed item {self.product} of price {removed_price} from category {category}")

                found = True

                break

        if not found:

            print(f"There is no such product as {self.product} in the category {category}")


    def view_items(self,category):  #view items in the category

        if category in self.shop:

            for product in self.shop[category]:

                print(f"Product: {product['product']}  Price: {product['price']}  Category: {category}")

        else:

            print("enter a valid category")
    
    def view_item(self,product_name):   # view a specific item

        count = False

        for  category,products in self.shop.items():

            for product in products:

                if product["product"] == product_name:
                    
                    print(f"Product: {product['product']}  Price: {product['price']}  Category: {category}")

                    count =True

        if not count:

            print("There is no product in the shop")
                
            



    def view_all_items(self):   #view all the items in the shop

        print("------------- E KART-------------\n")

        for products in self.shop.values():

            for item in products:

                print(f"{item['product']}  Price: {item['price']}")



class category1(item):

    def add_category(self):    # to add a category to shop
     
        if self.category not in self.shop:

            self.shop[self.category] = [{"product" : self.product , "price" : self.price}]

            print(f"category {self.category} is added to shop with item {self.product} of price {self.price}")
    
        else:

            self.shop[self.category].append({"product": self.product, "price": self.price})

            print(f" Category {self.category} already exists. Added product {self.product} of price {self.price} to it.")


        
    def remove_category(self,category):  # remove a category from shop

        if category in self.shop:

            print("are you sure you want to delete this category \n all the items within it will be deleted \n enter yes or no")
            
            op= input()

            if op == "yes":
                
                del self.shop[category]

                print(f" {category} deleted")

            elif op == "no":

                s1.view_shop()

        else:

            print("there is no such category \n please enter a existing category")
            

    def category_view(self):   # view all categories in the shop
        
        print("------------- ALL CATEGORIES IN SHOP -------------\n")
        
        for category1 in self.shop:

            print(category1)

    

class cart1(category1):

    def add_itemcart(self,quantity=1):   # ad item to cart

        if self.category in self.cart:

            self.cart[self.category].append({"product": self.product, "price": self.price, "quantity": quantity})
            s1.view_cart()

        else:

            print("enter a valid category")

    def view_cart(self):   # view all the items in the cart

        print("------------- ALL PRODUCTS IN CART -------------\n")  



        for products in self.cart.values():

            for item in products:

                q = item.get('quantity', 1) 

                print(f"Product: {item['product']}  Price: {item['price']}  Quantity: {q}")


    def removecart(self,category):

        found = False

        for item1 in self.cart[category]:

            if item1["product"] == self.product:

                removed_price = item1["price"]

                self.cart[category].remove(item1)

                print(f" Removed item '{self.product}' of price {removed_price} from category {category}")

                found = True

                break

        if not found:
            
            print(f"There is no such product '{self.product}' in the category '{category}'")


    def buy_item(self,category):

        found = False

        for item1 in self.cart[category]:

            if item1["product"] == self.product:

                quantity = item1.get('quantity', 1) 

                total_price = item1["price"] * quantity

                print(f"Purchased '{item1['product']}' x {quantity} for ₹{total_price}")

                self.cart[category].remove(item1)

                found = True

                break

        if not found:
            
            print(f"There is no such product '{self.product}' in the category '{category}'")


class shop1(cart1):
        

    def view_op(self):
        
        s1.view_all_items()
        
        print("what are you looking for")

        s1.view_shop()

    def view_shop(self):

        print("select the options \n 1.add \n 2.view  \n 3.delete \n 4.buy ")

        op = int(input())
        if op  == 1:

            self.add()

        elif op == 2:

            self.view()

        elif op == 3:

            self.remove()

        elif op == 4:

            self.buy()
    

    def add(self):

        while True:

            print("1. add category \n 2.add product \n 3.add item to cart \n 4.exit")

            op = int(input())

            if op == 1:

                category = input("enter a category")

                no = int(input("enter no of items you want to add"))

                for i in range(no):

                    product = input("enter the product")

                    price = int(input("enter the price"))
                
                    s1 = shop1(product,category,price)

                    s1.add_category()

                s1.category_view()

                s1.view_shop()
            
            elif op == 2:

                self.category_view()

                print("enter the category in which you want to add product")

                category = input()

                product = input("enter the product")

                price = int(input("enter the price"))
                
                s1 = shop1(product,category,price)

                s1.add_item()

                s1.view_shop()

            elif op == 3:

                category = input("enter a category")

                no = int(input("enter no of items you want to add"))

                for i in range(no):

                    product = input("enter the product")

                    price = int(input("enter the price"))
                
                    quantity = int(input("enter the quantity"))   # <-- ask for quantity
    
                    s1 = shop1(product, category, price)
                    
                    s1.add_itemcart(quantity)    


                s1.view_shop()

            else:

                self.view_shop()

    def remove(self):
        
        while True:
        
            op = int(input("1. Delete category \n 2.product delete \n 3.remove from cart \n 4.exit"))

            if op == 1:

                self.category_view()

                print("enter the category you want to delete")
                
                category = input()

                self.remove_category(category)

                self.view_shop()
        

            elif op == 2:

                print("enter the product you want to delete")

                product = input()

                product_name = product

                self.view_item(product_name)

                print("enter the category")

                category = input()

                s1 = shop1(product,category)

                s1.remove_item(category)

                s1.view_shop()

            elif op == 3:

                self.view_cart()
            
                print("enter the item to be removed")

                product = input()

                print("enter the category")

                category= input()

                s1 = shop1(product,category)

                s1.removecart(category)

                s1.view_shop()
            else:

                self.view_shop()


        
    def view(self):

        while True:
            op = int(input(" 1.view all categories \n 2.view product \n 3.view cart \n 4.exit"))

            
            if op == 1:

                s1.category_view()

                print("enter the category you want to view OR enter 1 to exit")   


                op = input()

                if op == "1":

                    self.view_shop()       

                else:        
                    category = op

                    self.view_items(category)

                    s1.view_shop()

            if op == 2:
                
                product_name= input(" enter the product you want to search")

                self.view_item(product_name)

                s1.view_shop()

            elif op == 3:

                s1.view_cart()
                print("press 1 to buy or press 2 to exit")

                op = int(input())
                if op == 1:
                    s1.buy()
                else:
                    s1.view_shop()
            
            else:
                
                s1.view_shop()

    def buy(self):

        self.view_cart()

        print("enter the product you want to buy")

        self.product = input()

        print("enter the category")

        category = input()

        self.buy_item(category)

    
        

s1 = shop1()
s1.view_op()


