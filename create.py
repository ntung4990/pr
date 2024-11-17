import os

folders = [
    ".github/workflows",
    ".github/ISSUE_TEMPLATE",
    "src/assets/css",
    "src/assets/js",
    "src/assets/images",
    "src/components",
    "src/pages",
    "src/services",
    "src/utils",
    "public",
    "tests",
    "scripts"
]

files = [".env", ".gitignore", "package.json", "README.md", "LICENSE", "src/index.js", "public/index.html"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, 'a').close()

print("Project structure created!")
