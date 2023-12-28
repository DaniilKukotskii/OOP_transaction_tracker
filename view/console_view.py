import model.financial_manager
from model.financial_manager import FinancialManager
from presenter.financial_presenter import FinancialPresenter


class ConsoleView:
    def __init__(self):
        self.user_choice = None
        self.presenter = FinancialPresenter(FinancialManager(), self)
        self.num_of_del_transaction = None

    def show_menu(self):
        self.user_choice = input("Здравствуйте! Выберите действие:\n"
                                 "1. Журнал транзакций(действия).\n"
                                 "2. Добавить категорию транзакции.\n"
                                 "3. Просмотр категорий транзакций.\n")

        # Уходим в ветвление журнала транзакций
        if self.user_choice == "1":
            self.user_choice = input("Выберите действие: \n"
                  "1. Показать последние 5 транзакций.\n"
                  "2. Добавить запись транзакции.\n"
                  "3. Удалить запись транзакции.\n"
                  "4. Отредактировать запись транзакции.\n"
                  "5. Назад.\n"
                  "Выбор:")

            # Показ последних 5 транзакций:
            if self.user_choice == "1":
                self.presenter.show_last_5_transactions()

            # Добавление записи транзакции:
            elif self.user_choice == "2":
                self.add_transaction()

            # Удаление записи транзакции:
            elif self.user_choice == "3":
                num_of_del_transaction = input("Введите номер транзакции к удалению: ")
                FinancialManager.delete_transaction(num_of_del_transaction)     # я не знаю как через презентер передать индекс к удалению

            # Изменение записи транзакции:
            elif self.user_choice == "4":
                number_of_transaction = input("Выберите номер транзакции: ")
                num_of_el_transaction = input("Что необходимо изменить?"
                                              "1. Дата."
                                              "2. Тип транзакции."
                                              "3. Категория транзакции."
                                              "4. Сумма."
                                              "5. Описание."
                                              "Выбор: ")
                self.presenter.edit_transact(number_of_transaction, num_of_el_transaction)

            # откат в первоначальное меню(додумать)
            elif self.user_choice == "5":
                pass

        # возвращаемся в ветвление основного меню:
        # Добавляем категорию транзакции:
        elif self.user_choice == "2":
            name = input("Введите название категории: ")
            self.presenter.add_category(name)

        # Просматриваем имеющиеся категории транзакций:
        elif self.user_choice == "3":
            self.presenter.get_categories()

    def add_transaction(self):
        # Метод для добавления транзакции
        date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
        transaction_type = input("Выберите тип транзакции: ")
        amount = int(input("Введите сумму транзакции: "))
        description = input("Введите описание транзакции: ")
        category = input("Выберите категорию транзакции: ")

        self.presenter.add_transaction(date, transaction_type, amount, description, category)

    # def get_user_input(self):
    #     self.user_choice = input("Выбор: ")
