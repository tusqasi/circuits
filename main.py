from components import Battery, Resistor, Helpers


def main():
    b = Battery(10)
    r2 = Resistor(2)
    r1 = Resistor(1, r2)
    b.next_component = r1
    r2.next_component = b
    print(Helpers.current_drawn(b))


if __name__ == "__main__":
    main()
