import mysql as sql

connection = sql.connect('database.db')
connection.execute(
    'CREATE TABLE IF NOT EXISTS pre_train_data(map TEXT, game_num INTEGER, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, PRIMARY KEY(map, game_num));')
connection.execute(
    'CREATE TABLE IF NOT EXISTS post_train_we(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5);')
connection.commit()