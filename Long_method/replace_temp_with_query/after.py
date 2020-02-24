class Company:
    def __init__(self, revenue, earnings, interests, amortization):
        self.revenue = revenue
        self.earnings_before_interest = earnings
        self.interests = interests
        self.amortization = amortization

    def get_EBITDA(self):
        return self.earnings_before_interest \
                 + self.interests \
                 + self.amortization

    def get_EBITDA_margin(self):
        EBITDA_margin = self.revenue / self.get_EBITDA()
        return EBITDA_margin