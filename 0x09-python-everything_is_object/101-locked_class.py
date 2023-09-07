#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        error_message = "'LockedClass' object has no attribute '{}'"
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(error_message.format(name))
