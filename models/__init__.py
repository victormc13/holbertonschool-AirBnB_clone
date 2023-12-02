#!usr/bin/python3

from models.engine.file_storage import FileStorage
from models.user import User

storage = FileStorage()
storage.reload()
