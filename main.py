from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

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

# MongoDB connection setup
client = MongoClient("mongodb+srv://admin:admin@cluster0.mryc9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Adjust the URI as needed
db = client["InventoryDB"]  # Replace with your database name
collection = db["Products"]  # Replace with your collection name

@app.get("/")
def read_root():
    # get all products from the database
    products = list(collection.find({}))
    return {"products": products}
