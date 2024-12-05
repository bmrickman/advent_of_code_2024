from collections import defaultdict
from copy import copy

with open("./day5/input.txt", "r") as f:
    data = f.read().splitlines()
# get split between two types of data
splitpoint = [i for i in range(len(data)) if data[i] == ""][0]
# parse the page order data
page_orders = data[splitpoint + 1 :]
page_orders = [order.split(",") for order in page_orders]
# create order rules dict
_order_rules = data[:splitpoint]
_order_rules = [rule.split("|") for rule in _order_rules]
order_rules = defaultdict(lambda: [])
for l, r in _order_rules:
    order_rules[l].append(r)


def is_valid_page_ordering(page_order: list[str]):
    for i, page in enumerate(page_order):
        u = set(order_rules[page]).intersection(set(page_order[:i]))
        if len(u) != 0:
            return False
    return True


def middle_page(page_order: list[str]):
    i = int((len(page_order) - 1) / 2)
    return page_order[i]


def reorder(page_order: list[str]):
    page_order = copy(page_order)
    for i in range(len(page_order)):  # list is properly sorted up to i
        for j in reversed(range(i)):
            # if we can swap j with j+1 without breaking rules, do it
            if page_order[j + 1] not in order_rules[page_order[j]]:
                cache = page_order[j]
                page_order[j] = page_order[j + 1]
                page_order[j + 1] = cache
    return page_order


print(
    sum(
        int(middle_page(reorder(page_order)))
        for page_order in page_orders
        if not is_valid_page_ordering(page_order)
    )
)
