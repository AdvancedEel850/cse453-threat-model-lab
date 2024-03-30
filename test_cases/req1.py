# this will test requirement 1: Program must have a variable which controls what permissions each user has
# just test to make sure that each person in the database has a permission setting


# this is just to make the unittest thing to work
import sys
sys.path.insert(1, 'C:/Users/Junky/Desktop/Winter_2024/computer_security/wk12/cse453-threat-model-lab/test_cases')



# this is for the file itself
import unittest
from messenger import interact as i


# making a function to look at all the users permisions, and see if they are in the 
# list of available user permissions.
def determine_security():
    access = i.control.Control()

    
    for user in i.userlist:
        if (user[2] not in access.get_control()):
            return False
        else:
            return True
        
# making a class so unittest works
class test_req1(unittest.TestCase):
    def test_sec(self):
        self.assertTrue(determine_security)

# running class (the test that the unittest uses)
test = test_req1()
test.test_sec()

if __name__ == "__main__":
    unittest.main()
