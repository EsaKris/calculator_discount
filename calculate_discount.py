def calculate_discount(price, discount_percent):
    """Calculate the final price after applying discount if it's 20% or higher"""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return round(final_price, 2)
    return round(price, 2)

def display_results(original_price, discount_percent, final_price):
    """Display the results in a user-friendly format"""
    print("\n" + "="*40)
    print("DISCOUNT CALCULATION RESULTS".center(40))
    print("="*40)
    print(f"{'Original Price:':<20} ${original_price:>10.2f}")
    print(f"{'Discount Percent:':<20} {discount_percent:>10}%")
    
    if discount_percent >= 20:
        discount_amount = original_price - final_price
        print(f"{'Discount Amount:':<20} ${discount_amount:>10.2f}")
        print("-"*40)
        print(f"{'Final Price:':<20} ${final_price:>10.2f}")
    else:
        print("-"*40)
        print("No discount applied (less than 20%)")
        print(f"{'Final Price:':<20} ${final_price:>10.2f}")
    print("="*40 + "\n")

def get_user_input():
    """Get and validate user input"""
    while True:
        try:
            price = float(input("Enter the original price of the item: $"))
            if price <= 0:
                print("Price must be greater than 0. Please try again.")
                continue
            
            discount = float(input("Enter the discount percentage (0-100): "))
            if discount < 0 or discount > 100:
                print("Discount must be between 0 and 100. Please try again.")
                continue
            
            return price, discount
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    """Main application function"""
    print("\n" + "="*40)
    print("DISCOUNT CALCULATOR".center(40))
    print("="*40)
    
    while True:
        # Get user input
        original_price, discount_percent = get_user_input()
        
        # Calculate final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Display results
        display_results(original_price, discount_percent, final_price)
        
        # Ask if user wants to continue
        another = input("Calculate another discount? (y/n): ").lower()
        if another != 'y':
            print("\nThank you for using the Discount Calculator!")
            break

if __name__ == "__main__":
    main()