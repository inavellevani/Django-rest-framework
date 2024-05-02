# Django REST API for Products and Categories
## This repository contains a Django project with a REST API for managing products and categories. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on products and categories.

<br>

## Features

• **List all available products and categories**
<br>
• **Create a new product or category**
<br>
• **Retrieve details of a specific product**
<br>
• **Update the stock of a product**
<br>
• **Delete a product**

<br>

## Getting Started
### Prerequisites

• **Python 3.x**
<br>
• **Django**
<br>
• **Django REST Framework**

<br>

## API Endpoints
### Products

• **GET /api/products/ - List all products**
<br>
• **POST /api/products/create/ - Create a new product**
<br>
• **GET /api/products/<int:pk>/ - Retrieve details of a specific product**
<br>
• **DELETE /api/products/<int:pk>/delete/ - Delete a product**
<br>
• **PATCH /api/products/<int:pk>/update/ - Update the stock of a product**

<br>

## Categories

• **GET /api/categories/ - List all categories**

<br>

## Django Admin
**You can access the Django admin interface at http://localhost:8000/admin/ to manage products and categories through a user-friendly interface. The superuser credentials created earlier will be required to log in.
Models**

<br>

## Category

• **name (CharField)**

<br>

## Product

• **category (ForeignKey to Category)**
<br>
• **name (CharField)**
<br>
• **price (DecimalField)**
<br>
• **stock (PositiveIntegerField)**

<br>

## Serializers
### The project includes the following serializers:

• **CategorySerializer: Serializes the Category model**
<br>
• **ProductSerializer: Serializes the Product model**
<br>
• **ProductListSerializer: Serializes the name and price fields of the Product model**
<br>
• **ProductUpdateSerializer: Serializes the stock field of the Product model**

<br>

## Views
### The project includes the following views:

• **ProductCreateView: Handles the creation of a new product**
<br>
• **ProductDetailView: Retrieves the details of a specific product**
<br>
• **ProductListView: Lists all available products**
<br>
• **ProductDeleteView: Deletes a product**
<br>
• **ProductUpdateView: Updates the stock of a product**
<br>
• **CategoryListView: Lists all available categories**
<br>
