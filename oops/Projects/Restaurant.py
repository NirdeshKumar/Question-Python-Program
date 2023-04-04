"""
2. Write a Python class Restaurant with attributes like menu_items,
book_table, and customer_orders, and methods like add_item_to_menu,
book_tables, and customer_order.

Perform the following tasks now:

Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.

Note: Use dictionaries and lists to store the data.

"""

class Restaurant:
    def __init__(self):
        self.__add_item={"Apple": 30,"Mango":25,"Roti":5,"dal":34}

    def menu(self):
        print("*********** WELCOME Buddy **************")
        for i,j in self.__add_item.items():
            print(i,j)

    def add_item_to_menu(self):
        self.key=input("enter a product name: ")
        self.value=input("enter a product price: ")
        self.__add_item[self.key]=self.value
        for i,j in self.__add_item.items():
            print(i,j)
        
    def book_table(self):
        self.name=input("enter a name: ")
        self.total_member=int(input("Total Member: "))
        if(self.name[0].lower()=="a" or self.name[0].lower()=="r" or self.name[0].lower()=="s" or self.name[0].lower()=="n" or self.name[0].lower()=="p"):
            print("Your Table No. is 013")
        elif(self.name[0].lower()=="b" or self.name[0].lower()=="t" or self.name[0].lower()=="m" or self.name[0].lower()=="u" or self.name[0].lower()=="g"):
            print("Your Table No. is 113")
        else:
            print("Your Table No. is 43")
    def customer_order(self):
        self.o={}
        print("Sir, Please order...")
        self.order=input("Sir, Product Name:   ")
        self.amount=int(input("Sir, tell me Quantity: "))
        self.o[self.order]=self.amount
        
        if(self.order in self.__add_item.keys()):
            self.temp2=self.__add_item[self.order]*self.amount
            print("\nYour order Sir.... ")
            for i,j in self.o.items():
                print(i,j)
            print(f"\n\nYour Payment\nProduct Name: {self.order}\nQuantity: {self.amount}\n\nTotal Amount: {self.temp2}")

        else:
            print("Sorry sir...\n this item is not available!!!!")
        
            



















