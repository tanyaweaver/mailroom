# -*- coding: utf -8 -*-
DONOR_DICT = {}


def initial_prompt():
    user_menu_choice = input('Choose: Thank You Letter or Report  ')
    print(user_menu_choice)
    return user_menu_choice.lower()


def initial_prompt_validator(user_menu_choice):
    if user_menu_choice in ('thank you letter', 'report'):
        return user_menu_choice
    else:
        print('Invalid Input')
        return 'invalid input'


def menu_choice_action(user_menu_choice):
    if user_menu_choice == 'thank you letter':
        name_prompt()
    elif user_menu_choice == 'report':
        create_report()
    else: 
        initial_prompt()

def name_prompt():
    donor_name_input = input('Enter Donor Name or List')
    if donor_name_input.lower() == 'list':
        print(DONOR_DICT.keys())
        name_prompt()
    elif isinstance(donor_name_input.lower(), str):
        DONOR_DICT.setdefault(donor_name_input.lower(), [])
        amount_prompt()
    else:
        print('Invalid Input')
        name_prompt()


def create_report():
    pass


def amount_prompt():

    if isinstance(donor_amount.lower(), str):
        donor_dict.setdefault(donor_name_input.lower(), []).append(donor_name_input.lower())
