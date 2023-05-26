def you_pay(cost, is_monday):
    if cost <= 50:
        discount= cost*0.1
    elif cost >50 and cost <=100:
        if(is_monday):
            cost-=10
            discount =cost* 0.2
          
        else:
            discount =cost*0.2
    else:
        if(is_monday):
            cost-=10
            discount =cost*0.4
         
        else:
            discount =cost*0.4

    return cost-discount
    
print(you_pay(50,True))
"""" You are a loyal customer, and a store is offering discounts to their loyal customers:

For a purchase between 0 & 50 CAD, you get a 10 % discount.
For a purchase between 51 & 100 CAD, you get a 20 % discount.
For a purchase of more than 100 CAD, you get a 40 % discount.
On Monday, if you spend more than 50 CAD, you get an additional 10 CAD OFF.
In this task, you need to write a function to calculate how much the customer’s purchase will actually cost after discounts and return that value."""
