import unittest
import census_error_analyzer



class CensusErrorAnalyzerTest(unittest.TestCase):

    def test_range(self):
        self.assertEqual(
            census_error_analyzer.statistical_range(37.9, 0.1),
            (37.8, 38.0)
        )

    def test_conversions(self):
        self.assertEqual(
            census_error_analyzer.convert_to_95_percent_confidence(3778),
            4501.446808510638
        )
        self.assertEqual(
            census_error_analyzer.convert_to_99_percent_confidence(3778),
            5925.373860182372
        )

    def test_difference(self):
        self.assertEqual(
            census_error_analyzer.statistical_difference((37.9, 0.1), (38.4, 0.1)),
            3.535533905932737
        )
        self.assertTrue(census_error_analyzer.is_statistically_different((37.9, 0.1), (38.4, 0.1)))
        self.assertFalse(census_error_analyzer.is_statistically_different((37284, 20922), (76850, 47200)))

    def test_sum(self):
        estimate, moe = census_error_analyzer.calculate_sum((379, 1), (384, 1))
        self.assertAlmostEqual(estimate, 763)
        self.assertAlmostEqual(moe, 1.4142135623730951)

    def test_proportion(self):
        estimate, moe = census_error_analyzer.calculate_proportion((379, 1), (384, 1))
        self.assertAlmostEqual(estimate, 0.9869791666666666)
        self.assertAlmostEqual(moe, 0.008208247339752435)

    def test_ratio(self):
        estimate, moe = census_error_analyzer.calculate_ratio((379, 1), (384, 1))
        self.assertAlmostEqual(estimate, 0.9869791666666666)
        self.assertAlmostEqual(moe, 0.07170047425884142)

    def test_product(self):
        estimate, moe = census_error_analyzer.calculate_product((384, 1), (0.987, 0.06))
        self.assertAlmostEqual(estimate, 379.008)
        self.assertAlmostEqual(moe, 23.061131130107213)

if __name__ == '__main__':
    unittest.main()
