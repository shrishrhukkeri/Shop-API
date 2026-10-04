from shop import validators


def test_valid_sku():
    assert validators.is_valid_sku("ABC-1234")


def test_lowercase_sku_is_rejected():
    assert not validators.is_valid_sku("abc-1234")


def test_valid_email():
    assert validators.is_valid_email("sam@example.com")


def test_email_without_domain_is_rejected():
    assert not validators.is_valid_email("sam@")
