from item import Item
from update_quality import update_quality


def test_conjured_item_decreases():
    item = Item("Conjured item", 10, 10)
    update_quality(items=[item])
    assert 8 == item.quality
    assert 9 == item.sell_in
