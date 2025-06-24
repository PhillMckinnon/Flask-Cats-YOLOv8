import io
import pytest
from main_app.app import app
from PIL import Image
from unittest.mock import patch
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

@patch('main_app.app.model')
def test_with_mock_model(mock_model, client):
    """Test with a mocked YOLO model and fake image upload."""
    mock_model.predict.return_value = []

    # Create dummy image in memory
    img = Image.new("RGB", (100, 100), color="white")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    data = {
        'image': (img_bytes, 'test.png'),
    }

    response = client.post('/getcats/', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert response.mimetype == 'image/png'