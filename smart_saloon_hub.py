#1: Variable Declaration & Data Types
customer_name = input("Enter your name: ")   # Taking user input for name
customer_age = int(input("Enter your age: "))  # Taking user input for age
customer_gender = input("Enter your gender (Male/Female): ").capitalize()  # Taking user input for gender
is_vip = input("Are you a VIP customer? (yes/no): ").lower() == "yes"  # Boolean
services = ["Haircut", "Manicure", "Facial"]  # List of available services
prices = {"Haircut": 20, "Manicure": 15, "Facial": 30}  # Dictionary with service prices

#2: Conditional Statements
if customer_age < 18:
    print("You must be 18+ to book a salon service.")
else:
    title = "Ms." if customer_gender == "Female" else "Mr."
    print(f"Welcome, {title} {customer_name}! You can book an appointment.")

#3: Operators
total_price = prices["Haircut"] + prices["Manicure"]  # Example of arithmetic operators
print("Total price for Haircut & Manicure:", total_price)

#4: Loop: Display Available Services
print("Available Salon Services:")
for service in services:  # Loop through the list
    print("-", service)

#5: Function: Booking a Service
def book_service(name, service, gender):
    if service in prices:
        title = "Ms." if gender == "Female" else "Mr."
        print(f"{title} {name} booked {service} for ${prices[service]}.")
    else:
        print("Invalid service selected.")

#6: User Input & Function Call
selected_service = input("Enter a service to book: ")  # Taking user input
book_service(customer_name, selected_service, customer_gender)

#7: Assigning Stylist Based on Customer Preference
preferred_stylist_gender = input("Do you prefer a Male or Female stylist? ").capitalize()
print(f"A {preferred_stylist_gender.lower()} stylist has been assigned to you. Enjoy your service!")
