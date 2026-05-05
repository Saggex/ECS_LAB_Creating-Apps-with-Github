import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_summary_returns_200_and_expected_shape(client):
    response = client.get('/summary')
    assert response.status_code == 200
    data = response.get_json()
    assert 'total' in data
    assert 'by_verdict' in data
    assert 'by_tool' in data

# Lab 2 Challenge: add more tests below this line
# Add a test for each of the the summary types:  by_verdict and by_tool.  You can use the existing tests for the /entries endpoint as a guide for how to set up the test data and make assertions about the response.
