from item import Item
from update_quality import update_quality


def test_common_item_decreases():
    item = Item("Common item", 10, 10)
    update_quality(items=[item])
    assert 9 == item.quality
    assert 9 == item.sell_in
