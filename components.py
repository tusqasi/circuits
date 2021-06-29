from typing import Union
from time import sleep

"""Defines some electrical components
"""


class Components:
    def __init__(
        self,
        voltage: None,
        resistance: None,
        next_component=None,
        previous_component=None,
    ):

        self.resistance = resistance
        self.voltage = voltage

        if next_component is not None:
            self.next_component = next_component
        if previous_component is not None:
            self.previous_component = previous_component


class Resistor(Components):
    """Defines a resistor"""

    def __init__(
        self,
        resistance: float = 0,
        voltage=None,
        next_component=None,
        previous_component=None,
    ):
        Components.__init__(
            self,
            resistance=resistance,
            voltage=None,
            next_component=next_component,
            previous_component=previous_component,
        )

    def voltage_across_resistor(self):
        """Calculate voltage across the given resistor"""
        current_flowing_in_resistor = self.get_current_drawn()
        return current_flowing_in_resistor * self.resistance

    def get_current_drawn(self):
        """Get the current_drawn from the battery"""

        curr_component = self
        while curr_component.voltage == None:
            curr_component = curr_component.next_component
        return curr_component.calculate_total_current_drawn()

    def __str__(self):
        return f"Resistance: {self.resistance}"


class Battery(Components):
    """Defines a battery"""

    def __init__(
        self,
        voltage: float = 0,
        next_component=None,
        previous_component=None,
    ):
        Components.__init__(
            self,
            voltage=voltage,
            resistance=None,
            next_component=next_component,
            previous_component=previous_component,
        )

    def calculate_total_current_drawn(self) -> float:
        """Calculate total current_drawn in circuit (only linear)"""

        curr_component = self.next_component
        net_resistance = 0
        while curr_component != self:
            if curr_component.resistance is not None:
                net_resistance += curr_component.resistance
                curr_component = curr_component.next_component
        current_drawn = self.voltage / net_resistance
        return current_drawn

    def __str__(self):
        return f"Battery voltage: {self.voltage}"


if __name__ == "__main__":
    b = Battery(100)
    r2 = Resistor(2)
    r1 = Resistor(1)

    b.next_component = r1
    r1.next_component = r2
    r2.next_component = b
    print(r2.get_current_drawn())
    print(r1)
    print(f"{r1.voltage_across_resistor()}")
    print(f"{r2.voltage_across_resistor()}")
