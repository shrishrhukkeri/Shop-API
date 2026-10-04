from shop import shipping


def test_light_parcels_use_the_first_tier():
    assert shipping.shipping_cost(0.5) == 4.99


def test_exactly_one_kilo_is_still_the_first_tier():
    assert shipping.shipping_cost(1.0) == 4.99


def test_exactly_five_kilos_is_still_the_second_tier():
    assert shipping.shipping_cost(5.0) == 8.99


def test_heavy_parcels_use_the_top_tier():
    assert shipping.shipping_cost(12.0) == 14.99


def test_express_adds_the_surcharge():
    assert shipping.shipping_cost(0.5, express=True) == 12.49
