from model.transaction import Transaction
from model.category import Category


class FinancialManager:
    def __init__(self):
        self.categories = []

    def get_transactions(self):
        with open("journal.txt", "r", encoding='utf-8') as file:
            transactions_data = [line.strip().split("\n") for line in file.readlines()]

        transactions = [Transaction(*data) for data in transactions_data]

        for i, transaction in enumerate(transactions, 1):
            print(f"{i}. {transaction}")

    def get_last5_transactions(self):
        with open("journal.txt", "r", encoding='utf-8') as file:
            all_lines = file.readlines()
            last_5_transactions = all_lines[:5]
        return last_5_transactions

    def get_categories(self):
        num = 1
        for i in self.categories:
            print(f"{num}. {i}.\n")
            num += 1

    def add_categories(self, name):
        category = Category(name)
        self.categories.append(category)

    def add_transaction(self, date, transaction_type, amount, description, category=None):
        transaction = Transaction(date, transaction_type, amount, description)

        with open("journal.txt", "w", encoding='utf-8') as file:
            first_line = file.readline()
            file.seek(0, 0)
            file.write(f"{transaction}\n")
            if first_line:
                file.write(first_line)

    def delete_transaction(self, index_to_delete):
        with open("journal.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()

        # Проверяем, что индекс находится в пределах допустимых значений
        if 1 <= index_to_delete <= len(lines):
            del lines[index_to_delete - 1]  # Удаляем строку из списка

            # Перезаписываем файл с обновленными строками
            with open("journal.txt", "w", encoding='utf-8') as file:
                file.writelines(lines)

    def delete_categories(self):        # Додумать
        if len(self.categories) > 5:
            self.categories.pop(5)

    def edit_transaction(self, number_of_transaction, num_of_el_transaction):       # Додумать
        with open("journal.txt", "w", encoding='utf-8') as file:
            file.readlines()
            pass
