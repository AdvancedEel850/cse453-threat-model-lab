# this will test requirement 1: Program must have a variable which controls what permissions each user has
# just test to make sure that each person in the database has a permission setting

import messenger.interact as i
import messenger.control as c


access = c.Control()

for user in i.userlist:
    if (user[2] is not in )