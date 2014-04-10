import random
import string
import hashlib

class SaltHasher(object):
    """If salt/hashed_pw given, validate instead"""
    def __init__(self, *args, **kwargs):
        self.pws = args
        if "salt" in kwargs and "hashed_pw" in kwargs:
            self.is_validating = True
            self.salt = kwargs['salt']
            self.hashed = kwargs['hashed_pw']
        else:
            self.is_validating = False
            self.salt = "".join(random.choice(string.letters) for x in xrange(5))
            self.hashed = hashlib.sha256("".join(self.pws) + self.salt).hexdigest()

    def get_result(self):
        if self.is_validating:
            return hashlib.sha256("".join(self.pws) + self.salt).hexdigest() == self.hashed
        else:
            return (self.hashed, self.salt)