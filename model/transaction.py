class Transaction:
    def __init__(self, date, transaction_type, category, amount, description):
        self.date = date
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return (f"Дата: {self.date},\nТип: {self.transaction_type},\nКатегория: {self.category},\nСумма: {self.amount},\n"
                f"Описание: {self.description}")
