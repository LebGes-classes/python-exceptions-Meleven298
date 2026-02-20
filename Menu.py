from Card import Card


class Menu:
    '''Класс меню.'''

    def __init__(self, main_ekz) -> None:
        '''Инициализация класса Menu.

        Args:
            main_ekz: Экземпляр класса Main, к которому Menu будет обращаться
                               для выполнения действий.
        '''
        
        self.main_ekz = main_ekz

    def display_menu(self) -> None:
        '''Отображение меню.'''

        print("\n----- ГЛАВНОЕ МЕНЮ -----")
        print("1. Создать новую карточку")
        print("2. Показать все карточки")
        print("3. Изменить данные карточек")
        print("4. Списать карту")
        print("0. Выход из программы")
        print("------------------------")

    def main_program(self) -> None:
        '''Основной цикл интерактивного меню, делегирующий вызовы к Main.'''

        isTrue = True

        while isTrue:
            self.display_menu()
            
            choice = input("Выберите действие: ").strip()

            if choice == '1':
                isInt = True

                new_id = self.main_ekz.card_id + 1

                new_name = input('Введите наименование карточки: ')

                if not new_name.strip(): new_name = 'NoName'

                new_dealer = input('Введите имя поставщика: ')

                if not new_dealer.strip(): new_dealer = 'NoName'

                new_manufacturer = input('Введите имя производителя: ')

                if not new_manufacturer.strip(): new_manufacturer = 'NoName' 

                new_location = input('Введите местоположение товара(в координатах): ')

                if not new_location.strip(): new_location = 'Not defined'

                while isInt:
                    try:
                        new_amount = int(input('Введите количество: '))

                        isInt = False

                    except ValueError as e:
                        print(e)

                isInt = True

                while isInt:
                    try:
                        new_cost = float(input('Введите цену(в долларах): '))

                        isInt = False

                    except ValueError as e:
                        print(e)

                isInt = True

                while isInt:
                    try:
                        new_weight = int(input('Введите вес(в килограммах): '))

                        isInt = False

                    except ValueError as e:
                        print(e)

                isInt = True

                while isInt:
                    try:
                        new_height = int(input('Введите высоты(в сантиметрах): '))

                        isInt = False

                    except ValueError as e:
                        print(e)

                isInt = True

                while isInt:
                    try:
                        new_sale = int(input('Введите скидку(в процентах): '))

                        isInt = False

                    except ValueError as e:
                        print(e)

                new_card = Card(new_id, new_name, new_amount, new_dealer,
                                new_manufacturer, new_cost, new_location,
                                new_weight, new_height, new_sale)
                
                self.main_ekz.all_cards.append(new_card)

                if len(self.main_ekz.all_cards) > 1:
                    if self.main_ekz.all_cards[-2] and self.main_ekz.all_cards[-2].get_state() != 'Списано с учета':
                        self.main_ekz.all_cards[-2].set_state('Состоит на учете')
            elif choice == '2':
                self.main_ekz.view_all_cards()
            elif choice == '3':
                changing_card = self.main_ekz.select_card()

                print('Что вы желаете изменить? Введите 1-9')
                print('1. Наименование')
                print('2. Количество')
                print('3. Поставщика')
                print('4. Производителя')
                print('5. Цену')
                print('6. Местоположение')
                print('7. Вес')
                print('8. Высоту')
                print('9. Наличие скидки')

                try:
                    option = int(input())

                    if type(option) == int:
                        inChange = True

                        while inChange:
                            match option:
                                case 1:
                                    new_name = input('Введите новое наименование карточки: ')

                                    changing_card.set_name(new_name)
                                    inChange = False
                                case 2:
                                    new_amount = input('Введите новое количество в карточке: ')

                                    changing_card.set_amount(new_amount)
                                    inChange = False
                                case 3:
                                    new_dealer = input('Введите нового поставщика: ')

                                    changing_card.set_dealer(new_dealer)
                                    inChange = False
                                case 4:
                                    new_manufacturer = input('Введите нового производителя: ')

                                    changing_card.set_manufacturer(new_manufacturer)
                                    inChange = False
                                case 5:
                                    new_cost = input('Введите новую цену: ')

                                    changing_card.set_cost(new_cost)
                                    inChange = False
                                case 6:
                                    new_location = input('Введите новое местоположение: ')

                                    changing_card.set_location(new_location)
                                    inChange = False
                                case 7:
                                    new_weight = input('Введите новый вес: ')

                                    changing_card.set_weight(new_weight)
                                    inChange = False
                                case 8:
                                    new_height = input('Введите новую высоту: ')

                                    changing_card.set_height(new_height)
                                    inChange = False
                                case 9:
                                    new_sale = input('Введите новую скидку: ')

                                    changing_card.set_sale(new_sale)
                                    inChange = False
                                case _:
                                    print('Введенное значение не соотвествует доступным')

                                    option = int(input('Введите корректный номер опции для изменения (1-9): '))
                except ValueError as e:
                    print(e)
            elif choice == '4':
                expelling_card = self.main_ekz.select_card()
                self.main_ekz.expel_card(expelling_card)
            elif choice == '0':
                print("До свидания!")

                isTrue = False
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
    