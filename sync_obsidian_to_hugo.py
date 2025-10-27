#!/usr/bin/env python3
import os
import re
import shutil
import argparse
from pathlib import Path

# Lines starting with these prefixes will be removed
REMOVE_PREFIXES = ["inspo:"]

# Match Obsidian links like [[path|label]] or [[path]]
OBSIDIAN_LINK_PATTERN = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

def clean_target_dir(target: Path):
    """Delete all files and folders in the target directory."""
    if not target.exists():
        raise FileNotFoundError(f"❌ Target folder does not exist: {target}")
    for item in target.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

def transform_content(content: str, base_url: str, strip_pattern: str) -> str:
    """Remove unwanted lines and transform Obsidian links."""
    base_url = "/" + base_url.strip("/")

    # Remove lines starting with any of the REMOVE_PREFIXES
    lines = content.splitlines()
    filtered = [
        line for line in lines
        if not any(line.strip().startswith(prefix) for prefix in REMOVE_PREFIXES)
    ]
    content = "\n".join(filtered)

    def replace_link(match):
        raw_path = match.group(1).strip().replace("\\", "/")
        label = match.group(2).strip() if match.group(2) else Path(raw_path).name

        # Strip configurable prefix pattern if provided
        if strip_pattern:
            raw_path = re.sub(strip_pattern, "", raw_path, flags=re.IGNORECASE)

        url = f"{base_url}/{raw_path}".replace("//", "/")
        return f"[{label}]({url})"

    return OBSIDIAN_LINK_PATTERN.sub(replace_link, content)

def copy_and_transform(source: Path, target: Path, base_url: str, strip_pattern: str):
    """Recursively copy and transform markdown and asset files."""
    for root, _, files in os.walk(source):
        rel_path = Path(root).relative_to(source)
        target_dir = target / rel_path
        target_dir.mkdir(parents=True, exist_ok=True)

        for file in files:
            src_file = Path(root) / file
            dst_file = target_dir / file

            if src_file.suffix.lower() == ".md":
                with open(src_file, "r", encoding="utf-8") as f:
                    content = f.read()
                transformed = transform_content(content, base_url, strip_pattern)
                with open(dst_file, "w", encoding="utf-8") as f:
                    f.write(transformed)
            else:
                shutil.copy2(src_file, dst_file)

def main():
    parser = argparse.ArgumentParser(
        description="Generic sync tool for transforming Obsidian markdown to Hugo-compatible format."
    )
    parser.add_argument("source", help="Path to the source folder (e.g., Obsidian notes)")
    parser.add_argument("target", help="Path to the target Hugo content folder (must exist)")
    parser.add_argument(
        "--base-url",
        default="/",
        help="Base URL prefix for generated links (default: '/')"
    )
    parser.add_argument(
        "--strip-pattern",
        default="",
        help="Regex pattern to strip from the start of Obsidian link paths (e.g., '^Blog/posts/')"
    )

    args = parser.parse_args()
    source = Path(args.source).resolve()
    target = Path(args.target).resolve()

    if not source.exists():
        print(f"❌ Source folder not found: {source}")
        return

    if not target.exists():
        print(f"❌ Target folder not found: {target}")
        return

    print(f"🧹 Cleaning target: {target}")
    clean_target_dir(target)

    print(f"🔄 Copying & transforming from {source} → {target}")
    copy_and_transform(source, target, args.base_url, args.strip_pattern)

    print("✅ Done!")

if __name__ == "__main__":
    main()
