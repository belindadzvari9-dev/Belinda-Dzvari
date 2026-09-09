#3. Typed Data Descriptor
class Typed:
    def __init__(self, expected_type):
        # Store the required type, for example int or str.
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        # Create a private attribute name for storing the value.
        self.storage_name = "_" + name

    def __get__(self, instance, owner):
        # Return the descriptor itself when accessed through the class.
        if instance is None:
            return self

        # Return the stored value from the object.
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance, value):
        # Check that the assigned value has the correct type.
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Expected {self.expected_type.__name__}, got {type(value).__name__}"
            )

        # Store the valid value on the object.
        setattr(instance, self.storage_name, value)


class Student:
    name = Typed(str)
    age = Typed(int)


student = Student()
student.name = "Alice"
student.age = 25

print(student.name)
print(student.age)

# student.age = "twenty five"  # Raises: TypeError
