
class FilterModule(object):
    '''Provide Jinja2 filters for Ansible
    
    The filters below are simplified wrappers on dict/list comprehension operations. 
    '''
    
    @staticmethod
    def list_values(d):
        '''List values from a dict'''
        return d.values()
    
    @staticmethod
    def list_keys(d):
        '''List keys from a dict'''
        return d.keys()
    
    @staticmethod
    def to_kv_pairs(d, sep=','):
        '''Format a dict as KV pairs'''
        f = lambda k, v: '{0}={1}'.format(k, v) if v else str(k)
        return sep.join([f(k, v)
            for k, v in d.items() if (not v or isinstance(v, basestring))])

    @staticmethod
    def map_keys(d, keys, source_path=None, path_delimiter='.'):
        '''Map keys on values from a set of (possibly nested) keys in an existing dict.
        
        If `source_path` is supplied, then it is expected to be a format string and 
        contain placeholder for the current key item, e.g.:
        
        >>>  map_keys(d, ['aa', 'bb']) # visits actual and explicitly-defined keys
        >>>  map_keys(d, ['aa', 'bb'], 'someprefix-{0}')   # visits actual keys 
        >>>  map_keys(d, ['aa', 'bb'], 'prefix-{0}-suffix.version')  # visits nested keys
        
        '''
        
        assert isinstance(keys, (list, set)), 'Expected an iterable'
        res = None
        if isinstance(source_path, str):
            f = lambda z,k: z.get(k) if z else None
            res = {k: reduce(f, source_path.format(k).split(path_delimiter), d) 
                for k in keys}
        else:
            res = {k: d.get(k) for k in keys}
        return res

    def filters(self):
        return {
           'map_keys': self.map_keys,
           'list_values': self.list_values,
           'list_keys': self.list_keys,
           'to_kv_pairs': self.to_kv_pairs,
        }
