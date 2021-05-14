class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter Pin A input for gate " + self.get_label() + "--> "))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter Pin B input for gate " + self.get_label() + "--> "))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        elif self.pin_b == None:
            self.pin_b = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def get_pin(self):
        return int(input("Enter Pin input for gate " + self.get_label() + "--> "))

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fromgate, togate):
        self.fromgate = fromgate
        self.togate = togate

        togate.set_next_pin(self)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate


def main():
    g1 = AndGate("1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())


main()
