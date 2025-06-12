# CustomerSupplier.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any

class CustomerSupplier(BaseModel):
    id: Optional[str] = Field(None, description="Unique identifier for the customer or supplier")
    name: str = Field(..., description="Name of the customer or supplier")
    email: Optional[EmailStr] = Field(None, description="Email address of the customer or supplier")
    phone: Optional[str] = Field(None, description="Phone number of the customer or supplier")
    address: Optional[str] = Field(None, description="Physical address of the customer or supplier")
    is_supplier: bool = Field(False, description="Flag indicating if the entity is a supplier (True) or a customer (False)")
    is_active: bool = Field(True, description="Flag indicating if the customer or supplier is active")
    is_customer: bool = Field(False, description="Flag indicating if the entity is a customer (True) or a supplier (False)")
    notes: Optional[str] = Field(None, description="Additional notes about the customer or supplier")