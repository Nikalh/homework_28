import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def selection_create_test(client, access_token):
    ad_list = AdFactory.create_batch(3)


    data = {
        "name": "Моя подборка",
        "items": [ad.pk for ad in ad_list]
    }

    expected_data = {
        "id": 1,
        "name": "Моя подборка",
        "owner": "test_user",
        "items": [ad.pk for ad in ad_list]
    }
    response = client.post("/selection/", data, HTTP_AUTORIZATION="Bearer " + access_token)
    assert response.status_code == 201
    assert response.data == expected_data
