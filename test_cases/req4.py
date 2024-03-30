# this will cover requirement 4: The Program must evaluate if the user is allowed to gain access to the asset.

from messenger import control
import unittest


class test_req4(unittest.TestCase):

    # control.Control.read_access()
    # control.Control.write_access()


    asset = control.Control()
    asset_levels = asset.get_control()


    users = [
        ['bob', asset_levels[0]], 
        ['billy', asset_levels[1]], 
        ['joe', asset_levels[2]], 
        ['sam', asset_levels[3]]
        ]
    
    assets = [
        ['txt', asset_levels[0]], 
        ['email', asset_levels[1]], 
        ['call', asset_levels[2]], 
        ['letter', asset_levels[3]]
    ]
    
    def test_req(self):

        # tests to see if the permissions are the same for the user and the asset
        # mostly just to test if this code approach works so I can use it later
        self.assertTrue(test_req4.users[1][1] == test_req4.assets[1][1])
        
    def test_req2(self):

        # this just tests to see if the permissions for the specified user
        # are at a lower index than than the permssion for the specified asset
        self.assertTrue(test_req4.asset_levels.index(test_req4.users[2][1]) 
                        <
                        test_req4.asset_levels.index(test_req4.assets[3][1]))
        
    def test_req3(self):

        # same test, just moved down one
        self.assertTrue(test_req4.asset_levels.index(test_req4.users[1][1]) 
                        <
                        test_req4.asset_levels.index(test_req4.assets[2][1]))



test = test_req4()
test.test_req()


if __name__ == '__main__':
    unittest.main()