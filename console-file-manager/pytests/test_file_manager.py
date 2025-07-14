from games.victory import get_date
def test_get_date():
    assert get_date('12.05.1794') == '12 мая 1794'
    assert get_date('1.02.1851') == '1 февраля 1851'
    assert get_date('29.10.1943') == '29 октября 1943'
