
class FilterModule(object):
    '''Provide Jinja2 filters for Ansible
    
    The filters below are simplified wrappers on dict/list comprehension operations. 
    '''
    
    @staticmethod
    def map_keys(d, keys, source_path=None):
        '''Map keys on values from a set of (possibly nested) keys in an existing dict.
        
        If `source_path` is supplied, then it is expected to be a format string and 
        contain placeholder for the current key item, e.g.:
        
        >>>  filter_by_keys(d, ['aa', 'bb']) # visits actual and explicitly-defined keys
        >>>  filter_by_keys(d, ['aa', 'bb'], 'someprefix-{0}')   # visits actual keys 
        >>>  filter_by_keys(d, ['aa', 'bb'], 'prefix-{0}-suffix.version')  # visits nested keys
        
        '''
        
        assert isinstance(keys, (list, set)), 'Expected an iterable'
        res = None
        if isinstance(source_path, str):
            res = {k: reduce(lambda z,k: z.get(k), source_path.format(k).split('.'), d) 
                for k in keys}
        else:
            res = {k: d.get(k) for k in keys}
        return res

    def filters(self):
        return {
           'map_keys': self.map_keys,
        }
