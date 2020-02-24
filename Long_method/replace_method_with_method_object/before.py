def get_weighed_profit():
    items_sale_prices = {'item1': 400, 'item2': 300, 'item3': 500}
    items_purchase_prices = {'item1': 200, 'item2': 150, 'item3': 100}
    sale_volumes = {'item1': 540, 'item2': 456, 'item3': 234}
    fixed_costs_by_period = 60_000
    profit_tax = 0.2
    capital_cost_by_period = 1.15

    profit_margin = 0
    for key in items_sale_prices:
        profit_margin += ((items_sale_prices[key] - items_purchase_prices[key]) * sale_volumes[key])
    profit = profit_margin - fixed_costs_by_period
    profit -= profit * profit_tax
    weighed_profit = profit/capital_cost_by_period
    return weighed_profit
