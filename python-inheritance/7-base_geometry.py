class BaseGeometry:
    def area(self):
        """Method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value

        Args:
            name (str): name of the value
            value (int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
