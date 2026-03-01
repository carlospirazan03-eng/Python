from flask import Blueprint, render_template, request, redirect, url_for
from models.product_model import db, Product

product_bp = Blueprint("product", __name__)

# LIST
@product_bp.route("/")
def list_products():
    products = Product.query.all()
    return render_template("product_list.html", products=products)

# CREATE FORM
@product_bp.route("/create")
def create_form():
    return render_template("product_create.html")

# CREATE
@product_bp.route("/create", methods=["POST"])
def create_product():
    name = request.form["name"]
    price = request.form["price"]
    description = request.form["description"]

    product = Product(name=name, price=price, description=description)
    db.session.add(product)
    db.session.commit()

    return redirect(url_for("product.list_products"))

# EDIT FORM
@product_bp.route("/edit/<int:id>")
def edit_form(id):
    product = Product.query.get_or_404(id)
    return render_template("product_edit.html", product=product)

# UPDATE
@product_bp.route("/edit/<int:id>", methods=["POST"])
def update_product(id):
    product = Product.query.get_or_404(id)

    product.name = request.form["name"]
    product.price = request.form["price"]
    product.description = request.form["description"]

    db.session.commit()
    return redirect(url_for("product.list_products"))

# DELETE
@product_bp.route("/delete/<int:id>")
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for("product.list_products"))