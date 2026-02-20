from Card import Card
from Menu import Menu


class Main:
    '''Класс Main.'''

    def __init__(self, card_id: int) -> None:
        '''Инициализация класса Main.

        Args:
            card_id: id карты, который определяется при ее создании
            all_cards: Список, в котором хранятся экземпляры класса Card.
        '''

        self.card_id = card_id
        self.all_cards: list[Card] = []

    def view_all_cards(self) -> None:
        '''Функция для просмотра всех карточек.'''

        try:
            for i, card in enumerate(self.all_cards):
                print(f'{i+1}. {card}')
        except IndexError as e:
            print(e, 'В списке отсутсвуют какие-либо карты.')

    def select_card(self) -> Card | None:
        '''Функция для выбора карточки.
        
        Returns: 
            Card: selected_card(выбранный экземпляр класса Card).

        Raises:
            IndexError: Если экземпляра с выбранным айди нету в списке.
        '''

        isTrue = True

        while isTrue:
            try:
                index = int(input('Введите идентификатор карты(или 0 для отмены выбора): '))

                if index > 0:
                    selected_card = self.all_cards[index-1]
                    isTrue = False

                    return selected_card
                
                elif index == 0:
                    isTrue= False
                else:
                    raise IndexError('Идентификатор должен быть целым положительным числом')
                
            except IndexError as e:
                print(e)

    def expel_card(self, expelling_card: Card) -> None:
        '''Функция для списания карточки.
        
        Args:
            Card: expelling_card(выбранный экземпляр класса Card на списание).
        '''

        print("\n--- Списание карты ---")

        expelling_card.set_state('Списана с учета')
        
        print(f"{expelling_card.get_name()} успешно списана c учета.")

if __name__ == "__main__":
    main = Main(0)
    menu = Menu(main)
    menu.main_program()
