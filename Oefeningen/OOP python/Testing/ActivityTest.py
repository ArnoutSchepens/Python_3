
import unittest

from activities import eat, nap, is_funny, laugh


class ActivityTests(unittest.TestCase):

    def test_eat_healthy(self):
        '''
        Eat should have a positive message for healthy eating
        '''
        self.assertEqual(eat("broccoli", is_healty=True),
                         "I'm eating broccoli, because my body is a temple")

    def test_eat_unhealthy(self):
        '''
        Eat should have a positive message for healthy eating
        '''
        self.assertEqual(eat("pizza", is_healty=False),
                         "I'm eating pizza, because YOLO")

    def test_eat_healthy_bool(self):
        """ is_healthy must be a bool """
        with self.assertRaises(ValueError):
            eat("pizza", is_healty = "Who cares",)
        


    def test_nap_short(self):
        """ Short naps should be refreshing """
        self.assertEqual(nap(1), "I slept enough. That felt great!")

    def test_nap_long(self):
        """ Long naps should be discouraging """
        self.assertEqual(nap(3), "I slept too long!")

    def test_is_funny_tim(self):
        self.assertEqual(is_funny("Tim"), False, "Tim should not be funny")
        # self.assertFalse(is_funny("Tim"), "Tim should not be funny")

    def test_is_funny_anyone_else(self):
        """ Anyone but Tim should be funny """
        self.assertTrue(is_funny("Blue"), "Blue should be funny")
        self.assertTrue(is_funny("Tammy"), "Tammy should be funny")
        self.assertTrue(is_funny("Sven"), "Sven should be funny")

    def test_laugh(self):
        self.assertIn(laugh(), ("Lol", "Haha", "Tehehe"))

if __name__ == "__main__":
    unittest.main()
