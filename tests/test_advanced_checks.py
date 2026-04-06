import pandas as pd

def test_country_values():
    target = pd.read_csv("data/target_system_b.csv")
    valid_countries = ["India", "United States"]

    for country in target["country"]:
        assert country in valid_countries

def test_sales_amount_positive():
    target = pd.read_csv("data/target_system_b.csv")
    assert (target["sales_amount"] > 0).all()

def test_date_format():
    target = pd.read_csv("data/target_system_b.csv")
    for date in target["order_date"]:
        assert "-" in date
