import random

def test_inventory(page):
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    assert(response.status == 200)
    print(response.status)
    print(response.json())


def test_add_user(page):
    data = [
              {
                "id": random.randint(1, 1000),
                "username": "fsd",
                "firstName": "fff",
                "lastName": "ggg",
                "email": "bbb",
                "password": "tt",
                "phone": "333",
                "userStatus": 0
              }
            ]
    header = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray',data=data, headers=header)
    assert (response.status == 200)
    print(response.status)
    print(response.json())