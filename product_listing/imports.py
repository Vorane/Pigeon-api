from django.core.files import File
import os
import json

from categories.models import SubCategory, Category, CategorySubCategory
from store_listing.models import Store, Outlet
from .models import Product, SubCategoryProduct, Inventory


def get_productsjson(filepath):
    """convert json to products"""

    with open(filepath, "rb") as data:
        # array =  data = open(filepath, "r")

        data = json.loads(data.read())

        #loop through the data

        # Get the relevant Store
        for category in data:
            store = Store.objects.get(id=category["store"])

            # create a new category
            cat = Category()
            cat.name = category["name"]
            cat.display_name = category["name"]
            cat.color = category["color"]
            cat.store = store
            cat.save()

            # read all subcategories in the data
            for subcategory in category["subcategories"]:
                # create a new subcategory
                subcat = SubCategory()
                subcat.name = subcategory["name"]
                subcat.display_name = subcategory["name"]
                subcat.color = "#ffffff"
                subcat.store = store
                subcat.save()

                # create a mapping between category & subcategory
                new_cat_subcat = CategorySubCategory(
                    category=cat, sub_category=subcat)
                new_cat_subcat.save()

                #set the home path where the images are found
                home_path = os.environ.get('HOME_PATH')
                image_success = 0

                # loop through products and create mapping
                for product in subcategory["products"]:
                    # create the product
                    new_product = Product()
                    new_product.name = product["Name"]
                    new_product.display_name = product["Name"]
                    new_product.price = product["Price"]
                    new_product.size = str(
                        product["Size"]) + " " + product["Unit"]
                    new_product.brand = product["Brand"]
                    new_product.color = "#ffffff"

                    print(product["Name"])
                    try:
                        # import pdb
                        # pdb.set_trace()
                        new_product.thumbnail.save(
                            str(product["Image"] + '.png'),
                            File(
                                open(
                                    str(home_path + '/photos/' +
                                        product["Image"] + ".png"), 'rb')))
                        print("success")
                        image_success = image_success + 1
                    except Exception as e:
                        print("")
                    try:
                        new_product.thumbnail.save(
                            str(product["Image"] + '.jpg'),
                            File(
                                open(
                                    home_path + '/photos/' + product["Image"] +
                                    ".jpg", 'rb')))
                        print("success")
                        image_success = image_success + 1
                    except:
                        print("")
                    try:
                        new_product.thumbnail.save(
                            str(product["Image"] + '.jpeg'),
                            File(
                                open(
                                    home_path + '/photos/' + product["Image"] +
                                    ".jpeg", 'rb')))
                        print("success")
                        image_success = image_success + 1
                    except:
                        print("")
                    try:
                        new_product.thumbnail.save(
                            str(product["Image"] + '.JPG'),
                            File(
                                open(
                                    home_path + '/photos/' + product["Image"] +
                                    ".JPG", 'rb')))
                        print("success")
                        image_success = image_success + 1
                    except Exception as e:
                        print("")

                    new_product.save()

                    # create a mapping for the product and subcategory
                    new_subcategory_product = SubCategoryProduct(
                        sub_category=subcat, product=new_product)
                    new_subcategory_product.save()

                    # create a inventory instance for the product for all outlets
                    outlets = Outlet.objects.all().filter(store=store)
                    for outlet in outlets:
                        new_product_inventory = Inventory(
                            product=new_product, outlet=outlet)
                        new_product_inventory.save()

                print(
                    str("successfully uploaded images for " +
                        str(image_success) + " products in " +
                        subcategory["name"]))


def create_store_inventory(filepath, store_id):
    """convert json to products"""

    with open(filepath, "rb") as data:
        # array =  data = open(filepath, "r")

        data = json.loads(data.read())


        #loop through the categories
        for category in data:
            # Get the relevant Store
            store = Store.objects.get(id=store_id)

            # create a new category
            cat = Category()
            cat.name = category["name"]
            cat.display_name = category["name"]
            cat.color = category["color"]
            cat.store = store
            cat.save()

            # read all subcategories in the data
            for subcategory in category["subcategories"]:
                # create a new subcategory
                subcat = SubCategory()
                subcat.name = subcategory["name"]
                subcat.display_name = subcategory["name"]
                subcat.color = "#ffffff"
                subcat.store = store
                subcat.save()

                # create a mapping between category & subcategory
                new_cat_subcat = CategorySubCategory(
                    category=cat, sub_category=subcat)
                new_cat_subcat.save()

                # loop through products and create mapping
                for product in subcategory["products"]:
                    # try to find the product
                    found_product = Product.objects.filter(name=product["Name"]).first()
                    if found_product:
                        print (product["Name"])

                        # create a mapping for the product and subcategory
                        new_subcategory_product = SubCategoryProduct(
                            sub_category=subcat, product=found_product)
                        new_subcategory_product.save()

                        # create a inventory instance for the product for all outlets
                        outlets = Outlet.objects.all().filter(store=store)
                        for outlet in outlets:
                            new_product_inventory = Inventory(product=found_product, outlet=outlet)
                            new_product_inventory.save()


def update_productsjson():
    """Update product images where it is missing"""

    all_products = Product.objects.all()

    #set the home path where the images are found
    home_path = os.environ.get('HOME_PATH')
    image_success = 0

    for product in all_products:

        if not product.thumbnail:
            #extract the name of the product
            product_name = product.name
            product_name = product_name.replace(",", "")
            print(product_name)

            try:
                # import pdb
                # pdb.set_trace()
                product.thumbnail.save(
                    str(product_name + '.png'),
                    File(
                        open(
                            str(home_path + '/photos/' + product_name +
                                ".png"), 'rb')))
                print("success")
                image_success = image_success + 1
            except Exception as e:
                print("f")
            try:
                product.thumbnail.save(
                    str(product_name + '.jpg'),
                    File(
                        open(home_path + '/photos/' + product_name + ".jpg",
                             'rb')))
                print("success")
                image_success = image_success + 1
            except:
                print("f")
            try:
                product.thumbnail.save(
                    str(product_name + '.jpeg'),
                    File(
                        open(home_path + '/photos/' + product_name + ".jpeg",
                             'rb')))
                print("success")
                image_success = image_success + 1
            except:
                print("f")
            try:
                product.thumbnail.save(
                    str(product_name + '.JPG'),
                    File(
                        open(home_path + '/photos/' + product_name + ".JPG",
                             'rb')))
                print("success")
                image_success = image_success + 1
            except Exception as e:
                print("f")

            print(
                str("successfully uploaded images for " + str(image_success) +
                    " products"))
