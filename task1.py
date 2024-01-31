def calculate_contract_value(injection_dates, withdrawal_dates, purchase_prices, sale_prices, injection_rate, withdrawal_rate, max_volume, storage_cost_per_month):
    total_value = 0
    
    # Calculate total value for injection
    for i in range(len(injection_dates)):
        purchase_price = purchase_prices[i]
        storage_months = (withdrawal_dates[i] - injection_dates[i]).days / 30
        storage_cost = storage_cost_per_month * storage_months
        total_value -= purchase_price * injection_rate * max_volume
        total_value -= storage_cost
        
    # Calculate total value for withdrawal
    for i in range(len(withdrawal_dates)):
        sale_price = sale_prices[i]
        total_value += sale_price * withdrawal_rate * max_volume
        
    return total_value

# Example usage
injection_dates = [datetime(2024, 1, 1), datetime(2024, 3, 1)]
withdrawal_dates = [datetime(2024, 5, 1), datetime(2024, 7, 1)]
purchase_prices = [2.0, 2.1]  # $/MMBtu
sale_prices = [3.0, 3.2]  # $/MMBtu
injection_rate = 1000000  # MMBtu
withdrawal_rate = 1000000  # MMBtu
max_volume = 1000000  # MMBtu
storage_cost_per_month = 100000  # $

contract_value = calculate_contract_value(injection_dates, withdrawal_dates, purchase_prices, sale_prices, injection_rate, withdrawal_rate, max_volume, storage_cost_per_month)
print(f"Contract value: ${contract_value:.2f}")
