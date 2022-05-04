"""This test the homepage"""

def test_hellow_world(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
