import pytest

@pytest.mark.django_db
def ad_create_test(client, access_token,user, category):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "СТол",
        "price": 1000,
        "description": ""
    }

    expected_data = {
        "id": 1,
        "is_published": False,
        "name": "Стол из слэба",
        "price": 28500,
        "description": "",
        "image": None,
        "author": user.pk,
        "category": category.pk
    }
    response = client.post("/ad/", data, HTTP_AUTORIZATION="Bearer " + access_token)
    assert response.status_code == 201
    assert response.data == expected_data