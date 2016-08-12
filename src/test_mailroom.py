# -*- coding: utf -8 -*-
import pytest

DONOR_DICT_KEYS = ['baker', 'williams', 'davidson']


DONOR_DICT_TEST = {
    'baker': [10.0, 20.0],
    'williams': [30.0, 40.0, 50.0],
    'davidson': [35.0, 28.0, 60.0]
}


DONOR_DICT_TEST_1 = {
    'baker': [10.0, 20.0],
    'williams': [30.0, 40.0, 50.0],
    'davidson': [35.0, 28.0, 60.0]
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


AMOUNT_TAB1 = [
    ('bill', 10, DONOR_DICT_TEST, {'bill': [10.0], 'baker': [10.0, 20.0],
                                                 'williams': [30.0, 40.0, 50.0],
                                                 'davidson': [35.0, 28.0, 60.0]}),
    ('baker', 100, DONOR_DICT_TEST, {'bill': [10.0],
                                                       'baker': [10.0, 20.0, 100.0],
                                                       'williams': [30.0, 40.0, 50.0],
                                                       'davidson': [35.0, 28.0, 60.0]}),
    ('matt', 65, DONOR_DICT_TEST, {'bill': [10.0], 'baker': [10.0, 20.0, 100.0],
                                                 'williams': [30.0, 40.0, 50.0],
                                                 'davidson': [35.0, 28.0, 60.0],
                                                 'matt': [65.0]})
]

MATH_CALC = [
    ['baker', 30.0, 2, 15.0],
    ['williams', 120.0, 3, 40.0],
    ['davidson', 123.0, 3, 41.0]
]


SORTED_LIST = [
        ['baker', 30.0, 2, 15.0],
        ['williams', 120.0, 3, 40.0],
        ['davidson', 123.0, 3, 41.0]
    ]


RESULT = [
                'baker 30.0 2 15.0',
                'williams 120.0 3 40.0',
                'davidson 123.0 3 41.0'
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


@pytest.mark.parametrize('u_input, u_amount, dictionary, result', AMOUNT_TAB1)
def test_amount_to_dict(u_input, u_amount, dictionary, result):
    from mailroom import amount_to_dict
    assert amount_to_dict(u_input, u_amount, dictionary) == result


def test_do_math():
    from mailroom import do_math
    assert do_math(DONOR_DICT_TEST_1) == MATH_CALC


def test_create_report():
    from mailroom import create_report
    assert create_report(SORTED_LIST) == RESULT
