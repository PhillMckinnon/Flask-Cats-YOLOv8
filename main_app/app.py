from PIL import Image, ImageFont, ImageDraw
from flask import Flask, request, render_template, send_file
from ultralytics import YOLO
import os
import io
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'model_folder/uploaded_images_folder'
model = YOLO("model_folder/best.pt")
def detect_and_annotate(image, conf=0.25, rectangle_thickness=3, text_size=70):
    image_pil = image if (isinstance(image, Image.Image)) else Image.fromarray(image)
    cat_detected = False
    draw = ImageDraw.Draw(image_pil)
    font = ImageFont.truetype("arial.ttf", text_size)
    results = model.predict(image, conf=conf)
    for result in results:
        for box in result.boxes:
            draw.rectangle(
                [
                    (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                    (int(box.xyxy[0][2]), int(box.xyxy[0][3]))
                ],
                outline=(255, 0, 255),
                width=rectangle_thickness
            )
            draw.text(
                (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - text_size + 70),
                result.names[int(box.cls[0])],
                fill=(230, 210, 0),
                font=font
            )

    return image_pil


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/getcats/', methods=['POST'])
def apply_detection():
    file = request.files.get('image')
    if not file or file.filename == '':
        return 'No file uploaded', 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    image = Image.open(file_path).convert("RGB")
    annotated_image = detect_and_annotate(image)
    buf = io.BytesIO()
    annotated_image.save(buf, format="PNG")
    buf.seek(0)
    os.remove(file_path)
    return send_file(buf, mimetype='image/png')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)