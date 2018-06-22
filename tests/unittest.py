# import unittest, os, json

# class BaseTestCase(unittest.TestCase):
#     """This class represents the base test case"""

#     def setUp(self):
#         """Define test variables and initialize app."""
#         # self.app = create_app(config_name="testing")
#         self.app = app
#         self.client = self.app.test_client

#         # binds the app to the current context
#         with self.app.app_context():
#             # create all tables
#             db.create_all()

#     def test_register_user(self):
#         test_client =self.client()
#         res = test_client.post('/register', 
#             data={'email':'ganesh.negi@3pillarglobal.com', 'password':'login@123', 'first_name':'ganesh', 'last_name':'negi'}
#             )
#         self.assertEquals(res.status_code, 201)

#     # def test_valid_login(self):
#     #     test_client = self.client()
#     #     res = test_client.post('/login', data={'email':'ganesh.negi@3pillarglobal.com', 'password':'login@123'})
#     #     self.assertEquals(res.status_code, 200)

        
#     def tearDown(self):
#         """teardown all initialized variables."""
#         with self.app.app_context():
#             # drop all tables
#             db.session.remove()
#             db.drop_all()

# if __name__ == "__main__":
#     unittest.main()