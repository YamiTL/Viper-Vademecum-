from typing import Iterable
from item import Item


# Now I will create 1 function that execute/ collect all relevant
# quality increase and sellin changes for the Brie
def executes_quality_and_sellin_changes_aged_brie(item: Item):
    if item.quality < 50:
        item.quality = item.quality + 2
        item.sell_in = item.sell_in - 1


# Executes/ collects all relevant changes for BACKSTAGE PASSES
def executes_quality_and_sellin_changes_backstage(item: Item):
    if item.quality < 50:
        item.quality = item.quality + 3

    if item.sell_in < 6:
        item.quality = item.quality + 1 and item.sell_in - 1

    if item.sell_in < 0:
        item.quality = item.quality - item.quality


# Executes/ collects all relevant changes for COMMON ITEMS
def executes_quality_and_sellin_changes_common_items(item: Item):
    if item.quality > 0:
        item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1


# # Executes/ collects all relevant changes for COMMON ITEMS


def executes_quality_and_sellin_changes_conjured(item: Item):
    if item.quality > 0:
        item.quality = item.quality - 2
        item.sell_in = item.sell_in - 1


AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"


# This function emulates the passing of time.
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

        elif item.name == SULFURAS:
            continue

        elif item.name == BACKSTAGE:
            executes_quality_and_sellin_changes_backstage(item)

        elif item.name == "Common item":
            executes_quality_and_sellin_changes_common_items(item)

        elif item.name == "Conjured item":
            executes_quality_and_sellin_changes_conjured(item)


item = Item(BACKSTAGE, 5, 10)
update_quality([item])


# Me queda por:
# Terminar de armar el test de los items conjurados
# Agregar a los items conjurados a la funcion de update quality
