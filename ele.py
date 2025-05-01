#electricity bill calculater and display the results
def calculate_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (100 * 7) + (units - 200) * 10

def main():
    num_customers = int(input("Enter the number of customers: "))
    customers = []

    for _ in range(num_customers):
        name = input("Enter customer name: ")
        units = int(input(f"Enter electricity units used by {name}: "))
        bill = calculate_bill(units)
        customers.append({"name": name, "units": units, "bill": bill})

    print("\n--- Electricity Bills ---")
    for customer in customers:
        print(f"{customer['name']} - Units: {customer['units']} - Bill: ₹{customer['bill']}")

    # Find customer with highest bill
    highest = max(customers, key=lambda c: c['bill'])
    print(f"\nCustomer with highest bill: {highest['name']} - ₹{highest['bill']}")

if __name__ == "__main__":
    main()
