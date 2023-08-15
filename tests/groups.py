import unittest
import os
from passbolt.passbolt import passbolt

#key = open(os.environ.get('keypath'), "r").read()
#passphrase = os.environ.get('passphrase')
#uri = os.environ.get('uri')

#Passbolt = passbolt(key, passphrase, uri)

key = os.environ.get('KEY')
passphrase = os.environ.get('PASSPHRASE')
uri = os.environ.get('URI')

Passbolt = passbolt(privatekey=key, passphrase=passphrase, apiurl=uri)

class TestPasswordMethods(unittest.TestCase):

    def test_0_creategroup(self):
        group = Passbolt.creategroup("pytest", ["alban+ci@garrigue.me"], ["alban+ci2@garrigue.me"])
        self.assertEqual(group, "The group has been added successfully.")

    def test_1_getgroup(self):
        group = Passbolt.getgroup("pytest")
        self.assertEqual(group.name, "pytest")

    def test_2_updategroup(self):
        group = Passbolt.updategroup("pytest", ["s1@a.com"], ["s2@a.com"])
        self.assertEqual(group, "The operation was successful.")

    def test_3_deletegroup(self):
        group = Passbolt.deletegroup("pytest")
        self.assertEqual(group, "The group was deleted successfully.")


if __name__ == '__main__':
    unittest.main()