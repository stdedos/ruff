"""Tests for R1709."""

from UNINFERABLE import condition

TRUE_VALUE = True
FALSE_VALUE = False


def simplify(oranges, apples=None) -> bool:
    return apples and False or oranges  # [simplify-boolean-expression]


def does_not_have_condition():
    false_value = False
    return condition and false_value or FALSE_VALUE  # [simplify-boolean-expression]


# ^^ original pylint tests
# New Permutations


def simplify_with_false_constant(oranges, apples=None) -> bool:
    return apples and FALSE_VALUE or oranges  # [simplify-boolean-expression]


def simplify_false_first(oranges, apples=None) -> bool:
    return False and apples or oranges  # XXX: pylint does not flag this


def simplify_with_false_constant_first(oranges, apples=None) -> bool:
    return FALSE_VALUE and apples or oranges  # XXX: pylint does not flag this


def simplify_with_true(oranges, apples=None) -> bool:
    return apples and True or oranges  # [consider-using-ternary] ??


def simplify_with_true_constant(oranges, apples=None) -> bool:
    return apples and TRUE_VALUE or oranges  # [consider-using-ternary] ??


def simplify_true_second(oranges, apples=None) -> bool:
    return apples and oranges or True   # XXX: pylint does not flag this


def simplify_with_true_constant_second(oranges, apples=None) -> bool:
    return apples and oranges or TRUE_VALUE  # XXX: pylint does not flag this


def does_not_have_condition_with_false() -> bool:
    return condition and False  # XXX: pylint does not flag this


def does_not_have_condition_with_false_constant() -> bool:
    return condition and FALSE_VALUE  # XXX: pylint does not flag this


def does_not_have_condition_with_true() -> bool:
    # This is a short-circuit operation - it MUST NOT be interfered with!
    return condition or True


def does_not_have_condition_with_true_constant() -> bool:
    # This is a short-circuit operation - it MUST NOT be interfered with!
    return condition or TRUE_VALUE


# `condition` can be ANYTHING. Not even exist!


def starts_with_true() -> bool:
    return True or condition  # XXX: pylint does not flag this


def starts_with_true_constant() -> bool:
    return TRUE_VALUE or condition  # XXX: pylint does not flag this


def starts_with_false() -> bool:
    return False and condition  # XXX: pylint does not flag this


def starts_with_false_constant() -> bool:
    return FALSE_VALUE and condition  # XXX: pylint does not flag this
