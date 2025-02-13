from kisa_utils import dates, config, codes
from kisa_utils.encryption import hash, encrypt, decrypt
from kisa_utils.db import Api
import kisa_utils as kutils
import json

def insert_data(data : dict) -> dict:
    """
        insert visitor data and fingerprint data into the visitors and fingerprints tables respectively

        @args `data`: dictionary that contains both the visitor data and fingerprint data e.g 
        {
            "nin": "hghdjkjk",
            "surname":"bukenya",
            "given_name": "tommy",
            "hand": "right",
            "finger": "middle",
            "fingerprint_url": "/tmp/e-visitors/prints/all/somecode.png"
        }

        returns a dictionary with "status" and "log" keys. "log" value is an error message if either visitor data or fingerprint data insertion fails else it is empty. e.g {"status": True, "log": ""}
    """

    db_path = config.getValue("e-visitors/db_path")
    tables = config.getValue("e-visitors/tables")

    visitor_data, fingerprint_data = extract_distinct_data(data).values()

    response = insert_visitor_data(visitor_data, db_path, tables)
    print("visitor status " , response["status"])

    if not response["status"]:
        return response
    
    response = insert_fingerprint_data(fingerprint_data, db_path, tables)
    print("fingerprint status " , response["status"])

    print("final: " ,response)
    return response


def extract_distinct_data(data : dict) -> dict:
    """
        separate visitor data from fingerprint data
        @args `data`: dictionary that contains both the visitor data and fingerprint data e.g 
        {
            "nin": "hghdjkjk",
            "surname":"bukenya",
            "given_name": "tommy",
            "hand": "right",
            "finger": "middle",
            "fingerprint_url": "/tmp/e-visitors/prints/all/somecode.png"
        }

        returns a dictionary with "visitor_data" and "fingerprint_data" keys. e.g {
            visitor_data : {
                "surname": "mukalazi",
                "given-name": "mark",
                "nin": "CMXce2674899ncv"
            },
            fingerprint_data = {
                "print_id": "sfhh735",
                "nin": "CMXce2674899ncv"
            }   
        }
    """

    # any other data about the visitor
    other_visitor_data = {}

    # first hand data about the visitor
    visitor_data = {
        "surname": encrypt(data["surname"]),
        "given-name": encrypt(data["given_name"]),
        "nin": hash(data["nin"]),
        "other": json.dumps(other_visitor_data),
        "timestamp": dates.currentTimestamp()
    }

    # any other data about the fingerprint
    other_fingerprint_data = {
        "hand": encrypt(data["hand"]),
        "finger": encrypt(data["finger"])
    }

    # first hand data about the fingerprint
    fingerprint_data = {
        "print_id": data["fingerprint_url"].split("/")[-1].split(".")[0],
        "nin": hash(data["nin"]),
        "other": json.dumps(other_fingerprint_data),
        "timestamp": dates.currentTimestamp(),
    }

    # response
    return {
        "visitor_data": visitor_data,
        "fingerprint_data": fingerprint_data
    }


def insert_visitor_data(visitor_data : dict, db_path : str, tables : dict) -> dict:
    """
        insert visitor data into visitors table 

        @args `visitor_data`: specific details about a visitor e.g surname, given name, nin
        @args `db_path`: path to the database
        @args `tables`: tables that the database contains

        returns a dictionary with "status" and "log" keys. "log" value is an error message if data insertion fails else it is empty. e.g {"status": True, "log": ""}
    """
    with Api(db_path, tables, readonly=False) as db:
        if is_record_already_present(db, "visitors", ["nin", "surname", "given_name"], "nin = ?", [visitor_data["nin"]]):
            return db.insert("visitors", [tuple(visitor_data.values())])

        return {"status": True, "log": ""}

def deleteFromDb(dbPath : str, tables : dict, table :str, condition : str, conditionData : list):
    with Api(dbPath, tables, readonly=False) as db:
        return db.delete(table, condition, conditionData)
    

def insert_fingerprint_data(fingerprint_data : dict, db_path : str, tables : dict) -> dict:
    """
        insert fingerprint data into fingerprints table

        @args `fingerprint_data`: specific details about a fingerprint e.g fingerprint thumbnail, hand, finger, timestamp
        @args `db_path`: path to the database
        @args `tables`: tables that the database contains

        returns a dictionary with "status" and "log" keys. "log" value is an error message if data insertion fails else it is empty. e.g {"status": True, "log": ""}
    """
    with Api(db_path, tables, readonly=False) as db: 
        return db.insert("fingerprints", [tuple(fingerprint_data.values())])

def is_record_already_present(database_instance : Api, table : str,columns_to_select : list, condition : str, condition_data : bool):
    """
        check if a record already exists in the database
       
        @args `database_instance`: instance of sqlite3 client
        @args `table`: table to which data is to be inserted
        @args `columns_to_select`: names of columns from which data is to be retrieved
        @args `condition`: specific condition that allows to retrieve only rows that meet certain criteria
        @args `condition_data`: values supplied to the condition in the query

        e.g is_record_already_present(database, "visitors_table", ["nin", "surname", "given_name"], "nin = ?", ["CMXc5992737MEy"]) 
        or 
        record_already_present(database, "visitors_table", ["nin", "surname", "given_name"], "nin = ? & surname = ?", ["CMXc5992737MEy", "Mukalazi"])

        returns a boolean i.e True or False
    """

    # check if returned list is empty -> no trace of the record queried
    return len(database_instance.fetch(table, columns_to_select, condition, condition_data, limit=1)) == 0

# cm7890765489789

if __name__ == '__main__':
    data = {
        "nin": 'cm7890765489789',
        "surname":"Magambo",
        "given_name": "isaac",
        "hand": "right",
        "finger": "thumb",
        "fingerprint_url": f"/tmp/e-visitors/prints/all/'{codes.new()}.png'"
    }

    db_path = config.getValue("e-visitors/db_path")
    tables = config.getValue("e-visitors/tables")
    # hNin  = hash(data["nin"])

    # insert_data(data)
    # print(deleteFromDb(db_path, tables, "visitors", "nin =? ", [hash(data["nin"])]))
    # print(deleteFromDb(db_path, tables, "fingerprints", "nin =? ", [hash(data["nin"])]))

    

    with Api(db_path, tables, readonly=True, bindingFunctions=[
        ('decrypt', 1, kutils.encryption.decrypt)
    ]) as db:
        condition =  'nin = ? and decrypt(json_extract(other, "$.hand")) = ? and decrypt(json_extract(other, "$.finger")) = ?'
        matching_rows = db.fetch(
            'fingerprints', ['print_id, other'], condition, [hash("cm7890765489789"), "right", "thumb"]
        )

        print(matching_rows)                                                                                                                                                            