import json

def save_build(build, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(build, f, ensure_ascii=False, indent=2)

def load_build(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)