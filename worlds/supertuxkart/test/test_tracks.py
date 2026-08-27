from .bases import STKTestBase

class TestLocationLogic(STKTestBase):

    run_default_tests = False

    def text_track_access(self):
        with self.subTest("Test track reachability for pre-unlocked tracks"):
            self.assertTrue(self.can_reach_location("Cornfield Crossing Easy"))

        with self.subTest("Test track reachability for locked difficulties"):
            self.collect_by_name("Minigolf")
            self.assertTrue(self.can_reach_location("Minigolf Easy"))

        with self.subTest("Test track reachability for locked tracks"):
            self.assertFalse(self.can_reach_location("Mines Easy"))