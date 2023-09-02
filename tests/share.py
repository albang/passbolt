import unittest
import os
from passbolt.passbolt import passbolt

key = os.environ.get('key')
passphrase = os.environ.get('passphrase')
uri = os.environ.get('uri')

Passbolt = passbolt(privatekey=key, passphrase=passphrase, apiurl=uri)


class TestPasswordMethods(unittest.TestCase):

    def setUp(self) -> None:
        password = Passbolt.createpassword("password_to_share", "chut")

    # def tearDown(self) -> None:
    #    Passbolt.deletepassword("password_to_share")

    def test_0_sharepassword(self):
        password = Passbolt.sharepassword("password_to_share", users=[ "alban@garrigue.me" ],permission="Read")
        self.assertEqual(password, "The operation was successful.")

    def test_1_share_already_shared_password(self):
        password = Passbolt.sharepassword("password_to_share", users=[ "alban@garrigue.me" ],permission="Owner")
        self.assertEqual(password, "The operation was successful.")

if __name__ == '__main__':
    unittest.main()