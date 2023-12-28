from model.financial_manager import FinancialManager
from view.console_view import ConsoleView
from view.report_generator import ReportGenerator
from presenter.financial_presenter import FinancialPresenter


def main():
    manager = FinancialManager()
    view = ConsoleView()
    report_generator = ReportGenerator()
    presenter = FinancialPresenter(manager, view)

    while True:
        view.show_menu()
        choice = view.user_choice

        if choice.lower() == 'выход':
            break

        try:
            if choice == '1':
                presenter.show_last_5_transactions()
            elif choice == '2':
                presenter.add_transaction()
            elif choice == '3':
                presenter.delete_transaction()
            elif choice == '4':
                presenter.edit_transaction()
            elif choice == '5':
                # Добавьте здесь логику для возврата в основное меню, если нужно
                pass
            elif choice == '6':
                presenter.add_category()
            elif choice == '7':
                presenter.get_categories()
            else:
                print("Неверный выбор. Пожалуйста, введите снова.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
