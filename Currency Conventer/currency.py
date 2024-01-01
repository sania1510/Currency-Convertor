from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()

    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to the Currency Converter!")
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency (e.g., USD): ").upper()
    print()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()
    print()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if isinstance(converted_amount, str):
        print(converted_amount)
    else:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
