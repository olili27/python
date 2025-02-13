# import sqlite3

# conn = sqlite3.connect("one.db")
# # c = conn.cursor()

# conn.execute("""
# create table if not exists other(
#           first text,
#           last text
# )
# """)

# with conn:
#     conn.execute("""
# delete from other where last = ?
# """, ["other"])
# # conn.commit()
# # c.close()
# conn.close()

obj = {
                op:{'passed':0, 'failed':0}
                for op in ['insert','delete','update','createTable']
            }

print(obj)