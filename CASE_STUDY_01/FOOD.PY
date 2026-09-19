# FOOD DELIVERY SYSTEM

order_amount = float(input("Enter order amount: "))
distance = float(input("Enter delivery distance: "))

customer_type = input("Enter customer type (regular/premium/new): ").lower()
customer_rating = float(input("Enter customer rating: "))
restaurant_rating = float(input("Enater restaurant rating: "))
preparation_time = int(input("Enter preparation time: "))

payment_method = input("Enter payment method (upi/card/cash): ").lower()
weather = input("Enter weather (normal/rain/storm): ").lower()
demand = input("Enter demand (low/medium/high): ").lower()
peak_hour = input("Is it peak hour? (yes/no): ").lower()
previous_cancellations = int(input("Enter previous cancellations: "))


# RESTAURANT STATUS

if restaurant_rating >= 4.5:
    restaurant_status = "Excellent"
elif restaurant_rating >= 4:
    restaurant_status = "Good"
elif restaurant_rating >= 3:
    restaurant_status = "Average"
else:
    restaurant_status = "Poor"


# DELIVERY CHARGE

if distance <= 3:
    delivery_charge = 30
elif distance <= 6:
    delivery_charge = 50
elif distance <= 10:
    delivery_charge = 80
else:
    delivery_charge = 120

if weather == "rain":
    delivery_charge = delivery_charge + 20
elif weather == "storm":
    delivery_charge = delivery_charge + 40


# DISCOUNT

discount = 0

if customer_type == "premium":
    if order_amount >= 1000:
        discount = order_amount * 0.20
    elif order_amount >= 500:
        discount = order_amount * 0.15
    else:
        discount = order_amount * 0.10

elif customer_type == "regular":
    if order_amount >= 1000:
        discount = order_amount * 0.10
    elif order_amount >= 500:
        discount = order_amount * 0.05

elif customer_type == "new":
    if order_amount >= 500:
        discount = order_amount * 0.15
    else:
        discount = order_amount * 0.10


# PRIORITY STATUS

priority_status = "Normal"

if customer_type == "premium" and order_amount >= 500:
    priority_status = "Priority"
elif customer_rating >= 4.5 and order_amount >= 1000:
    priority_status = "Priority"
elif demand == "high" and peak_hour == "yes":
    priority_status = "Priority"


# CANCELLATION RISK

if previous_cancellations >= 5:
    cancellation_risk = "High"
elif previous_cancellations >= 2:
    cancellation_risk = "Medium"
else:
    cancellation_risk = "Low"


# MANUAL REVIEW

manual_review = "No"

if customer_rating < 2.5:
    manual_review = "Yes"
elif restaurant_rating < 2.5:
    manual_review = "Yes"
elif previous_cancellations >= 5:
    manual_review = "Yes"
elif weather == "storm" and distance > 10:
    manual_review = "Yes"
elif order_amount >= 3000 and payment_method == "cash":
    manual_review = "Yes"


# ORDER STATUS

if manual_review == "Yes":
    order_status = "Manual Review"
elif restaurant_rating < 3:
    order_status = "Rejected"
elif customer_rating < 2:
    order_status = "Rejected"
elif weather == "storm" and distance > 15:
    order_status = "Rejected"
elif preparation_time > 90:
    order_status = "Rejected"
else:
    if payment_method == "cash" and order_amount > 2500:
        order_status = "Manual Review"
    elif payment_method == "upi" or payment_method == "card":
        order_status = "Accepted"
    else:
        order_status = "Accepted"


# ORDER CATEGORY

if order_status == "Rejected":
    order_category = "Rejected Order"
elif order_status == "Manual Review":
    order_category = "Verification Required"
elif priority_status == "Priority":
    order_category = "Priority Order"
elif cancellation_risk == "High":
    order_category = "High Risk Order"
else:
    order_category = "Normal Order"


# FINAL AMOUNT

final_amount = order_amount - discount + delivery_charge

if order_status == "Rejected" or order_status == "Manual Review":
    final_amount = 0


# FINAL REPORT

print("\nFINAL ORDER REPORT")

print("Order Status:", order_status)
print("Delivery Charge:", delivery_charge)
print("Discount:", discount)
print("Priority Status:", priority_status)
print("Cancellation Risk:", cancellation_risk)
print("Restaurant Status:", restaurant_status)
print("Manual Review:", manual_review)
print("Final Order Category:", order_category)
print("Final Payable Amount:", round(final_amount, 2))