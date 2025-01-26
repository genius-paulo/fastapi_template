import pytest

BASE_URL = 'http://localhost:8000'  # Укажите здесь адрес вашего API


@pytest.mark.asyncio
async def test_home_page(client):
    response = await client.get(f'{BASE_URL}/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Привет, Мир!'}


@pytest.mark.asyncio
async def test_get_all_students(client):
    response = await client.get(f'{BASE_URL}/students')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_students_with_filters(client):
    response = await client.get(f'{BASE_URL}/students?course=1&major=Computer Science&enrollment_year=2020')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
