import pytest


def test_string_in_url(client):
    """Test for a 404 response status code when there is a string in
    the url."""
    response = client.get('/qstnrs/"delete * from users;"')
    assert response.status_code == 404


@pytest.mark.django_db
def test_index_url(client):
    """Test for a 200 response status code when requesting the index page."""
    response = client.get('/qstnrs/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_page_no_questions(client):
    """Test that a correct message is displayed when there are no questions
    for a given page."""
    response = client.get('/qstnrs/2/4/')

    assert response.status_code == 200
    assert "This page has no questions available." in response.content