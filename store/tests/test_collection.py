from rest_framework.test import APIClient
from rest_framework import status
import pytest
from store.models import Collection
from model_bakery import baker


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_anonymous_return_401(self, create_collection):
        '''test that if the user is not registered return 401'''
        # Arrange

        # Act
        response = create_collection({'title': 'A'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self, authenticate_user, create_collection):
        '''test that if the user is not admin return 403'''
        # Arrange
        authenticate_user()

        # Act
        response = create_collection({'title': 'A'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, authenticate_user, create_collection):
        '''test that if the data is invalid'''
        # Arrange

        # Act
        authenticate_user(True)
        response = create_collection({'title': ''})

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_return_201(self, authenticate_user, create_collection):
        '''test that if the data is valid'''
        # Arrange

        # Act
        authenticate_user(True)
        response = create_collection({'title': 'A'})

        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    '''test retrieving collection'''

    def test_if_collection_exists_return_200(self, api_client):
        '''test retrieving if collection exist and return 200'''
        # Arrange
        collection = baker.make(Collection)

        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }

    def test_if_collection_does_not_exit_return_404(self, api_client):
        '''Test that the collection does not exist then return 404'''
        collection = baker.make(Collection)

        response = api_client.get(f'/store/collections/{collection.id+1}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestUpdatingCollection:
    '''Test updating a collection'''
