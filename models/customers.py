from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Customer:
    customer_id: Optional[int]
    user_id: int
    full_name: str
    email: str      
    phone: str      
    address: str
    dob: str
    pan: str

    
    def __str__(self):
        return f"Customer ID: {self.customer_id}\nFull Name: {self.full_name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\nDOB: {self.dob}\nPAN: {self.pan}"