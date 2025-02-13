from kisa_utils.db import Api
from kisa_utils import config, dates
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
        "root_path": "/tmp/test",
        "tables": {
            "visitors": """
                surname varchar(256) not null,
                given_name varchar(256) not null,
                nin varchar(256) not null unique,
                other json not null,
                timestamp varchar(256) not null
            """,
            "fingerprints": """
                print_id varchar(256) not null unique,
                nin varchar(256) not null,
                other json not null,
                timestamp varchar(32) json not null
            """
        }
    }

    defaults["db_path"] = defaults["root_path"] + "/visitor.db"
    defaults["fingerprints_path"] = defaults["root_path"] + "/prints/all"

    topic = "test"

    for key in defaults:
        topic_key = topic + f"/{key}"

        # if not config.getValue(topic_key):
        config.setValue(topic_key, defaults[key])
        # print(config.getValue(topic_key))

init()


if __name__ == "__main__":
# db_path = config.getValue("e-visitor/db_path")
# print(db_path)

    data = {
        "nin": "156567djhkjhfvjkkko39hiu",
        "surname":"bukenya",
        "given_name": "tom",
        "hand": "left",
        "finger": "middle",
        "fingerprint_url": "/tmp/e-visitors/prints/all/somecode.png"
    }


    other = {}

    visitor_data = {
        "surname": data["surname"],
        "given-name": data["given_name"],
        "nin": data["nin"],
        "other": json.dumps(other),
        "timestamp": dates.currentTimestamp()
    }

    with Api(config.getValue("test/db_path"), config.getValue("test/tables"), readonly=False) as db:
            print(db.insert("visitors", [tuple(visitor_data.values())]))
        
    with Api(config.getValue("test/db_path"), config.getValue("test/tables"), readonly=True) as db:
            print(db.fetch("visitors", ["nin"], "nin=?", ["cahgdhjh378673"]))

    # with Api(config.getValue("e-visitor/db_path"), config.getValue("e-visitor/tables"), readonly=False) as db:
    #         print(db.update("users", ["first_name", "last_name"], ["tony",], "first_name=?", ["timothy"]))
    #         print(db.fetch("users", ["*"], "first_name=?", ["tony"]))


