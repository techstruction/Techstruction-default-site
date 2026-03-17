import os
import sys

def main():
    """Scaffolds a new frontend component directory with boilerplate."""
    if len(sys.argv) < 2:
        print("Usage: python3 execution/frontend_factory.py <component_name>")
        sys.exit(1)
        
    component_name = sys.argv[1].lower().replace(" ", "_")
    base_path = f"frontend-design/{component_name}"
    
    os.makedirs(base_path, exist_ok=True)
    
    files = {
        "index.html": "<!DOCTYPE html>\n<html>\n<head>\n    <link rel='stylesheet' href='style.css'>\n</head>\n<body>\n    <div id='app'></div>\n    <script src='script.js'></script>\n</body>\n</html>",
        "style.css": ":root {\n    --primary: #000;\n}\n\nbody {\n    margin: 0;\n    font-family: sans-serif;\n}",
        "script.js": "// Client-side logic\nconsole.log('Component Loaded');"
    }
    
    for filename, content in files.items():
        file_path = os.path.join(base_path, filename)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content)
            print(f"Created {file_path}")
        else:
            print(f"Skipped {file_path} (already exists)")

if __name__ == "__main__":
    main()
