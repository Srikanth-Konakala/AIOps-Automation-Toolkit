import unittest
# We import your function from the main.py file
from main import analyze_log

class TestToolkit(unittest.TestCase):
    
    def test_error_count(self):
        # We tell the robot: "Go check server.log"
        result = analyze_log('server.log')
        
        # We tell the robot: "The answer MUST be 2. If not, raise an alarm."
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()