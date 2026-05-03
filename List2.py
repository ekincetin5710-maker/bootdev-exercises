def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")



    for i in range(0, len(inventory)):
                                                                  #not using i in loop because inventory gets shorter as loop goes on and i becomes out of range,
                                                                  #popping last item each time instead
        item = inventory.pop()
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()
