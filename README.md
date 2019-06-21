# census-error-analyzer

Tools for analyzing the margin of error in data published by the U.S. Census Bureau

### Features

* Statistical difference tests
* Alternative confidence level conversion

### Installation

```bash
$ pipenv install census-error-analyzer
```

### Usage

Import the library.

```python
>>> import census_error_analyzer
```

#### Test statistical difference

Returns `True` or `False` whether two values, considering their respective margins of error, are statistically different. The Census Bureau advises that this test be conducted for all comparisons.

Accepts two lists, each expected to be a pair with the value first and the margin of error second.

```python
>>> us_medianage, us_medianage_moe = 37.9, 0.1
>>> nyc_medianage, nyc_medianage_moe = 38.4, 0.1
>>> census_error_analyzer.is_statistically_different(
    (us_medianage, us_medianage_moe),
    (nyc_medianage, nyc_medianage_moe)
)
True
```

The precise difference can also be accessed. According to the Census Bureau, values greater than 1.0 can be considered to be statistically significant.

```python
>>> census_error_analyzer.statistical_difference(
    (us_medianage, us_medianage_moe),
    (nyc_medianage, nyc_medianage_moe)
)
3.535533905932737
```

#### Get statistical range

Returns the minimum and maximum values in the statistical range for an estimate given its margin of error. Expects two arguments: The estimate first. The margin of error second.

```python
>>> census_error_analyzer.statistical_range(us_medianage, us_medianage_moe)
(37.8, 38.0)
```

#### Convert to alternative confidence levels

The margins of error published by the Census are at the 90% confidence level. They can be converted to the 95% and 99% levels using the following methods:

```python
>>> census_error_analyzer.convert_to_95_percent_confidence(3778)
4501.446808510638
>>> census_error_analyzer.convert_to_99_percent_confidence(3778)
5925.373860182372
```

### References

This module was designed to conform with the Census Bureau's April 18, 2018, presentation ["Using American Community Survey Estimates and Margin of Error."](https://www.documentcloud.org/documents/6162551-20180418-MOE.html)
