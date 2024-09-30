import requests

class CurrencyConverter:
    def __init__(self):
        self.api_url = 'https://api.exchangerate-api.com/v4/latest/'  # API para taxas de câmbio

    def get_exchange_rates(self, base_currency):
        """Obtém as taxas de câmbio para a moeda base especificada."""
        response = requests.get(f"{self.api_url}{base_currency}")
        data = response.json()
        return data['rates']
    
    def convert_currency(self, amount, from_currency, to_currency, rates):
        """Converte um valor de uma moeda para outra."""
        if from_currency == to_currency:
            return amount
        converted_amount = amount * rates[to_currency] / rates[from_currency]
        return converted_amount

def main():
    print("Bem-vindo ao Conversor de Moedas!")
    
    base_currency = input("Digite a moeda base (ex: USD, EUR): ").upper()
    rates = CurrencyConverter().get_exchange_rates(base_currency)

    print("Taxas de câmbio disponíveis:")
    for currency in rates.keys():
        print(currency)

    from_currency = input("Digite a moeda de origem: ").upper()
    to_currency = input("Digite a moeda de destino: ").upper()
    amount = float(input("Digite o valor a ser convertido: "))

    if from_currency not in rates or to_currency not in rates:
        print("Uma das moedas não está disponível nas taxas de câmbio.")
        return

    converted_amount = CurrencyConverter().convert_currency(amount, from_currency, to_currency, rates)

    print(f"{amount} {from_currency} é igual a {converted_amount:.2f} {to_currency}.")

if __name__ == "__main__":
    main()