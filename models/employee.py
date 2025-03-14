from dataclasses import dataclass
from datetime import datetime

@dataclass
class Employee:
    employee_id: int
    full_name: str
    email: str
    phone: str
    address: str
    dob: datetime
    position: str
    branch_id: int
    user_id: int
    