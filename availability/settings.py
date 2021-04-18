

class AvailabilitySettings(object):

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + ['availability']


default = AvailabilitySettings
