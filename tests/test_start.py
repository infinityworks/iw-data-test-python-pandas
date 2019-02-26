from datetime import datetime
import pandas

from solution.solution_start import get_latest_transaction_date


class TestStart(object):

    def test_get_latest_transaction_date_returns_most_recent_date(self):
        transactions_df = pandas.concat(
            [
                pandas.read_json(
                    "{\"customer_id\": \"C6\", \"basket\": [{\"product_id\": \"P53\", \"price\": 476}, {\"product_id\": \"P42\", \"price\": 1937}, {\"product_id\": \"P43\", \"price\": 1019}], \"date_of_purchase\": \"2018-12-03 17:52:00\"}"),
                pandas.read_json(
                    "{\"customer_id\": \"C125\", \"basket\": [{\"product_id\": \"P28\", \"price\": 1752}], \"date_of_purchase\": \"2019-01-27 08:23:00\"}"),
                pandas.read_json(
                    "{\"customer_id\": \"C76\", \"basket\": [{\"product_id\": \"P39\", \"price\": 1033}], \"date_of_purchase\": \"2019-02-27 13:55:00\"}")
            ]
        )

        result = get_latest_transaction_date(transactions_df)
        assert result.date_of_purchase[0] == "2019-02-27 13:55:00"
