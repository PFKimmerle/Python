import importlib.metadata

# Replace this line:
# [int(part) for part in marshmallow.__version__.split(".") if part.isdigit()]

# With this line:
[int(part) for part in importlib.metadata.version("marshmallow").split(".") if part.isdigit()]