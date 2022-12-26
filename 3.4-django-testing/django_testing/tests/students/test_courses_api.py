import pytest
from rest_framework.test import APIClient
from students.models import Student, Course
from model_bakery import baker


def test_example():
    assert False is False


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_student(client, student_factory, course_factory):
    course = course_factory()
    cource_id = course.id
    response = client.get('/api/v1/courses/', {id: cource_id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == cource_id


@pytest.mark.django_db
def test_get_students(client, student_factory, course_factory):
    course = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    for i, name in enumerate(data):
        assert name['name'] == course[i].name


@pytest.mark.django_db
def test_application_filter_id(client, course_factory):
    course = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/', {'id': course[0].id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course[0].id


@pytest.mark.django_db
def test_application_filter_name(client, course_factory):
    course = course_factory()
    name = course.name
    response = client.get('/api/v1/courses/', {'name': name})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == name


@pytest.mark.django_db
def test_add_courses(client):
    response = client.post('/api/v1/courses/', {'name': 'python'})
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'python'


@pytest.mark.django_db
def test_edit_courses(client, course_factory):
    course = course_factory()
    course_id, course_name = course.id, course.name
    response = client.patch('/api/v1/courses/', {id: course_id, 'name': course_name})
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'python'


@pytest.mark.django_db
def test_edit_courses(client, course_factory):
    course = course_factory()
    response = client.delete(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 204

