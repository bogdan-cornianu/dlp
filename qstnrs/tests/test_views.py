from questionnaire.views import page, page_without_id, index, result
from django.core.urlresolvers import reverse
import pytest


@pytest.mark.django_db
def test_page(rf):
    request = rf.get(reverse('qstnrs-page', args=(1, 1)))
    response = page(request, '1', '1')

    assert response.status_code == 200
    assert "What&#39;s your name?" in response.content


@pytest.mark.django_db
def test_page_without_id(rf):
    request = rf.get(reverse('qstnrs-page-no-id', args=(1,)))
    response = page_without_id(request, '1')

    assert response.status_code == 302


@pytest.mark.django_db
def test_index(rf):
    request = rf.get(reverse('qstnrs-index'))
    request.session = {}
    response = index(request)

    assert response.status_code == 200
    assert 'List of questionnaires:' in response.content


@pytest.mark.django_db
def test_result(rf):
    request = rf.get(reverse('qstnrs-result', args=(1,)))
    request.session = {'choices': [2, 5, 10, 14, 17, 20, 23, 27]}
    response = result(request, '1')

    assert response.status_code == 200
