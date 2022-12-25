import pytest

from ads.serializer import AdListSerializer, AdDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def ads_detail_test(client, access_token):
    ad = AdFactory.create_batch(5)

    response = client.get(f"/ad/{ad.pk}/", HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 200
    assert response.data == AdDetailSerializer(ad).data
