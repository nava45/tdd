import os


class RemovalService(object):
    """A service for removing objects from the filesystem."""
    
    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
