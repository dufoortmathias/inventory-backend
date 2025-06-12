from schemas.CustomerSupplier import CustomerSupplier
import json
import uuid
from fastapi import APIRouter, HTTPException, Depends, status
from pymongo import MongoClient

router = APIRouter(
    prefix="/customers_suppliers", 
    tags=["Customers and Suppliers"], 
    responses={404: {"CustomerSupplier": "Not found"}}
    )

mongo_client = MongoClient("mongodb+srv://admin:admin@cluster0.mryc9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongo_client["InventoryDB"]  # Replace with your database name
collection = db["CustomerSuppliers"]  # Replace with your collection name

@router.get("/", response_model=list[CustomerSupplier])
def get_customers_suppliers():
    """
    Get all customers and suppliers.
    """
    try:
        customers_suppliers = list(collection.find({}))
        return customers_suppliers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{id}", response_model=CustomerSupplier)
def get_customer_supplier(id: str):
    """
    Get a customer or supplier by ID.
    """
    try:
        customer_supplier = collection.find_one({"_id": id})
        if not customer_supplier:
            raise HTTPException(status_code=404, detail="Customer or Supplier not found")
        return customer_supplier
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/", response_model=CustomerSupplier, status_code=status.HTTP_201_CREATED)
def create_customer_supplier(customer_supplier: CustomerSupplier):
    """
    Create a new customer or supplier.
    """
    try:
        customer_supplier_dict = customer_supplier.dict()
        customer_supplier_dict["_id"] = str(uuid.uuid4())  # Generate a unique ID
        customer_supplier_dict["id"] = customer_supplier_dict["_id"]
        collection.insert_one(customer_supplier_dict)
        return customer_supplier_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/{id}", response_model=CustomerSupplier)
def update_customer_supplier(id: str, customer_supplier: CustomerSupplier):
    """
    Update an existing customer or supplier by ID.
    """
    try:
        customer_supplier_dict = customer_supplier.dict()
        result = collection.update_one({"_id": id}, {"$set": customer_supplier_dict})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Customer or Supplier not found")
        return customer_supplier_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer_supplier(id: str):
    """
    Delete a customer or supplier by ID.
    """
    try:
        result = collection.delete_one({"_id": id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Customer or Supplier not found")
        return {"detail": "Customer or Supplier deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))