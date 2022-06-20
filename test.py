import unittest

import census_error_analyzer


class CensusErrorAnalyzerTest(unittest.TestCase):
    def test_range(self):
        self.assertEqual(
            census_error_analyzer.statistical_range(37.9, 0.1), (37.8, 38.0)
        )

    def test_conversions(self):
        self.assertEqual(
            census_error_analyzer.convert_to_95_percent_confidence(3778),
            4501.446808510638,
        )
        self.assertEqual(
            census_error_analyzer.convert_to_99_percent_confidence(3778),
            5925.373860182372,
        )

    def test_difference(self):
        self.assertEqual(
            census_error_analyzer.statistical_difference((37.9, 0.1), (38.4, 0.1)),
            3.535533905932737,
        )
        self.assertTrue(
            census_error_analyzer.is_statistically_different((37.9, 0.1), (38.4, 0.1))
        )
        self.assertFalse(
            census_error_analyzer.is_statistically_different(
                (37284, 20922), (76850, 47200)
            )
        )


if __name__ == "__main__":
    unittest.main()
