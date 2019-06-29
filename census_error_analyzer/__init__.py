#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math


def statistical_range(estimate, margin_of_error):
    """
    The minimum and maximum values for a statistical estimate.

    Args:
        estimate (int): An estimate value from the U.S. Census Bureau
        margin_or_error (float): The bureau's estimate of the value's margin of error

    Returns:
        A two-item tuple with the minimum and maximum value in the estimates statistical range

        (37.8, 38.0)

    Examples:
        >>> statistical_range(37.9, 0.1)
        37.8, 38.0
    """
    return estimate - margin_of_error, estimate + margin_of_error


def convert_to_95_percent_confidence(margin_of_error):
    """
    Converts a margin of error from the U.S. Census Bureau to the 95% confidence level.

    Args:
        margin_or_error (float): A margin of error at the bureau's standard 90% confidence level

    Returns:
        The adjusted margin of error (float).

        4501.446808510638

    Examples:
        >>> convert_to_95_percent_confidence(3778)
        4501.446808510638
    """
    return (1.96 / 1.645) * margin_of_error


def convert_to_99_percent_confidence(margin_of_error):
    """
    Converts a margin of error from the U.S. Census Bureau to the 99% confidence level.

    Args:
        margin_or_error (float): A margin of error at the bureau's standard 90% confidence level

    Returns:
        The adjusted margin of error (float).

        5925.373860182372

    Examples:
        >>> convert_to_95_percent_confidence(3778)
        5925.373860182372
    """
    return (2.58 / 1.645) * margin_of_error


def statistical_difference(pair_one, pair_two):
    """
    The statistical difference between two values, considering their respective margins of error.

    Assumes the provided margins of error were generated at the Census Bureau's standard 90% confidence level.

    Args:
        pair_one (list): A two-item list with a U.S. Census bureau estimate and its margin of error
        pair_two (list): Another two-item list with a U.S. Census bureau estimate and its margin of error

    Returns:
        A statistical value measuring the difference (float).

    Examples:
        >>> statistical_difference((37.9, 0.1), (38.4, 0.1))
        3.535533905932737
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
    Are two values, considering their respective margins of error, statistically different?

    Assumes the provided margins of error were generated at the Census Bureau's standard 90% confidence level.

    Args:
        pair_one (list): A two-item list with a U.S. Census bureau estimate and its margin of error
        pair_two (list): Another two-item list with a U.S. Census bureau estimate and its margin of error

    Returns:
        The answer to the question: Are the values statistically different? (boolean).

        True

    Examples:
        >>> is_statistically_different((37.9, 0.1), (38.4, 0.1))
        True
    """
    return statistical_difference(pair_one, pair_two) > 1.0


def aggregate_counts(pairs):
    """
    Computes a derived estimate and its MOE for the aggregation of all
    the arguments.

    Args:
        pairs (list): a list of two-item sequences with a U.S. Census bureau
            count estimate and its margin of error.

    Returns:
        A two-item sequence containing the aggregated estimate and its MOE.

    Examples:
        >>> aggregate_counts([(379, 1), (384, 1)])
        (763, 1.4142135623730953)

    """
    estimate = 0
    squared_moe = 0

    # Pull out the values
    for (value, moe) in pairs:
        estimate += value
        squared_moe += moe**2

    return (estimate, math.sqrt(squared_moe))


def calculate_proportion(numerator_pair, denominator_pair):
    """
    Computes a derived estimate and its MOE for the proportion between
    the numerator and denominator arguments where the numerator
    represents a subset of the denominator.

    Args:
        numerator (list): a two-item sequence with a U.S. Census
            bureau estimate and its margin of error.

        denominator (list): a two-item sequence with a U.S. Census
            bureau estimate and its margin of error.

    Returns:
        A two-item sequence containing the calculated estimate and its MOE.

    Examples:
        >>> calculate_proportion((379, 1), (384, 1))
        (0.9869791666666666, 0.02046644492870734)

    """
    # Pull out the values
    numerator_estimate, numerator_moe = numerator_pair
    denominator_estimate, denominator_moe = denominator_pair

    # Calculate the proportion
    proportion_estimate = numerator_estimate / denominator_estimate

    # Calculate the proportion MOE
    squared_proportion_moe = (
        numerator_moe**2 - proportion_estimate**2 * denominator_moe**2
    ) / denominator_estimate

    return (proportion_estimate, math.sqrt(squared_proportion_moe))


def calculate_ratio(numerator_pair, denominator_pair):
    """
    Computes a derived estimate and its MOE for the ratio between
    the numerator and denominator arguments where the numerator
    does not represent a subset of the denominator.

    Args:
        numerator (list): a two-item sequence with a U.S. Census
            bureau estimate and its margin of error.

        denominator (list): a two-item sequence with a U.S. Census
            bureau estimate and its margin of error.

    Returns:
        A two-item sequence containing the calculated estimate and its MOE.

    Examples:
        >>> calculate_ratio((379, 1), (384, 1))
        (0.9869791666666666, 0.0604892511542549)
    """
    # Pull out the values
    numerator_estimate, numerator_moe = numerator_pair
    denominator_estimate, denominator_moe = denominator_pair

    # Calculate the ratio
    ratio_estimate = numerator_estimate / denominator_estimate

    # Calculate the ratio MOE
    squared_ratio_moe = (
        numerator_moe**2 + ratio_estimate**2 * denominator_moe**2
    ) / denominator_estimate

    return (ratio_estimate, math.sqrt(squared_ratio_moe))


def calculate_product(pair_one, pair_two):
    """
    Computes a derived estimate and its MOE for the product between
    the arguments.

    Args:
        pair_one (list): a two-item sequence with a U.S. Census
            bureau estimate and its margin of error.

        pair_two (list): a two-item sequence with a U.S. Census
            bureau estimate and its margin of error.

    Returns:
        A two-item sequence containing the calculated estimate and its MOE.

    Examples:
        >>> calculate_product((384, 1), (0.987, 0.06))
        (379.008, 23.061131130107213)
    
    """
    # Pull out the values
    estimate_one, moe_one = pair_one
    estimate_two, moe_two = pair_two

    # Calculate the product
    product_estimate = estimate_one * estimate_two

    # Calculate the product MOE
    squared_product_moe = (estimate_one**2 * moe_two**2
                           + estimate_two**2 * moe_one**2)

    return (product_estimate, math.sqrt(squared_product_moe))
