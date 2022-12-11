import requests
import time
import csv
from bs4 import BeautifulSoup
import wget
import os
import shutil

# http://localhost/img/testowy/1.jpg


number_of_products = 0
product_number = 1


def getProductInfo(url, category):
    global product_number
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    attributes = {}

    name = soup.find("div", {"class": "product-title"}).text.replace("\n", "")

    for attr in soup.findAll("tr", {"class": "item-row"}):
        vals = attr.findAll("td")
        key = vals[0].text.replace("\n", "").replace("\t", "").replace(":", "")
        value = vals[1].text.replace("\n", "").replace("\t", "").replace("'", "")
        if "Zalety produktu" not in vals[0].text:
            if "Cena" in vals[0].text:
                value = value.split(".")[0]
            attributes[key] = value

    images_links = [soup.find("img", {"alt": name})["src"]]
    preview_images_links = soup.findAll("a", {"class": "thumb-image js-init-gallery"})

    for img in preview_images_links:
        images_links.append(img["data-src-large"])

    image_id = 1
    images = ""
    # Deleting images from localhost src_img folder
    if os.path.exists(f"/home/kuba/Documents/GitHub/Prestashop/src/src_img/{product_number}"):
        shutil.rmtree(f"/home/kuba/Documents/GitHub/Prestashop/src/src_img/{product_number}", ignore_errors=True)
    os.mkdir(f"/home/kuba/Documents/GitHub/Prestashop/src/src_img/{product_number}")
    for image in images_links:
        # Downloading images from leroymerlin server to localhost
        image_name = f"/home/kuba/Documents/GitHub/Prestashop/src/src_img/{product_number}/{image_id}.jpg"
        wget.download(image, image_name)
        images += f"http://localhost/src_img/{product_number}/{image_id}.jpg>"
        image_id += 1
    images = images[:-1]

    find = soup.find("span", {"class": "description"})
    description = ""
    if find is not None:
        description = find.text.replace("\n", "").replace("\t", "")

    reference = soup.find("span" ,{"id": "refNumber"}).text

    tax_found_text = soup.find("div", {"class": "product-vat"}).text
    tax_ID = ""
    if "23%" in tax_found_text:
        tax_ID = "1"
    elif "8%" in tax_found_text:
        tax_ID = "2"
    elif "5%" in tax_found_text:
        tax_ID = "3"

    info = {
        "id": product_number,
        "name": name.replace("\t", ""),
        "reference": reference,
        "category": category + ">Produkty>Oświetlenie",
        "description": description,
        "attributes": attributes,
        "img": "".join(images),
        "tax_ID": tax_ID
    }
    product_number += 1
    return info


def getAllProducts(led_links, lamp_links):
    products = {}
    base_url = "https://www.leroymerlin.pl"
    for link in led_links:
        products[link.split(',')[-2]] = getProductInfo(base_url + link, "Ledy")
        if len(products) % 10 == 0:
            time.sleep(1)
    for link in lamp_links:
        products[link.split(',')[-2]] = getProductInfo(base_url + link, "Lampy")
        if len(products) % 10 == 0:
            time.sleep(1)

    return products


def getLinks(name):
    global number_of_products
    page = 1
    links = []

    while number_of_products <= 500:
        urls = {
            "Ledy": f"https://www.leroymerlin.pl/oswietlenie/tasmy-led-profile-zasilacze,a1185,strona-{page}.html",
            "Lampy": f"https://www.leroymerlin.pl/oswietlenie/oswietlenie-scienne-i-sufitowe/zyrandole-lampy-wiszace-i-sufitowe,a956,strona-{page}.html"
        }
        soup = BeautifulSoup(requests.get(urls[name]).text, "html.parser")
        links_on_page = [div.find('a')['href'] for div in soup.find_all("div", {"class": "product"})]
        number_of_products += len(links_on_page)
        links.extend(links_on_page)
        page += 1
        if len(soup.find_all("a", {"class": "next disabled"})) != 0:
            break
    return links


def makeProductCSV():
    csv_columns = ['ID', 'Name', "Reference", 'Categories', 'Price', 'Short desc.', 'Features', 'Images URL', 'Quantity', "Tax ID"]

    led_links = getLinks('Ledy')
    lamp_links = getLinks('Lampy')
    if '#' in lamp_links:
        lamp_links.remove('#')

    all_products_info = {"products": getAllProducts(led_links, lamp_links)}

    with open("products.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns, delimiter=';')
        writer.writeheader()
        for data in all_products_info["products"]:
            writer.writerow({
                "ID": all_products_info["products"][data]["id"],
                "Name": all_products_info["products"][data]["name"],
                "Reference": all_products_info["products"][data]["reference"],
                "Categories": all_products_info["products"][data]["category"],
                "Price": all_products_info["products"][data]["attributes"]["Cena"].split("/")[0].replace("zł", ""),
                "Short desc.": all_products_info["products"][data]["description"],
                "Features": str(all_products_info["products"][data]["attributes"]).replace("{", "").replace("}",
                                                                                    "").replace(", ", '>').replace("'", ""),
                "Images URL": str(all_products_info["products"][data]["img"]).replace("{", "").replace("}", ""),
                "Quantity": "50",
                "Tax ID": all_products_info["products"][data]["tax_ID"]
            })


def makeCategoryCSV():
    csv_columns = ["ID", "Name", "Parent category"]
    with open("categories.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns, delimiter=';')
        writer.writeheader()
        writer.writerow({
            "ID": "2",
            "Name": "Oświetlenie",
            "Parent category": "Produkty"
        })
        writer.writerow({
            "ID": "3",
            "Name": "Ledy",
            "Parent category": "Oświetlenie"
        })
        writer.writerow({
            "ID": "4",
            "Name": "Lampy",
            "Parent category": "Oświetlenie"
        })


def makeCombinationsCSV():
    csv_columns = ["Product ID", "Attribute (Name:Type)", "Value", "Default (0 = No, 1 = Yes)", "Quantity"]
    with open("combinations.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns, delimiter=";")
        writer.writeheader()
        writer.writerow({
            "Product ID": "1",
            "Attribute (Name:Type)": "Długość:select:0",
            "Value": "5m:0",
            "Default (0 = No, 1 = Yes)": "0",
            "Quantity": "50"
        })
        writer.writerow({
            "Product ID": "1",
            "Attribute (Name:Type)": "Długość:select:0",
            "Value": "2m:0",
            "Default (0 = No, 1 = Yes)": "1",
            "Quantity": "50"
        })


makeProductCSV()

makeCategoryCSV()

makeCombinationsCSV()


