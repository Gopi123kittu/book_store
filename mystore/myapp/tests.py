from django.test import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
import requests
import random
import json

class ModelTest(TestCase):

    def setUp(self):

        user = User(username='gopi', password='ap35J8215#')
        user.save()

        # get Django authentication user object whose username is 'gopi'.
        user = User.objects.get(username='gopi')
      
        print(user)
        
        client = APIClient()
        self.refresh = AccessToken.for_user(user)
        print("under setup")

    
    def htest_book_with_token(self):
        '''
        Requirement: test the book request using authorized jwt tokens
        
        Procedure:
        1) use the generated jwt token in setup method
        2) request for get method with book url with jwt token in the headers
        
        verification:
        1) the get method should response with 200
        '''
        response = requests.get('http://127.0.0.1:8000/book/', headers={'Authorization': 'Bearer {}'.format(self.refresh)})
        self.assertEqual(response.status_code, 200)

    def htest_book_with_false_token(self):
        '''
        Requirement: verify book api is not acceptin false jwt tokens
        
        Procedure:
        1) Use some random string as jwt token
        2) hit the book api get method using random string and use the jwt 
        
        verification:
        1) book api should respond with 401 status_code
        '''
        self.fake_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        response = requests.get('http://127.0.0.1:8000/book/', headers={'Authorization': 'Bearer {}'.format(self.fake_token)})
        self.assertEqual(response.status_code, 401)

    def htest_book_save_data(self):
        '''
        Requirement: Check book api is able to save data with post method
        
        Procedure:
        1) Craete random book data with fields
            sample data: {"name": 'jaga', 'price': '45.6', 'author': 'mani', 'publisher': 'jack'}
        2) post the data to the book api
        
        Verification
        1) api should return 201 created status code
        '''
        data = {"name": 'jaga', 'price': '45.6', 'author': 'mani', 'publisher': 'jack'}
        response = requests.post('http://127.0.0.1:8000/book/', data= data, headers={'Authorization': 'Bearer {}'.format(self.refresh)}, )
        print(response.content)
        self.assertEqual(response.status_code, 201)
    
    def gtest_book_verify_saved_data(self):
        '''
        Requirement: Given random book details and save the data, data base should contain the random 
        generated book name
        
        Procedure:
        1) create random book data
        2) post the book data 
        
        Verification:
        1) db should contain random book data which is posted 
        '''
        
        book_name = 'book_name' + str(random.randint(1,10000)) # created random book name with randint
        
        data = {"name": book_name, 'price': '45.6', 'author': 'mani', 'publisher': 'jack'}
        
        # posting the data to book 
        requests.post('http://127.0.0.1:8000/book/', data= data, headers={'Authorization': 'Bearer {}'.format(self.refresh)}, )
        
        # getting the data 
        response = requests.get('http://127.0.0.1:8000/book/', headers={'Authorization': 'Bearer {}'.format(self.refresh)})

        book_list = response.json()
        
        # getting out the book names using list comphrehension and verify the book name 
        book_names = [i['name'] for i in book_list]
        if book_name not in book_names:
            self.fail("condition not met")
                

    def ftest_book_method_fail_with_invalid_price(self):
        '''
        Requirement: send characters to the price field and api should not save the data
        
        Procedure:
        1) create random book data 
        2) use some random string in the price field
        3) submit the data to the book api with post method
        
        verification:
        1) api should throw 400 bad request satus code 
        '''
        data = {"name": "sample 1", 'price': 'hello', 'author': 'mani', 'publisher': 'jack'}

        # posting the data to book 
        response = requests.post('http://127.0.0.1:8000/book/', data= data, headers={'Authorization': 'Bearer {}'.format(self.refresh)}, )

        self.assertEqual(response.status_code, 400)

    def htest_rating_to_save_data(self):
        '''
        Requirement: send rating data and save
        
        Procedure:
        1) create rating data with number / decimal
        2) send with book id
        
        Verification:
        1) verify rating saved to particular book
        '''
        book_name = 'book_name' + str(random.randint(1,10000)) # created random book name with randint
        data = {"name": book_name, 'price': '45.6', 'author': 'mani', 'publisher': 'jack'}
        # posting the data to book 
        response = requests.post('http://127.0.0.1:8000/book/', data= data, headers={'Authorization': 'Bearer {}'.format(self.refresh)}, )
        #print(response.content)
        book_id = response.json()["id"]
        rating_data = {"book_name": book_id, "rating_data": 2.5}
        response = requests.post('http://127.0.0.1:8000/rating/', data= rating_data, headers={'Authorization': 'Bearer {}'.format(self.refresh)}, )
        self.assertEqual(response.status_code, 201)

    def test_rating_not_to_save_with_false_id(self):
        '''
        Requirement: send id which is not there in the db
        and rating should not save the data
        
        Procedure:
        1) create rating data with non existing book_id
        2) send the data
        
        Verification:
        1) should not save the data
        '''
        rating_data = {"book_name": 10002, "rating_data": 2.5}
        response = requests.post('http://127.0.0.1:8000/rating/', data= rating_data, headers={'Authorization': 'Bearer {}'.format(self.refresh)}, )
        self.assertEqual(response.status_code, 400)

