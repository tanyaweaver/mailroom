# -*- coding: utf -8 -*-
import pytest

DONOR_DICT_KEYS = ['baker', 'williams', 'davidson']
DONOR_DICT_TEST = {
    'baker': [10, 20],
    'williams': [30, 40, 50],
    'davidson': [35, 28, 60]
}


DONOR_DICT_TEST_1 = {
    'baker': [10, 20],
    'williams': [30, 40, 50],
    'davidson': [35, 28, 60]
}


MENU_TABLE = [
    ('thank you letter', 'thank you letter'),
    ('report', 'report'),
    (123, 'invalid input')
]


NAME_TABLE = [
    ('dan', 'dan'),
    (' ', 'invalid input'),
    (123, 'invalid input')
]


AMOUNT_TABLE = [
    (1, 1),
    (1.5, 1.5),
    ('a', 'invalid input'),
]


DONOR_AMOUNT_TABLE = [
    ('bill', 10, DONOR_DICT_TEST, {'bill': [10], 'baker': [10, 20],
                                                 'williams': [30, 40, 50],
                                                 'davidson': [35, 28, 60]}),
    ('baker', 100, DONOR_DICT_TEST, {'bill': [10],
                                                       'baker': [10, 20, 100],
                                                       'williams': [30, 40, 50],
                                                       'davidson': [35, 28, 60]}),
    ('matt', 65, DONOR_DICT_TEST, {'bill': [10], 'baker': [10, 20, 100],
                                                 'williams': [30, 40, 50],
                                                 'davidson': [35, 28, 60],
                                                 'matt': [65]},)
]

MATH_CALC = [
    ['baker', 30, 2, 15.0],
    ['williams', 120, 3, 40.0],
    ['davidson', 123, 3, 41.0]
]


DO_MATH_TABLE = [DONOR_DICT_TEST_1, MATH_CALC]


SORTED_LIST = [
        ['baker', 30, 2, 15.0],
        ['williams', 120, 3, 40.0],
        ['davidson', 123, 3, 41.0]
    ]


RESULT = [
                'baker 30 2 15.0',
                'williams 120 3 40.0',
                'davidson 123 3 41.0'
                ]


@pytest.mark.parametrize('u_input, result', MENU_TABLE)
def test_initial_prompt_validator(u_input, result):
    from mailroom import initial_prompt_validator
    assert initial_prompt_validator(u_input) == result


@pytest.mark.parametrize('u_input, result', NAME_TABLE)
def test_name_prompt_validator(u_input, result):
    from mailroom import name_prompt_validator
    assert name_prompt_validator(u_input) == result


@pytest.mark.parametrize('u_input, result', AMOUNT_TABLE)
def test_amount_prompt_validator(u_input, result):
    from mailroom import amount_prompt_validator
    assert amount_prompt_validator(u_input) == result


@pytest.mark.parametrize('u_input, u_amount, dictionary, result', DONOR_AMOUNT_TABLE)
def test_amount_to_dict(u_input, u_amount, dictionary, result):
    from mailroom import amount_to_dict
    assert amount_to_dict(u_input, u_amount, dictionary) == result


# @pytest.mark.parametrize('dictionary, result', DO_MATH_TABLE)
# def test_do_math(dictionary, result):
#     from mailroom import do_math
#     assert do_math(dictionary) == result


def test_create_report():
    # list_sorted = [
    #     ['baker', 30, 2, 15.0],
    #     ['williams', 120, 3, 40.0],
    #     ['davidson', 123, 3, 41.0]
    # ]
    # result = [
    #             'baker              30                 2                  15.0               ',
    #             'williams           30                 2                  15.0               ',
    #             'davidson          30                 2                  15.0               '
    #             ]
    from mailroom import create_report
    assert create_report(SORTED_LIST) == RESULT
