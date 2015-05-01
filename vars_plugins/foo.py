class VarsModule(object):
    '''Loads variables for groups and/or hosts'''

    def __init__(self, inventory):
        self.inventory = inventory
        self.inventory_basedir = inventory.basedir()


    def run(self, host, vault_password=None):
        '''For backwards compatibility, when only vars per host were retrieved
        This method should return both host specific vars as well as vars
        calculated from groups it is a member of
        '''
        return {}


    def get_host_vars(self, host, vault_password=None):
        '''Provide host-specific variables'''
        host.set_variable('foo', {'bar': 'always', 'baz': 99})
        return {}


    def get_group_vars(self, group, vault_password=None):
        '''Provide group-specific variables'''
        return {}

