from types import SimpleNamespace
from . import errors
import logging

log = logging.getLogger(__name__)

class Locker:
    '''Simple locker that can be unlocked with multiple picks'''
    def __init__(self):
        self.unlocked = False

        class LockpickStorage(SimpleNamespace):
            pass

        self.lockpicks = LockpickStorage()
        log.debug("Initialized Locker instance")

    def get_status(self):
        '''Return locker's status'''
        log.debug(f"Returning current locker's status: {self.unlocked}")
        return self.unlocked

    def get_lockpicks(self):
        '''Return lockpicks'''
        log.debug(f"Returning current lockpicks: {self.lockpicks}")
        return vars(self.lockpicks)

    def check_lockpick(self, name:str):
        '''Checks if lockpick exists in storage. Returns bool depending on status'''
        if getattr(self.lockpicks, name, None) == None:
            log.debug(f"{name} doesnt exist in storage")
            return False

        log.debug(f"{name} exists in storage")
        return True

    def get_lockpick(self, name:str):
        '''Get specified lockpick. If not in storage - will throw exception'''
        if not self.check_lockpick(name):
            raise errors.LockpickDoesntExist(name)

        log.debug(f"Returning lockpick {name}")
        return getattr(self.lockpicks, name)

    def add_lockpick(self, name:str, status:bool = False):
        '''Add lockpick to the lockpicks storage'''
        if self.check_lockpick(name):
            raise errors.LockpickExists(name)

        setattr(self.lockpicks, name, status)
        log.debug(f"Succesfully added {name} to the lockpicks storage")

    def toggle_lockpick(self, name:str, status:bool = None):
        '''Toggle existing lockpick. Expect lockpick to already exist in storage.
        Without specified status, will flip current lockpick values'''
        if not self.check_lockpick(name):
            raise errors.LockpickDoesntExist(name)

        if status == None:
            if getattr(self.lockpicks, name):
                status = False
            else:
                status = True

        setattr(self.lockpicks, name, status)
        log.debug(f"Successfully toggled status of {name} lockpick to {status}")

    def picklock(self):
        '''Check current storage against keys. If all True - set self.unlocked to
        True, else - to False'''
        storage_items = vars(self.lockpicks)
        for item in storage_items:
            if not storage_items[item]:
                self.unlocked = False
                log.debug(f"Storage is locked: {item} is incorrect lockpick")
                return self.unlocked

        self.unlocked = True
        log.debug("Storage has been unlocked: all lockpicks has matched")
        return self.unlocked
