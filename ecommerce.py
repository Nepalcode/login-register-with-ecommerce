import json
import datetime
user_choice = input('Do you want to register/login? ').lower()

if user_choice == 'register':
    user_username = input('Enter your username: ')
    user_password = input('Enter your password: ')

    user_data = {'username':user_username,'password':user_password}

    json_user_data = json.dumps(user_data)

    f = open('login_data.txt','a')

    f.write(json_user_data+'-')

    f.close()
elif user_choice == 'login':
    user_username = input('Enter your username: ')
    user_password = input('Enter your password: ')

    f = open('login_data.txt','r')

    user_data = f.read()

    f.close()

    user_data_list = user_data.split('-')
    user_data_list_len = len(user_data_list)
    count = 0

    for i in user_data_list:
        if i != "":
            user_data_dict = json.loads(i)
            if user_username == user_data_dict.get('username') and user_password == user_data_dict.get('password'):
                print('Login succesfull!')
                #ecommerce
                class Buyer:  
    
                    def view_all_product(self):    
                        f = open("data_store.txt","r")                       
                        user_value = f.read()
                        f.close()

                        user_value_a = user_value.split("-")  

                        for i in user_value_a:
                            if i.strip():
                                json_user_value = json.loads(i)                    
                                product_name = json_user_value.get("product_name")
                                product_quantity = json_user_value.get("product_quantity")
                                product_price = json_user_value.get("product_price")
                                product_manufacture = json_user_value.get("product_manufacture")               

                                print(f"Product_name:{product_name}\t product_quantity:{product_quantity}\t product_price:{product_price}\t product_manufacture:{product_manufacture}\n" )            
                            
                    
                   
                    def purchase_product(self,product_name,quantity): 
                        self.product_name = product_name
                        self.quantity = int(quantity)
                        
                        #removing product after purchasing
                        f = open("data_store.txt","r")                      
                        file_user_value = f.read()
                        f.close()

                        user_value_a = file_user_value.split("-") 
                        text = "overwrite"
                        
                        for i in user_value_a:
                            if i !="":

                                json_user_value = json.loads(i)                   
                                file_product_name = json_user_value.get("product_name")
                                file_product_quantity = int(json_user_value.get("product_quantity"))
                                file_product_price = json_user_value.get("product_price")
                                file_product_manufacture = json_user_value.get("product_manufacture")

                                if  file_product_name == self.product_name:
                                    
                                    if self.quantity < file_product_quantity: 

                                        update_product_quantity = file_product_quantity - self.quantity 
                                        text = f'{{"product_name": "{file_product_name}", "product_quantity": "{file_product_quantity}", "product_price": "{file_product_price}", "product_manufacture": "{file_product_manufacture}"}}'
                                        new_text = f'{{"product_name": "{file_product_name}", "product_quantity": "{update_product_quantity}", "product_price": "{file_product_price}", "product_manufacture": "{file_product_manufacture}"}}'
                                    
                                        #decrese the number of quantiy
                                        
                                        f = open("data_store.txt","w")
                                        f.write(file_user_value.replace(text, new_text))
                                        f.close() 
                                        break

                                    elif self.quantity == file_product_quantity:
                                        text = f'{{"product_name": "{file_product_name}", "product_quantity": "{file_product_quantity}", "product_price": "{file_product_price}", "product_manufacture": "{file_product_manufacture}"}}'
                                        f = open("data_store.txt","w")
                                        f.write(file_user_value.replace(text + "-", ""))
                                        f.close() 
                                        break 

                                    elif self.quantity > file_product_quantity:
                                        print("NOt available much product")
                                        break
                                        
                    
                    def viewbills(self,quantity,product_name):
                        
                        self.quantity = quantity
                        self.product_name = product_name
                        product_found = False

                        f = open("data_store.txt","r")                      
                        file_user_value = f.read()
                        f.close()

                        user_value_a = file_user_value.split("-") 
                        
                        for i in user_value_a:
                            if i.strip():                
                                json_user_value = json.loads(i)                   
                                file_product_name = json_user_value.get("product_name")                
                                price = json_user_value.get("product_price")

                                if  self.product_name == file_product_name:                     
                                    product_found = True
                                    print("\n")      
                                    print("                                                    YOUR BILL                ")
                                                    
                                    total_cost = int(self.quantity)* int(price)
                                    desc = datetime.datetime.now()
                                    day_desc = desc.strftime("%y-%m-%d")
                                    time_desc = desc.strftime("%H:%M")
                                    
                                    print(f"                           Date:20{day_desc}")
                                    print(f"                           Time:{time_desc}")
                                    print(f"                           Product Name:{self.product_name}")
                                    print(f"                           Quantity:{self.quantity}")
                                    print(f"                           Total Cost:{total_cost}")
                                
                        if not product_found:
                            print("Product is not available")



                class Seller:  
                    
                    def add_product(self): 
                        f = open("data_store.txt","a+")
                        product_name = input("Enter product_name:")
                        product_quantity = input("Enter product_quantity:")
                        product_price = input("Enter product_price:")
                        product_manufacture = input("Enter product_manufacture:")
                    
                        
                        list_product = {"product_name":product_name,"product_quantity":product_quantity,"product_price":product_price,"product_manufacture":product_manufacture}
                        
                        json_list_product = json.dumps(list_product)            
                        f.write(json_list_product+"-")            
                        f.close()     

                    def view_all_product(self):
                        f = open("data_store.txt","r")                       
                        user_value = f.read()
                        f.close()
                        user_value_a = user_value.split("-")    

                        for i in user_value_a:
                            if i.strip():
                                json_user_value = json.loads(i)                    
                                product_name = json_user_value.get("product_name")
                                product_quantity = json_user_value.get("product_quantity")
                                product_price = json_user_value.get("product_price")
                                product_manufacture = json_user_value.get("product_manufacture")               

                                print(f"Product_name:{product_name} \t product_quantity:{product_quantity} \t product_price:{product_price} \t product_manufacture:{product_manufacture}\n" )            
                            
                

                user_choice = input("Enter a buy for Buyer and sell for seller:").lower()

                if user_choice == "buyer":
                
                    buyer1 = Buyer()    
                    count_buy = 1
                    while True:
                        count_buy +=1
                        user_input = input("Enter 1 (for View all prducts) 2(for purchase product):")
                        if user_input == "1":
                            buyer1.view_all_product()
                            break
                        elif user_input == "2":            
                            product_name = input("Enter the prduct name:")
                            quantity = input("Enter the Product Quantity:")           
                            buyer1.purchase_product(product_name,quantity)            
                            buyer1.viewbills(quantity,product_name)            
                            break
                        elif count_buy == 3:
                            break            
                        else:
                            pass
                            

                elif user_choice == "seller":
                    
                    seller1 = Seller()   
                    count = 1
                    while True:
                        user_input = input("Write 1(for add_product) 2 (for view view_all_product):")
                            
                        if user_input == "1":
                            seller1.add_product()
                            break
                        
                        elif user_input == "2":
                            seller1.view_all_product()
                            break
                        elif count == 3:
                            break    
                        else:
                            pass
                            count+=1
                        
                        
                else:
                    print("Plz enter one of them (buyer and seller)")  
    
    
            else:
                count += 1

    if count == user_data_list_len:
        print('Invalid credentials!') 