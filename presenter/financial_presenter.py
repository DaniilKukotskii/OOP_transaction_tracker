from model.financial_manager import FinancialManager
from view.report_generator import ReportGenerator


class FinancialPresenter:
    def __init__(self, manager, view):
        self.manager = FinancialManager()
        self.report_generator = ReportGenerator()

    def get_categories(self):
        self.manager.get_categories()

    def show_last_5_transactions(self):
        self.manager.get_last5_transactions()

    def edit_transact(self, number_of_transaction, num_of_el_transaction):
        self.manager.change_transaction(number_of_transaction, num_of_el_transaction)

    def add_transaction(self, date, transaction_type, amount, description, category):
        # Метод для добавления транзакции
        # Вызываем соответствующий метод у менеджера
        self.manager.add_transaction(date, transaction_type, amount, description, category)

    def add_category(self, name):
        # Метод для добавления категории
        # Вызываем соответствующий метод у менеджера
        self.manager.add_categories(name)
