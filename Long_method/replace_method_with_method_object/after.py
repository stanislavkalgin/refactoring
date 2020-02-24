def weighed_profit():
    return WeighedProfitCalc().compute()


class WeighedProfitCalc:
    def __init__(self):
        self.items_sale_prices = {'item1': 400, 'item2': 300, 'item3': 500}
        self.items_purchase_prices = {'item1': 200, 'item2': 150, 'item3': 100}
        self.sale_volumes = {'item1': 540, 'item2': 456, 'item3': 234}
        self.fixed_costs_by_period = 60_000
        self.profit_tax = 0.2
        self.capital_cost_by_period = 1.15

    def compute(self):
        profit_margin = 0
        for key in self.items_sale_prices:
            profit_margin += ((self.items_sale_prices[key] -
                               self.items_purchase_prices[key]) *
                              self.sale_volumes[key])
        profit = profit_margin - self.fixed_costs_by_period
        profit -= profit * self.profit_tax
        weighed_profit = profit / self.capital_cost_by_period
        return weighed_profit

print(weighed_profit())
