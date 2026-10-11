import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [ROOT / "Copy of podcast_listening_time.ipynb", ROOT / "Calories__Prediction.ipynb"]

class KaggleNotebookSetupTests(unittest.TestCase):
    def test_notebooks_are_valid_json_with_no_saved_outputs(self):
        for path in NOTEBOOKS:
            with self.subTest(notebook=path.name):
                notebook = json.loads(path.read_text(encoding="utf-8"))
                self.assertTrue(notebook.get("cells"))
                for cell in notebook["cells"]:
                    if cell.get("cell_type") == "code":
                        self.assertIsNone(cell.get("execution_count"))
                        self.assertFalse(cell.get("outputs"))

    def test_notebook_uses_local_data_and_not_a_fixed_drive_path(self):
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        source = "\n".join(
            "".join(cell.get("source", []))
            for cell in notebook["cells"] if cell.get("cell_type") == "code"
        )
        self.assertIn("DATA_DIR_CANDIDATES", source)
        self.assertIn("FileNotFoundError", source)
        self.assertNotIn("/content/drive/MyDrive/", source)
        self.assertNotIn("google.colab", source)
        self.assertIn("submission.csv", source)

    def test_readme_explains_competition_data_not_redistributed(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("not redistributed", readme.lower())
        self.assertIn("train.csv", readme)
        self.assertIn("test.csv", readme)

if __name__ == "__main__":
    unittest.main()
