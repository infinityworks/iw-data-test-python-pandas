import argparse
import glob
import json

import pandas.io.parsers


def read_csv(csv_location: str):
    return pandas.read_csv(csv_location, header=0)


def read_json_folder(json_folder: str):
    transactions_files = glob.glob("{}*/*.json".format(json_folder))

    return pandas.concat(pandas.read_json(tf, lines=True) for tf in transactions_files)


def run_transformations(customers_location: str, products_location: str,
                        transactions_location: str, output_location: str):
    customers_df = read_csv(customers_location)
    products_df = read_csv(products_location)
    transactions_df = read_json_folder(transactions_location)

    return get_latest_transaction_date(transactions_df)


def get_latest_transaction_date(transactions):
    latest_purchase = transactions.date_of_purchase.max()
    latest_transaction = transactions[transactions.date_of_purchase == latest_purchase]
    return latest_transaction


def to_canonical_date_str(date_to_transform):
    return date_to_transform.strftime('%Y-%m-%d')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='IWDataTest')
    parser.add_argument('--customers_location', required=False, default="../input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="../input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="../input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="../output_data/outputs/")
    args = vars(parser.parse_args())

    run_transformations(args['customers_location'], args['products_location'],
                        args['transactions_location'], args['output_location'])
