# custom exceptions

class LockyException(Exception):
    '''Parent exception for everything below'''
    pass

class LockpickExists(Exception):
    '''Exception thrown when action expects lockpick to be non-existant in
    storage, but its already there'''
    def __init__(self, lockpick:str):
        message = f"{lockpick} already exists in storage"
        super().__init__(message)

class LockpickDoesntExist(Exception):
    '''Exception thrown when action expects lockpick to exist in storage,
    but its not there'''
    def __init__(self, lockpick:str):
        message = f"{lockpick} doesnt exist in storage"
        super().__init__(message)
