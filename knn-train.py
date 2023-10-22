import os
import cv2
import numpy as np
import sqlite3 as sql
import math

rows = 100
cols = 100

matrix = [[[] for _ in range(cols)] for _ in range(rows)]


def train_we():
    for x in range(100):
        for y in range(100):
            matrix[x][y] = [None, None, None, None, None, None, None, None]
    connection = sql.connect('database.db')
    k = 3
    for x in range(100):
        for y in range(100):
            cursor = connection.execute('SELECT x1, y1, x2, y2 FROM pre_train_we;')
            cursor.fetchall()
            counter = 0
            data_row = [[-1, -1, -1, -1] for _ in range(3)]
            distance_row = [-1] * 3
            weight = [-1] * 3
            total = 0
            x_trans = x
            y_trans = y

            for row in cursor:

                x1 = row[0]
                y1 = row[1]
                x2 = row[2] 
                y2 = row[3]
                distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
                print(x1, x2)
                if counter != 3:
                    distance_row[counter] = distance
                    data_row[counter] = row
                    counter = counter + 1
                else:
                    int_large = -1
                    pop_dex = -1
                    for index in range(3):
                        if distance_row[index] > int_large:
                            int_large = distance_row[index]
                            pop_dex = index
                    distance_row[pop_dex] = distance
                    data_row[pop_dex][0] = x1
                    data_row[pop_dex][1] = y1
                    data_row[pop_dex][2] = x2
                    data_row[pop_dex][3] = y2
            
            for k in range(3):
                weight[k] = 1 / distance_row[k]
                total += weight[k]

            for k in range(3):
                x1 = data_row[k][0]
                y1 = data_row[k][1]
                x2 = data_row[k][2] 
                y2 = data_row[k][3]
                x_change = math.floor((weight[k] / total)*(x2 - x1))
                y_change = math.floor((weight[k] / total)*(y2 - y1))
                x_trans = x_trans + x_change
                y_trans = y_trans + y_change
            if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                matrix[x][y][0] = x_trans
                matrix[x][y][1] = y_trans
    
    # second
    for x in range(100):
        for y in range(100):
            if matrix[x][y][0] != None:
                cursor = connection.execute('SELECT x2, y2, x3, y3 FROM pre_train_we;')
                cursor.fetchall()
                counter = 0
                data_row = data_row = [[-1, -1, -1, -1] for _ in range(3)]
                distance_row = [-1] * 3
                weight = [-1] * 3
                total = 0
                x_trans = matrix[x][y][0]
                y_trans = matrix[x][y][1]
                for row in cursor:

                    x1 = row[0]
                    y1 = row[1]
                    x2 = row[2] 
                    y2 = row[3]
                    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                    if counter != 3:
                        distance_row[counter] = distance
                        data_row[counter][0] = x1
                        data_row[counter][1] = y1
                        data_row[counter][2] = x2
                        data_row[counter][3] = y2
                        counter = counter + 1
                    else:
                        int_large = -1
                        pop_dex = -1
                        for index in range(3):
                            if distance_row[index] > int_large:
                                int_large = distance_row[index]
                                pop_dex = index
                        distance_row[pop_dex] = distance
                        data_row[pop_dex][0] = x1
                        data_row[pop_dex][1] = y1
                        data_row[pop_dex][2] = x2
                        data_row[pop_dex][3] = y2
                
                for k in range(3):
                    weight[k] = (1 / distance_row[k])
                    total += weight[k]
                for k in range(3):
                    x1 = data_row[k][0]
                    y1 = data_row[k][1]
                    x2 = data_row[k][2] 
                    y2 = data_row[k][3]
                    x_change = math.floor((weight[k] / total)*(x2 - x1))
                    y_change = math.floor((weight[k] / total)*(y2 - y1))
                    x_trans = x_trans + x_change
                    y_trans = y_trans + y_change
                if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                    matrix[x][y][2] = x_trans
                    matrix[x][y][3] = y_trans

    # third
    for x in range(100):
        for y in range(100):
            if matrix[x][y][2] != None:
                cursor = connection.execute('SELECT x3, y3, x4, y4 FROM pre_train_we;')
                cursor.fetchall()
                counter = 0
                data_row = data_row = [[-1, -1, -1, -1] for _ in range(3)]
                distance_row = [-1] * 3
                weight = [-1] * 3
                total = 0
                x_trans = matrix[x][y][2]
                y_trans = matrix[x][y][3]
                for row in cursor:
                    x1 = row[0]
                    y1 = row[1]
                    x2 = row[2] 
                    y2 = row[3]
                    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                    if counter != 3:
                        distance_row[counter] = distance
                        data_row[counter][0] = x1
                        data_row[counter][1] = y1
                        data_row[counter][2] = x2
                        data_row[counter][3] = y2
                        counter = counter + 1
                    else:
                        int_large = -1
                        pop_dex = -1
                        for index in range(3):
                            if distance_row[index] > int_large:
                                int_large = distance_row[index]
                                pop_dex = index
                        distance_row[pop_dex] = distance
                        data_row[pop_dex][0] = x1
                        data_row[pop_dex][1] = y1
                        data_row[pop_dex][2] = x2
                        data_row[pop_dex][3] = y2
                
                for k in range(3):
                    weight[k] = 1 / distance_row[k]
                    total += weight[k]
                for k in range(3):
                    x1 = data_row[k][0]
                    y1 = data_row[k][1]
                    x2 = data_row[k][2] 
                    y2 = data_row[k][3]
                    x_change = math.floor((weight[k] / total)*(x2 - x1))
                    y_change = math.floor((weight[k] / total)*(y2 - y1))
                    x_trans = x_trans + x_change
                    y_trans = y_trans + y_change
                if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                    matrix[x][y][4] = x_trans
                    matrix[x][y][5] = y_trans

    # fourth
    for x in range(100):
        for y in range(100):
            if matrix[x][y][4] != None:
                cursor = connection.execute('SELECT x4, y4, x5, y5 FROM pre_train_we;')
                cursor.fetchall()
                counter = 0
                data_row = data_row = [[-1, -1, -1, -1] for _ in range(3)]
                distance_row = [-1] * 3
                weight = [-1] * 3
                total = 0
                x_trans = matrix[x][y][4]
                y_trans = matrix[x][y][5]
                for row in cursor:

                    x1 = row[0]
                    y1 = row[1]
                    x2 = row[2] 
                    y2 = row[3]
                    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                    if counter != 3:
                        distance_row[counter] = distance
                        data_row[pop_dex][0] = x1
                        data_row[counter][1] = y1
                        data_row[counter][2] = x2
                        data_row[counter][3] = y2
                        counter = counter + 1
                    else:
                        int_large = -1
                        pop_dex = -1
                        for index in range(3):
                            if distance_row[index] > int_large:
                                int_large = distance_row[index]
                                pop_dex = index
                        distance_row[pop_dex] = distance
                        data_row[pop_dex][0] = x1
                        data_row[pop_dex][1] = y1
                        data_row[pop_dex][2] = x2
                        data_row[pop_dex][3] = y2
                
                for k in range(3):
                    weight[k] = 1 / distance_row[k]
                    total += weight[k]
                for k in range(3):
                    x1 = data_row[k][0]
                    y1 = data_row[k][1]
                    x2 = data_row[k][2] 
                    y2 = data_row[k][3]
                    x_change = math.floor((weight[k] / total)*(x2 - x1))
                    y_change = math.floor((weight[k] / total)*(y2 - y1))
                    x_trans = x_trans + x_change
                    y_trans = y_trans + y_change
                if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                    matrix[x][y][6] = x_trans
                    matrix[x][y][7] = y_trans
                    
    # push trained data

    for x in range(100):
        for y in range(100):
            x1 = x
            y1 = y
            x2 = matrix[x][y][0]
            y2 = matrix[x][y][1]
            x3 = matrix[x][y][2]
            y3 = matrix[x][y][3]
            x4 = matrix[x][y][4]
            y4 = matrix[x][y][5]
            x5 = matrix[x][y][6]
            y5 = matrix[x][y][7]
            if x1 ==  None or y1 == None or x2 == None or y2 == None or x3 == None or y3 == None or x4 == None or y4 == None or x5 == None or y5 == None:
                continue
            else:
                connection.execute('INSERT INTO post_train_we(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5) VALUES (?,?,?,?,?,?,?,?,?,?);', 
                                (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5))
    connection.commit()
    connection.close()
    return

