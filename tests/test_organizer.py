import unittest
import os
import shutil
from BOFT import organize_files_by_type

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_files"
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create test files
        with open(os.path.join(self.test_dir, "test.txt"), "w") as f:
            f.write("Test text file")
        with open(os.path.join(self.test_dir, "test.jpg"), "wb") as f:
            f.write(b"Test image file")
        
    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        
    def test_organize_files(self):
        organize_files_by_type(self.test_dir, silent=True)
        
        # Check if files are moved to correct categories
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Documents", "test.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Images", "test.jpg")))
        
    def test_empty_directory(self):
        # Remove all files
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
            
        result = organize_files_by_type(self.test_dir, silent=True)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
