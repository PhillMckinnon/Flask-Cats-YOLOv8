<a href="https://codecov.io/gh/PhillMckinnon/Flask-Cats-YOLOv8"> <img src="https://codecov.io/gh/PhillMckinnon/Flask-Cats-YOLOv8/graph/badge.svg?token=JF6QMZU4PC" alt="Code Coverage Badge"/> </a> <img src="https://img.shields.io/github/license/PhillMckinnon/Flask-Cats-YOLOv8" alt="License Badge"/> <img src="https://img.shields.io/badge/Made%20With-Python%203.8+-blue.svg" alt="Python Version Badge"/> <img src="https://img.shields.io/badge/Docker-Supported-blue" alt="Docker Badge"/>

# 🐱 Flask Cat Detection Project

Welcome to the **Flask Cats Project**! This project offers a friendly Flask-based web interface for detecting cats in images using the YOLOv8 object detection model. Just upload an image and find out if there are any adorable cats hidden within! 🖼️🐾

---

## 🚀 Features

* **Cat Detection with YOLOv8**: Accurate and fast object detection using a model trained on a custom cat dataset.
* **Flask Web Interface**: Simple, interactive UI for uploading images and viewing detection results.
* **Docker Support**: Run the entire app with a single Docker command.

---

## 🧑‍💻 Getting Started

### 🔧 Prerequisites

Make sure you have the following installed:

* Python **3.8+**
* `pip` – Python package manager
* Virtual environment tool (optional, but recommended)

---

### ⚙️ Run Locally (Without Docker)

```bash
# Clone the repository
git clone https://github.com/PhillMckinnon/flask_cats_project.git
cd flask_cats_project/main_app

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

---

### 🐳 Run with Docker (Recommended)

```bash
docker pull phillipmckinnon/flask-cats:latest
docker run -p 8080:8080 phillipmckinnon/flask-cats:latest
```

The app will be available at: [http://localhost:8080](http://localhost:8080)

---

## 🧠 Model Details

* **YOLOv8**: A state-of-the-art object detection model, trained on a custom dataset of cat images.
* Detects cats with high precision and speed using a lightweight, optimized model.

---

## 💻 Technologies Used

* **YOLOv8** – Object detection model
* **Flask** – Lightweight web framework for Python
* **PIL (Pillow)** – Image processing library for Python

---

## 📈 Example

Upload an image containing a cat, like the one below:

![image](https://github.com/user-attachments/assets/1c80e78d-92cd-4f39-b7b2-d33c4ad36504)

---

## 📫 Contact

For questions, feedback, or collaboration, feel free to reach out:

* 📧 Email: [phillipmckinnonwork@proton.me](mailto:phillipmckinnonwork@proton.me)
* 🐙 GitHub: [@PhillMckinnon](https://github.com/PhillMckinnon)

**Happy cat detecting!** 😺🐾


