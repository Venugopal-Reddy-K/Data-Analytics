# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS song_play;"
user_table_drop = "DROP TABLE IF EXISTS user;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS song_play(songplay_id varchar PRIMARY KEY, start_time datetime, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS user(user_id varchar PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song(song_id varchar PRIMARY KEY, title varchar, artist_id varchar, year int, duration timestamp);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist(artist_id varchar PRIMARY KEY, name varchar, location varchar, latitude float, longitude float);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time datetime, hour int, day int, week int, month int, year int, weekday varchar);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO song_play(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)""")

user_table_insert = ("""INSERT INTO user(user_id, first_name, last_name, gender, level)\
VALUES (%s, %s, %s, %s, %s)""")

song_table_insert = ("""INSERT INTO song(song_id PRIMARY KEY, title , artist_id , year, duration)\
VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)""")

artist_table_insert = ("""INSERT INTO artist(artist_id PRIMARY KEY, name, location, latitude , longitude)\
VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)\
VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]