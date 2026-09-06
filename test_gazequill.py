# test_gazequill.py
"""
Tests for GazeQuill module.
"""

import unittest
from gazequill import GazeQuill

class TestGazeQuill(unittest.TestCase):
    """Test cases for GazeQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GazeQuill()
        self.assertIsInstance(instance, GazeQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GazeQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
