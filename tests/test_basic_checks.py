import pandas as pd

def test_row_count():
    source = pd.read_csv("data/source_system_a.csv")
    target = pd.read_csv("data/target_system_b.csv")
    assert len(source) == len(target)

def test_no_null_customer_id():
    target = pd.read_csv("data/target_system_b.csv")
    assert target["customer_id"].isnull().sum() == 0

def test_no_duplicate_order_id():
    target = pd.read_csv("data/target_system_b.csv")
    assert target["order_id"].duplicated().sum() == 0
