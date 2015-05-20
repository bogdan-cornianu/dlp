import pytest
from django.core.urlresolvers import reverse, NoReverseMatch


@pytest.mark.django_db
def test_index_string_param(client):
    with pytest.raises(NoReverseMatch):
        client.get(reverse('qstnrs-index', args=('a',)))


@pytest.mark.django_db
def test_page_noid_string_param(client):
    with pytest.raises(NoReverseMatch):
        client.get(reverse('qstnrs-page-no-id', args=('a',)))


@pytest.mark.django_db
def test_page_string_param(client):
    with pytest.raises(NoReverseMatch):
        client.get(reverse('qstnrs-page', args=('a',)))


@pytest.mark.django_db
def test_result_string_param(client):
    with pytest.raises(NoReverseMatch):
        client.get(reverse('qstnrs-result', args=('a',)))


@pytest.mark.django_db
def test_index_url(client):
    response = client.get(reverse('qstnrs-index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_page_no_questions(client):
    """Test that a correct message is displayed when there are no questions
    for a given page."""
    response = client.get(reverse('qstnrs-page', args=(2, 4)))

    assert response.status_code == 200
    assert "This page has no questions available." in response.content
