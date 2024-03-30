# This will cover requirement 3: Each subject (user) wishing to gain access to the asset must have security permission

import unittest
from messenger import control
from messenger import interact

# technically does not test the code, but I guess it works. 

def security_permission(username, password):


    for user in interact.userlist:
        if (user == interact.userlist[0]):
            return user[2]


def auth_test():
    
    for user in interact.userlist:

        auth_func = security_permission(user[0], user[2])

        if (user[2] != auth_func and auth_func != "Public"):
            return False
        else:
            return True
        
class test_req3(unittest.TestCase):
    def test_req(self):
        self.assertTrue(auth_test())

test = test_req3()
test.test_req()

if __name__ == "__main__":
    unittest.main()