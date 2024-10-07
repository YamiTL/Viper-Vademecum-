from update_quality import Item, update_quality
from update_quality import BACKSTAGE


def test_backstage_increases_quality_neg1():
    item = Item(BACKSTAGE, -1, -1)
    update_quality([item])
    assert 0 == item.quality


def test_backstage_increase_quality_10_days_left():
    item = Item(BACKSTAGE, 10, 25)
    update_quality([item])
    assert 27 == item.quality
    assert 9 == item.sell_in


def test_backstage_increase_quality_1_day_left():
    item = Item(BACKSTAGE, 1, 1)
    update_quality([item])
    assert 4 == item.quality
    assert 0 == item.sell_in


def test_backstage_increases_quality_49():
    item = Item(BACKSTAGE, 49, 47)
    update_quality([item])
    assert 48 == item.quality
    assert 48 == item.sell_in


def test_backstage_increases_quality_50():
    item = Item(BACKSTAGE, 50, 50)
    update_quality([item])
    assert 50 == item.quality
    assert 49 == item.sell_in
