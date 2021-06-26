from typing import Union

"""Defines some electrical components
"""


class Resistor:
    """Defines a resistor"""

    def __init__(
        self,
        resistance: float,
        next_component=None,
        previous_component=None,
    ):
        self.resistance = resistance

        if next_component != None:
            self.next_component = next_component
        if previous_component != None:
            self.previous_component = previous_component


class Battery:
    def __init__(
        self,
        voltage: float,
        next_component=None,
        previous_component=None,
    ):
        self.voltage = voltage
        if next_component != None:
            self.next_component = next_component
        if previous_component != None:
            self.previous_component = previous_component


class Helpers:
    @staticmethod
    def calculate_current_drawn(component: Resistor) -> float:
        """Calculate total current_drawn in circuit (only linear and for resistance)."""
        _curr_component = component.next_component
        net_resistance = 0
        while _curr_component != component:
            if _curr_component.resistance != None:
                net_resistance += _curr_component.resistance
                _curr_component = _curr_component.next_component
        current_drawn = component.voltage / net_resistance
        return current_drawn

    def voltage_across_component(component: Resistor):
        """Calculate voltage across the given component"""

        current_drawn = Helpers.calculate_current_drawn(component)
        return current_drawn * component.resistance


if __name__ == "__main__":
    b = Battery(100)
    r2 = Resistor(2)
    r1 = Resistor(1, r2)
    b.next_component = r1
    r2.next_component = b
    print(f"{Helpers.calculate_current_drawn(r1)=}")
    print(f"{Helpers.voltage_across_component(r1)=}")
