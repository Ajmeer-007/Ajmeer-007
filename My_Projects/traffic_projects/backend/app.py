from flask import Flask, request, jsonify
from flask_cors import CORS
import os
# from yolov4 import detect_cars   # Commented out for now
# from algo import optimize_traffic  # Commented out for now

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('videos')
    if len(files) != 4:
        return jsonify({'error': 'Please upload exactly 4 videos'}), 400

    # Save uploaded videos
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    video_paths = []
    for i, file in enumerate(files):
        video_path = os.path.join('uploads', f'video_{i}.mp4')
        file.save(video_path)
        video_paths.append(video_path)

    # TEMPORARY: Skip actual detection and return dummy optimization results
    result = {
        'north': 30,
        'south': 25,
        'west': 20,
        'east': 35
    }

    return jsonify(result)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
