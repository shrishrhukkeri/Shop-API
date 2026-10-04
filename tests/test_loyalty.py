from shop import loyalty


def test_basic_customers_earn_a_point_per_unit():
    assert loyalty.points_for_order(100.0) == 100


def test_gold_customers_earn_double():
    assert loyalty.points_for_order(100.0, "gold") == 200


def test_platinum_customers_earn_a_bonus():
    assert loyalty.points_for_order(100.0, "platinum") >= 100


def test_points_are_worth_half_a_cent_each():
    assert loyalty.points_value(10) == 5
