import io
import pytest
from main_app.app import app
from PIL import Image
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
@pytest.fixture
def setup_upload_folder():
    upload_folder = 'model_folder/uploaded_images_folder'
    os.makedirs(upload_folder, exist_ok=True)
    yield

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test if the homepage loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Upload" in response.data

def test_no_file_uploaded(client):
    """Test if API returns 400 when no file is uploaded."""
    response = client.post('/getcats/', data={})
    assert response.status_code == 400
    assert b"No file uploaded" in response.data

@patch('main_app.app.get_model')  # patch get_model function
def test_with_mock_model(mock_get_model, client):
    # Create a mock model instance with a predict method
    mock_model_instance = mock_get_model.return_value
    mock_model_instance.predict.return_value = []

    # Create dummy image in memory
    img = Image.new("RGB", (100, 100), color="white")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    data = {'image': (img_bytes, 'test.png')}

    response = client.post('/getcats/', data=data, content_type='multipart/form-data')

    assert response.status_code == 200
    assert response.mimetype == 'image/png'