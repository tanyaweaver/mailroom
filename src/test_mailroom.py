# -*- coding: utf -8 -*-
import pytest


MENU_INPUTS = [
    (u'thank you letter', u'thank you letter'),
    (u'report', u'report'),
    (123, u'invalid input')
]


NAME_INPUTS = [
    (u'dan', u'dan'),
    (u' ', u'invalid input'),
    (123, u'invalid input')
]


AMOUNT_INPUTS = [
    (1, 1),
    (1.5, 1.5),
    (u'a', u'invalid input'),
]


DONOR_DICT_TEST = {
    u'baker': [10.0, 20.0],
    u'williams': [30.0, 40.0, 50.0],
    u'davidson': [35.0, 28.0, 60.0]
}


DONOR_DICT_TEST_1 = {
    u'baker': [10.0, 20.0],
    u'williams': [30.0, 40.0, 50.0],
    u'davidson': [35.0, 28.0, 60.0]
}


UPDATED_DICT = [
    (u'bill', 10, DONOR_DICT_TEST, {u'bill': [10.0],
                                    u'baker': [10.0, 20.0],
                                    u'williams': [30.0, 40.0, 50.0],
                                    u'davidson': [35.0, 28.0, 60.0]}),
    (u'baker', 100, DONOR_DICT_TEST, {u'bill': [10.0],
                                      u'baker': [10.0, 20.0, 100.0],
                                      u'williams': [30.0, 40.0, 50.0],
                                      u'davidson': [35.0, 28.0, 60.0]}),
    (u'matt', 65, DONOR_DICT_TEST, {u'bill': [10.0],
                                    u'baker': [10.0, 20.0, 100.0],
                                    u'williams': [30.0, 40.0, 50.0],
                                    u'davidson': [35.0, 28.0, 60.0],
                                    u'matt': [65.0]})
]


SORTED_STATS_LIST = [
    [u'baker', 30.0, 2, 15.0],
    [u'williams', 120.0, 3, 40.0],
    [u'davidson', 123.0, 3, 41.0]
]


@pytest.mark.parametrize(u'u_input, result', MENU_INPUTS)
def test_initial_prompt_validator(u_input, result):
    from mailroom import initial_prompt_validator
    assert initial_prompt_validator(u_input) == result


@pytest.mark.parametrize(u'u_input, result', NAME_INPUTS)
def test_name_prompt_validator(u_input, result):
    from mailroom import name_prompt_validator
    assert name_prompt_validator(u_input) == result


@pytest.mark.parametrize(u'u_input, result', AMOUNT_INPUTS)
def test_amount_prompt_validator(u_input, result):
    from mailroom import amount_prompt_validator
    assert amount_prompt_validator(u_input) == result


@pytest.mark.parametrize(u'u_input, amount, dictionary, result', UPDATED_DICT)
def test_update_dict(u_input, amount, dictionary, result):
    from mailroom import update_dict
    assert update_dict(u_input, amount, dictionary) == result


def test_do_math():
    from mailroom import do_math
    assert do_math(DONOR_DICT_TEST_1) == SORTED_STATS_LIST


def test_generate_letter():
    from mailroom import generate_letter
    assert generate_letter('smith', 100) == u'Dear Smith, '\
        u'thank you for your donation of $100.'
