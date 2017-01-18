from abc import ABCMeta, abstractmethod


class LightSource(object):
    """Abstract superclass"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def turn_light_on(self):  # abstract method
        pass

    @abstractmethod
    def turn_light_off(self):
        pass
