import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    return inventory

# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)

def test_suite():
    test("strawberries" in new_inventory)
    test(new_inventory["strawberries"] == 10)
    add_fruit(new_inventory, "strawberries", 25)
    test(new_inventory["strawberries"] == 35)

test_suite()