import requests


def get_nbu_rate(currency_code: str) -> float | None:
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code.upper()}&json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  #check for http errors (404, 500 status)
        data = response.json()

        if data:
            return data[0]["rate"]
        return None
    except requests.exceptions.RequestException as e:
        print(f"\nCannot get data from bank ({e})")
        return None


def run():
    allowed_currencies = ["USD", "EUR", "PLN"]

    while True:
        currency = (
            input(f"Type currency type ({', '.join(allowed_currencies)}): ")
            .strip()
            .upper()
        )
        if currency in allowed_currencies:
            break
        print(
            f"This currency ({', '.join(allowed_currencies)}) is not supported\n"
        )

    while True:
        try:
            amount = float(input(f"Type amount of {currency}: "))
            if amount <= 0:
                print("Must be greater than 0!\n")
                continue
            break
        except ValueError:
            print("Value is incorrect!\n")

    print("\nRequesting the actual rate from the bank...")
    rate = get_nbu_rate(currency)

    if rate is not None:
        total_uah = amount * rate
        print(f"Rate: 1 {currency} = {rate:.4f} UAH")
        print(f"Result: {amount:,.2f} {currency} = {total_uah:,.2f} UAH")
    else:
        print(
            "An error was occured while requesting actual rate"
        )
        
run()