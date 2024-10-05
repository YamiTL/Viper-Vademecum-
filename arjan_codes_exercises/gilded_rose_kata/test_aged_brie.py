from update_quality import Item, update_quality
from update_quality import AGED_BRIE

# Arjan recommends storing this product in a constant,
# so we make sure we wont mispell it by mistake


def test_aged_brie_increases_quality_neg1():
    item = Item(AGED_BRIE, -1, -1)
    update_quality([item])
    assert 1 == item.quality


def test_aged_brie_increases_quality_49():
    item = Item(AGED_BRIE, 49, 49)
    update_quality([item])
    assert 50 == item.quality


def test_aged_brie_increases_quality_50():
    item = Item(AGED_BRIE, 50, 50)
    update_quality([item])
    assert 50 == item.quality