def train_kc():
    for x in range(101):
        for y in range(101):
            matrix[x][y] = [None, None, None, None, None, None, None, None]
    connection = sql.connect('database.db')
    k = 3
    for x in range(101):
        for y in range(101):
            cursor = connection.execute('SELECT x1, y1, x2, y2 FROM pre_train_kc;')
            cursor.fetchall()
            counter = 0
            data_row = []
            distance_row = []
            weight = []
            total = 0
            x_trans = x
            y_trans = y
            for row in cursor:

                x1, y1, x2, y2 = row
                distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                if counter != 3:
                    distance_row[counter] = distance
                    data_row[counter] = row
                    counter = counter + 1
                else:
                    int_large = -1
                    pop_dex = -1
                    for index in range(3):
                        if distance_row[index] > int_large:
                            int_large = distance_row[index]
                            pop_dex = index
                    distance_row[pop_dex] = distance
                    data_row[pop_dex] = row
            
            for k in range(3):
                weight[k] = 1 / distance_row[k]
                total += weight[k]
            for k in range(3):
                x1, y1, x2, y2 = data_row[k]
                x_change = math.floor((weight[k] / total)*(x2 - x1))
                y_change = math.floor((weight[k] / total)*(y2 - y1))
                x_trans = x_trans + x_change
                y_trans = y_trans + y_change
            if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                matrix[x][y][0] = x_trans
                matrix[x][y][1] = y_trans
    
    # second
    for x in range(101):
        for y in range(101):
            if matrix[x][y][0] != None:
                cursor = connection.execute('SELECT x2, y2, x3, y3 FROM pre_train_kc;')
                cursor.fetchall()
                counter = 0
                data_row = []
                distance_row = []
                weight = []
                total = 0
                x_trans = matrix[x][y][0]
                y_trans = matrix[x][y][1]
                for row in cursor:

                    x1, y1, x2, y2 = row
                    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                    if counter != 3:
                        distance_row[counter] = distance
                        data_row[counter] = row
                        counter = counter + 1
                    else:
                        int_large = -1
                        pop_dex = -1
                        for index in range(3):
                            if distance_row[index] > int_large:
                                int_large = distance_row[index]
                                pop_dex = index
                        distance_row[pop_dex] = distance
                        data_row[pop_dex] = row
                
                for k in range(3):
                    weight[k] = 1 / distance_row[k]
                    total += weight[k]
                for k in range(3):
                    x_change = math.floor((weight[k] / total)*(x2 - x1))
                    y_change = math.floor((weight[k] / total)*(y2 - y1))
                    x_trans = x_trans + x_change
                    y_trans = y_trans + y_change
                if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                    matrix[x][y][2] = x_trans
                    matrix[x][y][3] = y_trans

    # third
    for x in range(101):
        for y in range(101):
            if matrix[x][y][2] != None:
                cursor = connection.execute('SELECT x3, y3, x4, y4 FROM pre_train_kc;')
                cursor.fetchall()
                counter = 0
                data_row = []
                distance_row = []
                weight = []
                total = 0
                x_trans = matrix[x][y][2]
                y_trans = matrix[x][y][3]
                for row in cursor:

                    x1, y1, x2, y2 = row
                    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                    if counter != 3:
                        distance_row[counter] = distance
                        data_row[counter] = row
                        counter = counter + 1
                    else:
                        int_large = -1
                        pop_dex = -1
                        for index in range(3):
                            if distance_row[index] > int_large:
                                int_large = distance_row[index]
                                pop_dex = index
                        distance_row[pop_dex] = distance
                        data_row[pop_dex] = row
                
                for k in range(3):
                    weight[k] = 1 / distance_row[k]
                    total += weight[k]
                for k in range(3):
                    x_change = math.floor((weight[k] / total)*(x2 - x1))
                    y_change = math.floor((weight[k] / total)*(y2 - y1))
                    x_trans = x_trans + x_change
                    y_trans = y_trans + y_change
                if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                    matrix[x][y][4] = x_trans
                    matrix[x][y][5] = y_trans

    # fourth
    for x in range(101):
        for y in range(101):
            if matrix[x][y][4] != None:
                cursor = connection.execute('SELECT x4, y4, x5, y5 FROM pre_train_kc;')
                cursor.fetchall()
                counter = 0
                data_row = []
                distance_row = []
                weight = []
                total = 0
                x_trans = matrix[x][y][4]
                y_trans = matrix[x][y][5]
                for row in cursor:

                    x1, y1, x2, y2 = row
                    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                    if counter != 3:
                        distance_row[counter] = distance
                        data_row[counter] = row
                        counter = counter + 1
                    else:
                        int_large = -1
                        pop_dex = -1
                        for index in range(3):
                            if distance_row[index] > int_large:
                                int_large = distance_row[index]
                                pop_dex = index
                        distance_row[pop_dex] = distance
                        data_row[pop_dex] = row
                
                for k in range(3):
                    weight[k] = 1 / distance_row[k]
                    total += weight[k]
                for k in range(3):
                    x_change = math.floor((weight[k] / total)*(x2 - x1))
                    y_change = math.floor((weight[k] / total)*(y2 - y1))
                    x_trans = x_trans + x_change
                    y_trans = y_trans + y_change
                if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                    matrix[x][y][6] = x_trans
                    matrix[x][y][7] = y_trans
                    
    # push trained data

    for x in range(101):
        for y in range(101):
            x1 = x
            y1 = y
            x2 = matrix[x][y][0]
            y2 = matrix[x][y][1]
            x3 = matrix[x][y][2]
            y3 = matrix[x][y][3]
            x4 = matrix[x][y][4]
            y4 = matrix[x][y][5]
            x5 = matrix[x][y][6]
            y5 = matrix[x][y][7]
            connection.execute('INSERT INTO post_train_kc(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5) VALUES (?,?,?,?,?,?,?,?,?,?);', 
                               (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5))
    connection.commit()
    connection.close()
    return

