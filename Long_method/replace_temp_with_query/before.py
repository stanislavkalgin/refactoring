class Company:
    def __init__(self, revenue, earnings, interests, amortization):
        self.revenue = revenue
        self.earnings_before_interest = earnings
        self.interests = interests
        self.amortization = amortization

    def get_EBITDA_margin(self):
        EBITDA = self.earnings_before_interest\
                 + self.interests\
                 + self.amortization

        EBITDA_margin = self.revenue / EBITDA
        return EBITDA_margin