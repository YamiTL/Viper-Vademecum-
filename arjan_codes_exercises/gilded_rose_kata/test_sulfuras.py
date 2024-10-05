from update_quality import Item, update_quality
from update_quality import SULFURAS

# Arjan recommends storing this product in a constant,
# so we make sure we wont mispell it by mistake


def test_sulfuras_maintains_quality_neg1():
    item = Item(SULFURAS, -1, quality=-1)
    update_quality([item])
    assert -1 == item.quality
    assert -1 == item.sell_in


def test_sulfuras_maintains_quality_0():
    item = Item(SULFURAS, 0, 0)
    update_quality([item])
    assert 0 == item.quality
    assert 0 == item.sell_in


def test_sulfuras_maintains_quality_49():
    item = Item(SULFURAS, 49, 49)
    update_quality([item])
    assert 49 == item.quality
    assert 49 == item.sell_in


def test_sulfuras_increases_quality_50():
    item = Item(SULFURAS, 50, 50)
    update_quality([item])
    assert 50 == item.quality
    assert 50 == item.sell_in
