from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from routers import CustomerSupplier_router as CustomerSupplier

app = FastAPI(swagger_ui_parameters={"syntaxHighlight" : False})  # Disable syntax highlighting in Swagger UI

# add swagger documentation
app.title = "Inventory Management API"
app.description = "API for managing inventory products."
app.version = "1.0.0"

# add swagger UI configuration
app.docs_url = "/docs"  # Swagger UI endpoint
app.redoc_url = "/redoc"  # ReDoc UI endpoint

# Allow CORS for all origins (frontend access from anywhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(CustomerSupplier.router)