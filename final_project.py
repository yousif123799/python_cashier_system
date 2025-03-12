from json import dumps,loads
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def to_dict(self):
        return {'name':self.name,'price':self.price}
def total_price(products):
    total=0.0
    for product in products:
        total+=product.price
        return f"the total price is : {total}"
def add_product(name,price):
    new_product=Product(name, price)
    products.append(new_product)
def show_produts(products):
    for i in products:
        print(f"the product name is : {i.name}, and the price is : {i.price}.")
def load_products():
           try: 
                product_file=open("product.json","r+")
           except IOError:
                return []
           product_json=product_file.read()
           product_data=loads(product_json)
           products=[]
           for product in product_data:
                products.append(Product(product['name'], product['price']))
                product_file.close()
                return products
def save_products(products):
    save_products=[]
    for product in products:
        save_products.append(product.to_dict())
    products_file=open("products.json","w+")
    products_file.write(dumps(save_products))
    products_file.close()
products=load_products()
while True:
    print(50*"*")
    print("type 'add' to add the product ")
    print("type 'quit' to exit from the program ")
    print("type 'show' to show and list the product : ")
    command=input("type the command : ")
    if(command=='quit'):
        save_products(products)
        break
    elif(command=='add'):
        product_name=input("please, enter the product name : ")
        try:
            product_price=float(input("please, enter the product price : "))
        except ValueError:
            print("please,enter a valid number!")
            continue
        add_product(product_name, product_price)
    elif(command=='show'):
        show_produts(products)
    elif (command=='total'):
        total_price(products)
    else:
        print("that is invaild command, please try again.")