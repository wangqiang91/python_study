import unittest

def add(x,y):
    return x + y

class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("大胖胖")
    @classmethod
    def tearDownClass(cls) -> None:
        print("小胖胖")
    def setUp(self) :
        print("爱吃哈密瓜")
    def tearDown(self):
        print("二胖")
    @unittest.skip("跳过啦")
    def test01_add(self):
        result = add(1,1)
        self.assertEqual(result,2)
    def test02_add(self):
        result = add(2,2)
        self.assertNotEqual(result,4.12)
if __name__ == "__main__":
    unittest.main()