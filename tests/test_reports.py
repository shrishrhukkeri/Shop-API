from shop import reports


def test_average_of_two_orders():
    assert reports.average_order_value([10.0, 20.0]) == 15.0


def test_average_of_no_orders_is_zero():
    assert reports.average_order_value([]) == 0.0


def test_busiest_day_is_the_one_with_most_orders():
    assert reports.busiest_day({"mon": 3, "tue": 9}) == "tue"


def test_no_data_means_no_busiest_day():
    assert reports.busiest_day({}) == ""
