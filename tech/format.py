import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List
from slugify import slugify

from tech.lingo import Lingo
from tech.load import load_lingos

def format():
    files: Dict[str, List[Lingo]] = defaultdict(list)
    for lingo in load_lingos():

        files[f"{lingo.category}-{lingo.language}"].append(lingo)
    lingos = Path("lingos")
    for t, lists in files.items():
        jsons = [ll.asdict() for ll in sorted(lists, key=lambda lng: slugify(lng.term))]
        with open(lingos /f"{t}.json", "wt", encoding="utf8") as w:
            json.dump(jsons, w, indent=2,ensure_ascii=False)

if __name__ == '__main__':
    format()
