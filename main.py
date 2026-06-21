from pathlib import Path


dir_path = Path(__file__).parent
target_extensions = {".md", ".py"}

# Loop through top-level items
for entry in dir_path.iterdir():
    if entry.is_file() and entry.suffix.lower() in target_extensions:
        print(f"--- Contents of: {entry.name} ---")
        
        # Read the file text directly
        try:
            content = entry.read_text(encoding='utf-8')
            print(content)
        except (PermissionError, UnicodeDecodeError):
            print("oops")
