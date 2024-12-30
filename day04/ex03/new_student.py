import random
import string
from dataclasses import dataclass, field

# Function to generate a random ID
def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))

# Dataclass for Student
@dataclass
class Student:
    name: str
    surname: str
    active: bool = field(default=True, init=False)  # Set active to True by default, cannot be overridden in init
    login: str = field(init=False)  # Login is automatically generated and not provided by the user
    id: str = field(default_factory=generate_id, init=False)  # Randomly generated ID, cannot be set in init

    # Post-init method to automatically generate the login
    def __post_init__(self):
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"
