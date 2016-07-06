class Budgets:

    usd_to_eur = 0.85
    gbp_to_eur = 1.10

    def __init__(self, budget_value, budget_currency):
        self.budget_value = budget_value
        self.budget_currency = budget_currency
        self.budget_eur = None

    def calculate_budget_eur(self):
        if self.budget_currency == "USD":
            self.budget_eur = float(self.budget_value) * Budgets.usd_to_eur
        elif self.budget_currency == "GBP":
            self.budget_eur = float(self.budget_value) * Budgets.gbp_to_eur
        else:
            self.budget_eur = float(self.budget_value)
        return self.budget_eur