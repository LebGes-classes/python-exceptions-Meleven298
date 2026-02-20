class Card:
    '''Класс карточки.'''

    def __init__(self, id: int=0, name: str='NoName', amount:int=0, dealer: str='NoName', 
                 manufacturer: str='NoName', cost: int=0, location: str='No location', weight: int=0,
                 height: int=0, sale: int=0, state: str='Принято к учету'):
        ''' Инициализация карточки.
        
        Args:
            id: Идентификатор карточки.
            name: Наименование карточки.
            amount: Количество товара.
            dealer: Поставщик товара.
            manufacturer: Производитель товара.
            cost: Цена товара.
            location: Местоположение товара.
            weight: Вес товара.
            height: Высота товара.
            sale: Скидка на товар
            state: Состояние товара.
        '''

        self.__id = id
        self.__name = name
        self.__amount = amount
        self.__dealer = dealer
        self.__manufacturer = manufacturer
        self.__cost = cost
        self.__location = location
        self.__weight = weight
        self.__height = height
        self.__sale = sale
        self.__state = state

    def get_name(self) -> str:
        '''Геттер для наименования.

            Returns:
                str: __name
        '''

        return self.__name
    
    def set_name(self, name: str) -> None:
        '''Сеттер для имени.
        
            Args:
                str: name(новое значение для __name)
        '''

        if name.strip():
            self.__name = name
        else:
            self.__name = 'NoName'
    
    def get_amount(self) -> int:
        '''Геттер для количества.
        
            Returns:
                int: __amount
        '''

        return self.__amount
    
    def set_amount(self, amount: int) -> None:
        '''Сеттер для количества.
        
            Args:
                int: amount(новое значение для __amount)
        '''

        isTrue = True

        while isTrue:
            try:
                if type(int(amount)) == int:
                    self.__amount = amount
                    isTrue = False
            except ValueError as e:
                print(e)
                print('Введите целое положительное число')

                amount = input()
    
    def get_dealer(self) -> str:
        '''Геттер для поставщика.
        
            Returns:
                str: __dealer
        '''

        return self.__dealer
    
    def set_dealer(self, dealer: str) -> None:
        '''Сеттер для поставщика.
        
            Args:
                str: dealer(новое значение для __dealer)
        '''

        if dealer.strip():
            self.__dealer = dealer
        else:
            self.__dealer = 'NoName'
    
    def get_manufacturer(self) -> str:
        '''Геттер для производителя.
        
            Returns:
                str: __manufacturer
        '''

        return self.__manufacturer
    
    def set_manufacturer(self, manufacturer: str) -> None:
        '''Сеттер для производителя.
        
            Args:
                str: manufacturer(новое значение для __manufacturer)
        '''

        if manufacturer.strip():
            self.__manufacturer = manufacturer
        else:
            self.__manufacturer = 'NoName'
    
    def get_cost(self) -> int:
        '''Геттер для цены.
        
            Returns:
                int: __cost
        '''

        return self.__cost
    
    def set_cost(self, cost: int) -> None:
        '''Сеттер для цены.
        
            Args:
                int: cost(новое значение для __cost)
        '''

        isTrue = True

        while isTrue:
            try:
                if type(int(cost)) == int:
                    self.__cost = cost
                    isTrue = False
            except ValueError as e:
                print(e)
                print('Введите целое положительное число')

                cost = input()
    
    def get_location(self) -> str:
        '''Геттер для местоположения.
        
            Returns:
                str: __location
        '''

        return self.__location
    
    def set_location(self, location: str) -> None:
        '''Сеттер для местоположения.
        
            Args:
                str: location(новое значение для __location)
        '''

        if location.strip():
            self.__location = location 
        else:
            self.__location = 'Not defined' 
    
    def get_weight(self) -> int:
        '''Геттер для веса.
        
            Returns:
                int: __weight
        '''

        return self.__weight
    
    def set_weight(self, weight: int) -> None:
        '''Сеттер для веса.
        
            Args:
                int: weight(новое значение для __weight)
        '''

        isTrue = True

        while isTrue:
            try:
                if type(int(weight)) == int:
                    self.__weight = weight
                    isTrue = False
            except ValueError as e:
                print(e)
                print('Введите целое положительное число')

                weight = input()
    
    def get_height(self) -> int:
        '''Геттер для высоты.
        
            Returns:
                int: __height
        '''

        return self.__height
    
    def set_height(self, height: int) -> None:
        '''Сеттер для высоты.
        
            Args:
                int: height(новое значение для __height)
        '''

        isTrue = True

        while isTrue:
            try:
                if type(int(height)) == int:
                    self.__height = height
                    isTrue = False
            except ValueError as e:
                print(e)
                print('Введите целое положительное число')

                height = input()
    
    def get_sale(self) -> int:
        '''Геттер для скидки.
        
            Returns:
                int: __sale
        '''

        return self.__sale
    
    def set_sale(self, sale: int) -> None:
        '''Сеттер для скидки.
        
            Args:
                int: sale(новое значение для __sale)
        '''

        isTrue = True

        while isTrue:
            try:
                if type(int(sale)) == int:
                    self.__sale = sale
                    isTrue = False
            except ValueError as e:
                print(e)
                print('Введите целое положительное число')

                sale = input()

    def get_state(self) -> str:
        '''Геттер для состояния.
        
            Returns:
                int: __state
        '''

        return self.__location
    
    def set_state(self, state: str) -> None:
        '''Сеттер для состояния.
        
            Args:
                str: state(новое значение для __state)
        '''

        self.__state = state
        
    def __str__(self) -> str:
        '''Функция для представления экземпляра класса в строковом виде.
        
        Returns:
            f-строка
        '''

        return f"""Карточка {self.__name}.
          Идентификатор: {self.__id}
          Количество: {self.__amount}.
          Поставщик: {self.__dealer}.
          Производитель: {self.__manufacturer}.
          Цена: {self.__cost}.
          Местоположение: {self.__location}.
          Вес: {self.__weight}.
          Высота: {self.__height}.
          Скидка: {'Есть' if self.__sale else 'Отсутствует'}.
          Состояние: {self.__state}"""
        