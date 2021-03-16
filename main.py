from bs4 import BeautifulSoup
import pymssql
from create import creating

conn = pymssql.connect(
    server="10.175.1.60:1433",
    user="importer_doc",
    password='QAZxsw123',
    database="Test",
    charset='UTF-8')
db = conn.cursor()

def rewrite():
    infile = open('Tovary_c6f1b46c_a593_11ea_8215_ac162d75ecbb.yml', "r")
    content = infile.read()

    with open('example.html', 'w') as f:
        f.write(content)
    infile.close()


def categories():
    category = soup.find_all('category')
    for cat in category:
        id_category = cat.get('id')
        name_category = cat.getText()
        db.execute(f"insert into yml.categories values ('{id_category}', N'{name_category}')")
        conn.commit()


def parsing():

    all_offer = soup.find_all('offer')
    for offer in all_offer:
        offer_id = offer.get('id')
        name = offer.find('name').getText()
        category_offer = offer.find('categoryid').getText()
        vendor_code = offer.find('vendorcode').getText()
        vendor = offer.find('vendor').getText()
        barcode = offer.find('barcode').getText()
        url = offer.find('url').getText()
        description = (offer.find('description').getText().strip())

        db.execute(f"INSERT INTO  yml.items VALUES (N'{offer_id}', N'{name}', N'{category_offer}', N'{vendor_code}', N'{vendor}',N'{barcode}', N'{url}', N'{description}')")
        conn.commit()
    return all_offer


def picture():
    all_offer = soup.find_all('offer')
    for offer in all_offer:
        offer_id = offer.get('id')
        pictures = offer.find_all('picture')
        for picture in pictures:
            pict = picture.getText()
            # db.execute(f"insert into yml.picture(item_id_FK, picture) values ((select TransactionID from yml.items where N'{offer_id}' = N'7467e01a-871a-11e7-80ca-ac162d75ecb8'), N'{pict}')")
            # conn.commit()
            db.execute(f"insert into yml.picture values (N'{offer_id}', N'{pict}')")
            conn.commit()


def parametrs():

    all_offer = soup.find_all('offer')
    for offer in all_offer:
        offer_id = offer.get('id')
        params = offer.find_all('param')
        for param in params:

            param_name = param.get('name')
            param_value = (param.nextSibling).strip()
            db.execute(f"insert into yml.params values (N'{offer_id}', N'{param_name}', N'{param_value}')")
            conn.commit()


if __name__ == "__main__":
    creating()
    rewrite()
    infile = open('example.html', 'r')
    content = infile.read()
    soup = BeautifulSoup(content, 'html.parser')
    categories()
    parsing()
    picture()
    parametrs()
    infile.close()
