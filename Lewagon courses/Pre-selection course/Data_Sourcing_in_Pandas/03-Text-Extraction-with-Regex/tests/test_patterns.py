import re
from nbresult import ChallengeResultTestCase


class TestPatterns(ChallengeResultTestCase):

    TEXT_TO_SEARCH = """
Receipt Number 102790 ||| 02-01-2017
------------------------------------

Quantity                         163
Total Amount               3097.00 €
====================================
************************************
Receipt Number 102862 ||| 05-01-2017
------------------------------------

Quantity                         110
Total Amount                935.00 €
====================================
************************************
Receipt Number 103086 ||| 23-01-2017
------------------------------------

Quantity                         156
Total Amount               2808.00 €
        """

    def test_zip_code_pattern(self):
        zip_code_pattern = self.result.zipcode_re
        text_to_search = """13000 is the zip code of Marseille,
            Le Wagon Bdx is located in Bordeaux 33000, France
            city:Lyon,  zip: 69000"""
        zipcodes = re.findall(zip_code_pattern, text_to_search)
        self.assertEqual(zipcodes, ['13000', '33000', '69000'])

    def test_date_pattern(self):
        date_pattern = self.result.date_re
        text_to_search = """
            She was born on the 07-04-1983
            05-05-1986: message sent
            Date: 26-05-2021, Location: Australia, Event: Total lunar eclipse
        """
        dates = re.findall(date_pattern, text_to_search)
        self.assertEqual(dates, ['07-04-1983', '05-05-1986', '26-05-2021'])

    def test_quantity_pattern(self):
        quantity_pattern = self.result.quantity_re
        quantities = re.findall(quantity_pattern, self.TEXT_TO_SEARCH)
        self.assertEqual(quantities, [
            "Quantity                         163",
            "Quantity                         110",
            "Quantity                         156"
        ])

    def test_amount_pattern(self):
        amount_pattern = self.result.amount_re
        amounts = re.findall(amount_pattern, self.TEXT_TO_SEARCH)
        self.assertEqual(amounts, [
            "Total Amount               3097.00 €",
            "Total Amount                935.00 €",
            "Total Amount               2808.00 €"
        ])

    def test_quantity_group_pattern(self):
        quantity_group_pattern = self.result.quantity_grp_re
        quantities = re.findall(quantity_group_pattern, self.TEXT_TO_SEARCH)
        self.assertEqual(quantities, ['163', '110', '156'])

    def test_amount_group_pattern(self):
        amount_group_pattern = self.result.amount_grp_re
        amounts = re.findall(amount_group_pattern, self.TEXT_TO_SEARCH)
        self.assertEqual(amounts, ['3097.00', '935.00', '2808.00'])
