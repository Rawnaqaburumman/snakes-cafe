def show_message():
 print(menues )

 
menues = """

**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""" 

def take_order():
 orders =["Wings","Cookies","Spring Rolls","Entrees" , "Ice Cream", "Cake","Pie" , "Drinks" ,"Coffee" ,"Tea","Unicorn Tears","Salmon", "Steak","Meat Tornado","A Literal Garden","Desserts"]   
 ordersIndex=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 order = input(">>>>>>>>")

 while  (order != "quit" ):
  num = orders.index(order)
  ordersIndex[num] =  ordersIndex[num] + 1 ;
 ## print(num)
 ## print(ordersIndex)
  print(f"** {ordersIndex[num]} Order of {order} have been added to your meal **")
  order = input(">>>>>>>>>")

if __name__=="__main__":
 
 show_message()
 take_order()
  