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
        user = Passbolt.sharepassword("alban@garrigue.me", "Test", "Ing")
        self.assertEqual(user, "The user was successfully added. This user now need to complete the setup.")


if __name__ == '__main__':
    unittest.main()