def train_o():
    for x in range(101):
        for y in range(101):
            matrix[x][y] = [None, None, None, None, None, None, None, None]
    connection = sql.connect('database.db')
    k = 3
    for x in range(101):
        for y in range(101):
            cursor = connection.execute('SELECT x1, y1, x2, y2 FROM pre_train_o;')
            cursor.fetchall()
            counter = 0
            data_row = []
            distance_row = []
            weight = []
            total = 0
            x_trans = x
            y_trans = y
            for row in cursor:

                x1, y1, x2, y2 = row
                distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                if counter != 3:
                    distance_row[counter] = distance
                    data_row[counter] = row
                    counter = counter + 1
                else:
                    int_large = -1
                    pop_dex = -1
                    for index in range(3):
                        if distance_row[index] > int_large:
                            int_large = distance_row[index]
                            pop_dex = index
                    distance_row[pop_dex] = distance
                    data_row[pop_dex] = row
            
            for k in range(3):
                weight[k] = 1 / distance_row[k]
                total += weight[k]
            for k in range(3):
                x1, y1, x2, y2 = data_row[k]
                x_change = math.floor((weight[k] / total)*(x2 - x1))
                y_change = math.floor((weight[k] / total)*(y2 - y1))
                x_trans = x_trans + x_change
                y_trans = y_trans + y_change
            if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                matrix[x][y][0] = x_trans
                matrix[x][y][1] = y_trans
    
    # second
    for x in range(101):
        for y in range(101):
            if matrix[x][y][0] != None:
                cursor = connection.execute('SELECT x2, y2, x3, y3 FROM pre_train_o;')
                cursor.fetchall()
                counter = 0
                data_row = []
                distance_row = []
                weight = []
                total = 0
                x_trans = matrix[x][y][0]
                y_trans = matrix[x][y][1]
                for row in cursor:

                    x1, y1, x2, y2 = row
                    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                    if counter != 3:
                        distance_row[counter] = distance
                        data_row[counter] = row
                        counter = counter + 1
                    else:
                        int_large = -1
                        pop_dex = -1
                        for index in range(3):
                            if distance_row[index] > int_large:
                                int_large = distance_row[index]
                                pop_dex = index
                        distance_row[pop_dex] = distance
                        data_row[pop_dex] = row
                
                for k in range(3):
                    weight[k] = 1 / distance_row[k]
                    total += weight[k]
                for k in range(3):
                    x_change = math.floor((weight[k] / total)*(x2 - x1))
                    y_change = math.floor((weight[k] / total)*(y2 - y1))
                    x_trans = x_trans + x_change
                    y_trans = y_trans + y_change
                if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                    matrix[x][y][2] = x_trans
                    matrix[x][y][3] = y_trans

    # third
    for x in range(101):
        for y in range(101):
            if matrix[x][y][2] != None:
                cursor = connection.execute('SELECT x3, y3, x4, y4 FROM pre_train_o;')
                cursor.fetchall()
                counter = 0
                data_row = []
                distance_row = []
                weight = []
                total = 0
                x_trans = matrix[x][y][2]
                y_trans = matrix[x][y][3]
                for row in cursor:

                    x1, y1, x2, y2 = row
                    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                    if counter != 3:
                        distance_row[counter] = distance
                        data_row[counter] = row
                        counter = counter + 1
                    else:
                        int_large = -1
                        pop_dex = -1
                        for index in range(3):
                            if distance_row[index] > int_large:
                                int_large = distance_row[index]
                                pop_dex = index
                        distance_row[pop_dex] = distance
                        data_row[pop_dex] = row
                
                for k in range(3):
                    weight[k] = 1 / distance_row[k]
                    total += weight[k]
                for k in range(3):
                    x_change = math.floor((weight[k] / total)*(x2 - x1))
                    y_change = math.floor((weight[k] / total)*(y2 - y1))
                    x_trans = x_trans + x_change
                    y_trans = y_trans + y_change
                if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                    matrix[x][y][4] = x_trans
                    matrix[x][y][5] = y_trans

    # fourth
    for x in range(101):
        for y in range(101):
            if matrix[x][y][4] != None:
                cursor = connection.execute('SELECT x4, y4, x5, y5 FROM pre_train_o;')
                cursor.fetchall()
                counter = 0
                data_row = []
                distance_row = []
                weight = []
                total = 0
                x_trans = matrix[x][y][4]
                y_trans = matrix[x][y][5]
                for row in cursor:

                    x1, y1, x2, y2 = row
                    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

                    if counter != 3:
                        distance_row[counter] = distance
                        data_row[counter] = row
                        counter = counter + 1
                    else:
                        int_large = -1
                        pop_dex = -1
                        for index in range(3):
                            if distance_row[index] > int_large:
                                int_large = distance_row[index]
                                pop_dex = index
                        distance_row[pop_dex] = distance
                        data_row[pop_dex] = row
                
                for k in range(3):
                    weight[k] = 1 / distance_row[k]
                    total += weight[k]
                for k in range(3):
                    x_change = math.floor((weight[k] / total)*(x2 - x1))
                    y_change = math.floor((weight[k] / total)*(y2 - y1))
                    x_trans = x_trans + x_change
                    y_trans = y_trans + y_change
                if x_trans >= 0 and x_trans <= 100 and y_trans >= 0 and y_trans <= 100:
                    matrix[x][y][6] = x_trans
                    matrix[x][y][7] = y_trans
                    
    # push trained data

    for x in range(101):
        for y in range(101):
            x1 = x
            y1 = y
            x2 = matrix[x][y][0]
            y2 = matrix[x][y][1]
            x3 = matrix[x][y][2]
            y3 = matrix[x][y][3]
            x4 = matrix[x][y][4]
            y4 = matrix[x][y][5]
            x5 = matrix[x][y][6]
            y5 = matrix[x][y][7]
            connection.execute('INSERT INTO post_train_o(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5) VALUES (?,?,?,?,?,?,?,?,?,?);', 
                               (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5))
    connection.commit()
    connection.close()
    return


train_we()
#train_kc()
#train_o()