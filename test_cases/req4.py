# this will cover requirement 4: The Program must evaluate if the user is allowed to gain access to the asset.

from messenger import control
import unittest


class test_req4():

    control.Control.read_access()
    control.Control.write_access()


    asset_levels = control.Control.get_control()

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
        self.assertTrue(control.Control.read_access())