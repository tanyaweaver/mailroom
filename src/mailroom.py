#!/usr/bin/env python
# -*- coding: utf -8 -*-
from __future__ import division


from sys import exit


try:
    input = raw_input
except NameError:
    pass
DONOR_DICT = {
    u'baker': [10.0, 20.0],
    u'williams': [30.0, 40.0, 50.0],
    u'davidson': [35.0, 28.0, 60.0]
}


def initial_prompt():
    """Run the main menu prompt."""
    user_menu_choice = input(u'Choose: Thank You Letter or Report (Q to exit) ').lower()
    return user_menu_choice


def initial_prompt_validator(user_menu_choice):
    """Validate user input from the initial_prompt."""
    if user_menu_choice in (u'thank you letter', 'report'):
        return user_menu_choice
    elif user_menu_choice == 'q':
        exit()
    else:
        print(u'Invalid Input')
        return u'invalid input'


def name_prompt():
    """Prompt user for a name, or asks for list to print the names in dict."""
    donor_name_input = input(u'Enter Donor Name or List '
                             u'(Q to return to Main Menu) ').lower()
    return donor_name_input


def name_prompt_validator(donor_name_input):
    """Validate name_prompt's input."""
    if donor_name_input == u'q':
        main_function()
    else:
        try:
            if int(donor_name_input) or float(donor_name_input):
                print(u'Invalid Input')
                return u'invalid input'
        except ValueError:
            if donor_name_input != ' ':
                return donor_name_input
            else:
                print(u'Invalid Input')
                return u'invalid input'


def amount_prompt():
    """Prompt for donation amount."""
    donation_amount = input(u'Enter Donation Amount  '
                            u'(Q to return to Main Menu)')
    return donation_amount


def amount_prompt_validator(donation_amount):
    """Validate donation amount."""
    if donation_amount == u'q':
            main_function()
    else:
        try:
            if int(donation_amount) or float(donation_amount):
                return float(donation_amount)
        except ValueError:
            print(u'Invalid Input')
            return u'invalid input'


def amount_to_dict(donor_name_input, donation_amount, dictionary):
    """Check if name is in dict, add if not and append donation as a value."""
    dictionary.setdefault(donor_name_input, []).append(donation_amount)
    # return donor_name_input, dictionary[donor_name_input]
    return dictionary


def generate_letter(donor_name_input, donation_amount):
    """Generate thank you letter with name and new donation."""
    print(u'Dear {0}, thank you for your donation of '
          u'${1}.'.format(donor_name_input, donation_amount))


def do_math(dictionary):
    """Find sum, no. of donations, and avg of donations for individuals."""
    summary_list = []
    for key in dictionary:
        donor_math_list = []
        value = dictionary[key]
        total = sum(value)
        count = len(value)
        average = total / count
        donor_math_list = [key, total, count, average]
        summary_list.append(donor_math_list)
    return sorted(summary_list, key=lambda x: x[1])


def create_report(list_sorted):
    """Print report of donors, with sum, count of, and avg of donations."""
    print(u'{:<15} {:<15} {:<15} {:<15}'
          .format('Name', 'Total', 'Count', 'Average'))
    print_out_list = []
    for individual_donor_list in list_sorted:
        print_each_donor = (u'{:<15} {:<15} {:<15} {:<15}'
                            .format(*individual_donor_list))
        print_out_list.append(print_each_donor)
        print(print_each_donor)
    return print_out_list


def name_prompt_call(donor_name):
    """Shortcut used in main_function."""
    DONOR_DICT.setdefault(donor_name.lower(), [])
    donation_amount = amount_prompt_validator(amount_prompt())
    amount_to_dict(donor_name, donation_amount, DONOR_DICT)
    generate_letter(donor_name, donation_amount)


def main_function():
    """Main function to call other functions."""
    user_menu_choice = initial_prompt_validator(initial_prompt())
    if user_menu_choice == u'thank you letter':
        donor_name = name_prompt_validator(name_prompt())
        if donor_name == u'list':
            print(DONOR_DICT.keys())
            donor_name = name_prompt_validator(name_prompt())
        elif donor_name == u'invalid input':
            donor_name = name_prompt_validator(name_prompt())
        name_prompt_call(donor_name)
        main_function()
    elif user_menu_choice == u'report':
        create_report(do_math(DONOR_DICT))
        main_function()
    else:
        main_function()


if __name__ == '__main__':
    main_function()
