import os


def resource_path(relative_path):
    base_path = os.path.abspath("../media")
    return os.path.join(base_path, relative_path)
