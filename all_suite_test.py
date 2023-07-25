import unittest

from unittest.loader import makeSuite

from test_cases.clear_button import TestClearButtonAddPlayer
from test_cases.filling_add_a_player_form import TestFillingAddPlayerForm
from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage
from test_cases.open_add_a_player_form import TestAddPlayer
from test_cases.sign_out import TestSignOut


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest((makeSuite(Test)))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestFillingAddPlayerForm))
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestClearButtonAddPlayer))
   test_suite.addTest(makeSuite(TestSignOut))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
