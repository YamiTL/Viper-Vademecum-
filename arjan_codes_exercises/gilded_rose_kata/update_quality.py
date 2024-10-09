from typing import Iterable
from item import Item

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"


# Now I will create 1 function to execute/ collect all relevant
# quality increase and sellin changes for the Brie
def executes_quality_and_sellin_changes_aged_brie(item: Item):
    if item.quality < 50:
        item.quality = item.quality + 2
        item.sell_in = item.sell_in - 1


# Executes/ collects all relevant changes for BACKSTAGE PASSES
def executes_quality_and_sellin_changes_backstage(item: Item):
    if item.sell_in < 0:
        print("Your passes are expired :(")
        item.quality = 0
        return

    if item.quality < 50:
        if item.sell_in <= 5:
            item.quality = item.quality + 3

        elif item.sell_in <= 10:
            item.quality = item.quality + 2

        else:
            item.quality = item.quality + 1

    item.sell_in = item.sell_in - 1


# Executes/ collects all relevant changes for COMMON ITEMS
def executes_quality_and_sellin_changes_common_items(item: Item):
    if item.quality > 0:
        item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1


# Executes/ collects all relevant changes for CONJURED ITEMS
def executes_quality_and_sellin_changes_conjured(item: Item):
    if item.quality > 0:
        item.quality = item.quality - 2
        item.sell_in = item.sell_in - 1


def update_quality(items: Iterable[Item]):
    # This for loop iterates item name and quality, the problems here are lack of
    # modularization and repetition of code.
    # How many types of items do we have? Can we find some sort of groups that
    # allow for breaking down this one function into 2 or 3?
    # Also consider applying this principle of getting the exception/odd one out
    # of the way first in the if loop, and then moving on to the broader cases.
    for item in items:
        if item.name == AGED_BRIE:
            executes_quality_and_sellin_changes_aged_brie(item)
            continue

        elif item.name == SULFURAS:
            continue

        elif item.name == BACKSTAGE:
            executes_quality_and_sellin_changes_backstage(item)
            continue

        elif "Conjured" in item.name:
            executes_quality_and_sellin_changes_conjured(item)

        else:
            executes_quality_and_sellin_changes_common_items(item)


item1 = Item("Pollito", 3, 6)
update_quality([item1])
print(item1)
