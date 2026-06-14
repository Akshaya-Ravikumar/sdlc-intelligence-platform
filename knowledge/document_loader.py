from pathlib import Path
from pypdf import PdfReader
import json
import yaml
import pandas as pd

def load_document(file_path):

    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        reader = PdfReader(path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        return text

    elif suffix in [".txt", ".md"]:
        return path.read_text(
            encoding="utf-8"
        )

    elif suffix in [".yaml", ".yml"]:
        return path.read_text(
            encoding="utf-8"
        )

    elif suffix == ".json":
        data = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

        return json.dumps(
            data,
            indent=2
        )

    elif suffix == ".csv":
        df = pd.read_csv(path)
        return df.to_string()

    else:
        raise ValueError(
            f"Unsupported file type: {suffix}"
        )