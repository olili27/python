from kisa_utils.db import Api
from kisa_utils import config, dates, codes
from database import insert_data
import json



# config.setValue("topic/there", "here")
# config.setValue("topic/two", "2")
# value = config.getValue("topic/there")
# value2 = config.getValue("topic/two")
# topic = config.getTopic("topic")

# config.init()
# print(config.getConfigPath())




# db.fetch("users", ["*"], "first_name?", "timothy", limit=2)


def init():
    defaults = {
        "root_path": "/tmp/e-visitors",
        "tables": {
            "visitors": """
                surname varchar(255) not null,
                given_name varchar(256) not null,
                nin varchar(256) not null unique,
                other json,
                timestamp varchar(256) not null
            """,
            "fingerprints": """
                print_id varchar(255) not null unique,
                nin varchar(255) not null,
                other json,
                timestamp varchar(32)
            """
        }
    }

    defaults["db_path"] = defaults["root_path"] + "/visitor.db"
    defaults["fingerprints_path"] = defaults["root_path"] + "/prints/all"

    topic = "e-visitors"

    for key in defaults:
        topic_key = topic + f"/{key}"

        # set key-values pairs in a config file
        if not config.getValue(topic_key):
            config.setValue(topic_key, defaults[key])

init()


if __name__ == "__main__":
# db_path = config.getValue("e-visitor/db_path")
# print(db_path)

    data = {
        "nin": "hghdjkjk",
        "surname":"bukenya",
        "given_name": "tom",
        "hand": "right",
        "finger": "middle",
        "fingerprint_url": f"/tmp/e-visitors/prints/all/{codes.new()}.png"
    }

    insert_data(data)

    db_path = config.getValue("visitor/db_path")
    tables = config.getValue("visitor/tables")

    other = {}
    timestamp = dates.currentTimestamp()

    visitor_data = {
        "surname": data["surname"],
        "given-name": data["given_name"],
        "nin": data["nin"],
        "other": json.dumps(other),
        "timestamp": timestamp
    }

    # with Api(db_path, tables, readonly=False) as db:
    #         print(db.insert("visitors", tuple(visitor_data.values())))
        
    # with Api(db_path, tables, readonly=True) as db:
    #         print(db.fetch("visitors", ["nin"], "nin=?", ["156567djhkjhfvjkkko39hiu"]))

    # with Api(config.getValue("e-visitor/db_path"), config.getValue("e-visitor/tables"), readonly=False) as db:
    #         print(db.update("users", ["first_name", "last_name"], ["tony",], "first_name=?", ["timothy"]))
    #         print(db.fetch("users", ["*"], "first_name=?", ["tony"]))


