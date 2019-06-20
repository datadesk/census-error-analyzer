#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math


def convert_to_95_percent_confidence(moe):
    """
    Returns the provided margin of error converted to the 95% confidence level.

    Assumes the provided value was generated at the Census Bureau's standard 90% confidence level.
    """
    return (1.96 / 1.645) * moe


def convert_to_99_percent_confidence(moe):
    """
    Returns the provided margin of error converted to the 95% confidence level.

    Assumes the provided value was generated at the Census Bureau's standard 90% confidence level.
    """
    return (2.58 / 1.645) * moe


def statistical_difference(pair_one, pair_two):
    """
    Returns the statistical difference between two values, considering their respective margins of error.

    Accepts two lists, each expected to be a pair with the value first and the margin of error second.

    Assumes the provided margins of error were generated at the Census Bureau's standard 90% confidence level.
    """
    # Pull out the values
    estimate_one, moe_one = pair_one
    estimate_two, moe_two = pair_two

    # TK: Validate the margins to account for the Census Bureau's footnotes and exceptions

    # Take the difference of the estimates
    difference = estimate_one - estimate_two

    # Convert that to an absolute value
    abs_difference = abs(difference)

    # Square the margin of errors and combine them
    margins_squared = moe_one**2 + moe_two**2

    # Get the root of that result
    margins_root = math.sqrt(margins_squared)

    # Divide the absolute difference by the root
    return abs_difference / margins_root


def is_statistically_different(pair_one, pair_two):
    """
    Returns True or False whether two values, considering their respective margins of error, are statistically different.

    Accepts two lists, each expected to be a pair with the value first and the margin of error second.

    Assumes the provided margins of error were generated at the Census Bureau's standard 90% confidence level.
    """
    return statistical_difference(pair_one, pair_two) > 1.0
