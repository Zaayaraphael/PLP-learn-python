# define function

def calculate_discount(price, discount_percent):
  
  # if loop
  
    if discount_percent >= 20:
# calculate discount 
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
        
# else loop
    else:
        return price
        
# form to enter value with decimal places.
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# final result
final_price = calculate_discount(price, discount_percent)

print("The final price is:", final_price)