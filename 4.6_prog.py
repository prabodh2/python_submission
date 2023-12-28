class LU:
    def __init__(self, lu_code):
        self.lu_code = lu_code

    def display_lu_info(self):
        print(f"LU Code: {self.lu_code}")

class ITM:
    def __init__(self, itm_code):
        self.itm_code = itm_code

    def display_itm_info(self):
        print(f"ITM Code: {self.itm_code}")

# Derived class with multiple inheritance
class DerivedClass(LU, ITM):
    def __init__(self, lu_code, itm_code, derived_info):
        # Calling the constructors of both base classes
        LU.__init__(self, lu_code)
        ITM.__init__(self, itm_code)

        # Additional information specific to the derived class
        self.derived_info = derived_info

    def display_derived_info(self):
        print(f"Derived Info: {self.derived_info}")

# Example usage:
def main():
    # Create an object of the derived class
    derived_object = DerivedClass(lu_code="LU123", itm_code="ITM456", derived_info="Additional Info")

    # Access methods from both base classes
    derived_object.display_lu_info()
    derived_object.display_itm_info()

    # Access method from the derived class
    derived_object.display_derived_info()

if __name__ == "__main__":
    main()
