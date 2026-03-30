import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['version'] == '1.0.0'

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_test_endpoint(client):
    response = client.get('/api/test')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Pipeline test successful!'