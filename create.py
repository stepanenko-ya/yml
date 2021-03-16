import pymssql

conn = pymssql.connect(
    server="10.175.1.60:1433",
    user="importer_doc",
    password='QAZxsw123',
    database="Test",
    charset='UTF-8')

db = conn.cursor()


def creating():

    db.execute("create table yml.categories (TransactionID int IDENTITY (1,1) NOT NULL, id_category NVARCHAR (30), name_category NVARCHAR (130))")
    conn.commit()


    db.execute("create table yml.items (TransactionID int IDENTITY(1,1) NOT NULL, CONSTRAINT PK_items_TransactionID PRIMARY KEY CLUSTERED (TransactionID), offer_number NVARCHAR (130), name_offer NVARCHAR (130), category_offer NVARCHAR (130), vendor_code NVARCHAR (130), vendor NVARCHAR (130),barcode NVARCHAR (130), url NVARCHAR (330), description ntext)")
    conn.commit()



    # db.execute("create table yml.picture (picture NVARCHAR (130), item_id_FK int FOREIGN KEY REFERENCES yml.items(TransactionID))")      # создание таблицы через foreing key#
    # conn.commit()


    db.execute("create table yml.picture (TransactionID int IDENTITY(1,1) NOT NULL, offer_number NVARCHAR (130), picture NVARCHAR(130) )")
    conn.commit()

    db.execute("create table yml.params (TransactionID int IDENTITY(1,1) NOT NULL, offer_number NVARCHAR (130), param_name NVARCHAR(130), param_value NVARCHAR(130))")
    conn.commit()


