from flask import Flask, request, jsonify
import os
import cv2
import sqlite3 as sql
from flask_cors import CORS

app = Flask(__name__)

def draw_rings(image, coordinates, diameters):
    for x, y, diameter in zip(coordinates[::2], coordinates[1::2], diameters):
        center = (int(x), int(y))
        radius = int(diameter / 2)
        image = cv2.circle(image, center, radius, (255, 255, 255), 2)
    return image

@app.route('/we_get_image', methods=['POST'])
def we_get_image():
    print("Received Request")
    try:
        data = request.get_json()
        x = data['x']
        y = data['y']
        
        junk = {
            "message":"Hello, this message is useless."
        }
        connection = sql.connect('database.db')
        cursor = connection.execute('SELECT x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 FROM post_train_we WHERE x1 = ? AND x2 = ?;', (x, y))
        row = cursor.fetchone()

        if row:
            x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 = row
            image_path = './zone-predictor-website/src/components/Pages/Map/we.jpg'

            if os.path.exists(image_path):
                image = cv2.imread(image_path)
                diameters = [60, 30, 20, 10, 5]
                coordinates = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]

                image = draw_rings(image, coordinates, diameters)

                result_image_path = './zone-predictor-website/src/components/Pages/Map/result.jpg'
                cv2.imwrite(result_image_path, image)

                return jsonify(junk)
            else:
                return jsonify(junk)
        else:
            return jsonify(junk)

    except Exception as e:
        return jsonify(junk)

if __name__ == '__main__':
    app.run(debug=True)