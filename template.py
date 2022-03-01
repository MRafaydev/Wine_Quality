import os

# dirs paths
dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src",
]

# Make dir
for dir_ in dirs:
    os.makedirs(dir_ , exist_ok=True)
    with open (os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

# files path
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py"),
]

# Make files
for files_ in files:
    with open (files_, "w") as f:
        pass