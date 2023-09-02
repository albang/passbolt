import unittest
import os
from passbolt.passbolt import passbolt

key = os.environ.get('key')
passphrase = os.environ.get('passphrase')
uri = os.environ.get('uri')

Passbolt = passbolt(privatekey=key, passphrase=passphrase, apiurl=uri)

class TestPasswordMethods(unittest.TestCase):
    def setUp(self) -> None:
        user = Passbolt.createuser("user@example.com", "Test", "Ing")
        user2 = Passbolt.createuser("user2@example.com", "Test", "Ing")

    def tearDown(self) -> None:
        Passbolt.deleteuser("user@example.com")

    def test_0_creategroup(self):
        group = Passbolt.creategroup("pytest_action", ["alban@garrigue.me"], [])
        self.assertEqual(group, "The group has been added successfully.")

    def test_1_getgroup(self):
        group = Passbolt.getgroup("pytest_action")
        self.assertEqual(group.name, "pytest")

    def test_2_updategroup(self):
        group = Passbolt.updategroup("pytest_action", [], ["user2@example.com"])
        self.assertEqual(group, "The operation was successful.")

    def test_3_deletegroup(self):
        group = Passbolt.deletegroup("pytest_action")
        self.assertEqual(group, "The group was deleted successfully.")


if __name__ == '__main__':
    unittest.main()