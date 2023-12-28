class Grandfather:
    def __init__(self, property_in_grandfather):
        self.property_in_grandfather = property_in_grandfather

    def display_grandfather_property(self):
        print(f"Property in Grandfather: {self.property_in_grandfather}")

class Father(Grandfather):
    def __init__(self, property_in_grandfather, property_in_father):
        # Call the constructor of the base class (Grandfather)
        super().__init__(property_in_grandfather)
        self.property_in_father = property_in_father

    def display_father_property(self):
        print(f"Property in Father: {self.property_in_father}")

class Child(Father):
    def __init__(self, property_in_grandfather, property_in_father, property_in_child):
        # Call the constructor of the immediate base class (Father)
        super().__init__(property_in_grandfather, property_in_father)
        self.property_in_child = property_in_child

    def display_child_property(self):
        print(f"Property in Child: {self.property_in_child}")

# Example usage:
def main():
    # Create an object of the Child class
    child_object = Child(property_in_grandfather="Grandfather's Property",
                         property_in_father="Father's Property",
                         property_in_child="Child's Property")

    # Access properties from all levels of inheritance
    child_object.display_grandfather_property()
    child_object.display_father_property()
    child_object.display_child_property()

if __name__ == "__main__":
    main()
