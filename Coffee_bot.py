def coffee_bot():
    print('Welcome to the cafe!')


def get_size():
    while True:
        res = input('What size drink can I get for you? \n[1] Small \n[2] Medium \n[3] Large \n ')

        if res == '1':
            return 'small'
        elif res == '2':
            return 'medium'
        elif res == '3':
            return 'large'
        else:
            print_message()
            return get_size()


def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')


def get_drink_type():
    while True:
        res = input('What type of drink would you like? \n[1] Brewed Coffee \n[2] Mocha \n[3] Latte \n ')

        if res == '1':
            return 'brewed coffee'
        elif res == '2':
            return order_mocha()
        elif res == '3':
            return order_latte()
        else:
            print_message()
            return get_drink_type()


def order_latte():
    while True:
        res = input('And what kind of milk for your latte? \n[1] 2% milk \n[2] Non-fat milk \n[3] Soy milk \n ')

        if res == '1':
            return 'latte'
        elif res == '2':
            return 'non-fat latte'
        elif res == '3':
            return 'soy latte'
        else:
            print_message()
            order_latte()


def order_mocha():
    while True:
        res = input('Would you like to try our limited-edition peppermint mocha? \n[1] Sure! \n[2] Maybe next time! \n ')

        if res == '1':
            return 'peppermint mocha'
        elif res == '2':
            return 'mocha'
        else:
            print_message()
            order_mocha()


def get_cup_type():
    while True:
        res = input('Which cup would you like to use? \n[1] Plastic \n[2] Your own \n ')

        if res == '1':
            return 'plastic'
        elif res == '2':
            return 'your own'
        else:
            print_message()
            get_cup_type()


def get_hot_iced():
    while True:
        res = input('Would you like your drink hot or iced? \n[1] Hot \n[2] Iced \n ')

        if res == '1':
            return 'hot'
        elif res == '2':
            return 'iced'
        else:
            print_message()
            get_hot_iced()
    

def main():
    coffee_bot()
    order_drink = 'y'
    drinks = []

    while order_drink == 'y':    
        size = get_size()
        drink_type = get_drink_type()
        cup_type = get_cup_type()
        hot_iced = get_hot_iced()
    
        print(f'Alright, that\'s a {size}, {hot_iced} {drink_type} in {cup_type} cup!')
        drinks.append(drink_type)
        
        while True:
            order_drink = input('Would you like to order another drink? (y/n) \n ')

            if order_drink in ['y', 'n']:
                break

        print('Okay, so I have:')

        for drink in drinks:
            print(f'- {hot_iced} {drink}')

    name = input('Can I get your name please? ')

    print(f'Thanks, {name}! Your drink will be ready shortly.')
    

if __name__ == '__main__':
    main()