import nbformat

file_path = "./notebooks/prompt_token_counts.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

if 'widgets' in nb['metadata']:
    print("Found corrupted widgets metadata. Removing it.")
    del nb['metadata']['widgets']

with open(file_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook cleaned.")
