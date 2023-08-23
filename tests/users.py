import unittest
import os
from passbolt.passbolt import passbolt

key = os.environ.get('key')
passphrase = os.environ.get('passphrase')
uri = os.environ.get('uri')

Passbolt = passbolt(privatekey=key, passphrase=passphrase, apiurl=uri)


class TestPasswordMethods(unittest.TestCase):

    def test_0_createuser(self):
        user = Passbolt.createuser("alban+ci@garrigue.me", "Test", "Ing")
        self.assertEqual(user, "The user was successfully added. This user now need to complete the setup.")

    def test_1_getuser(self):
        user = Passbolt.getuser("alban+ci@garrigue.me")
        self.assertEqual(user.username, "alban+ci@garrigue.me")

    def test_2_updateuser(self):
        user = Passbolt.updateuser("alban+ci@garrigue.me", "First", "Admin", True)
        self.assertEqual(user, "The user has been updated successfully.")


    def test_3_deleteuser(self):
        user = Passbolt.deleteuser("alban+ci@garrigue.me")
        self.assertEqual(user, "The user has been deleted successfully.")


if __name__ == '__main__':
    unittest.main()