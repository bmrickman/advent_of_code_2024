from collections import defaultdict

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


print(
    sum(
        int(middle_page(page_order))
        for page_order in page_orders
        if is_valid_page_ordering(page_order)
    )
)
