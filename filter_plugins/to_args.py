
def _flatten_items(items):
    ''' A simple flattening routine based on the type of each value item.'''
    res = {}
    for k,v in items:
        # Detect value type
        it1 = None
        if isinstance(v, dict):
            it1 = v.iteritems()
        elif isinstance(v, list) or isinstance(v, tuple):
            it1 = enumerate(v)
        # Decide if we must descent
        if it1:
            res1 = _flatten_items(it1)
            for k1,v1 in res1.items():
                res[(k,)+k1] = v1
        else:
            res[(k,)] = v
    return res

class FilterModule(object):
    '''Provide additional Jinja2 filters for Ansible'''

    @staticmethod
    def to_args(d):
        d1 = _flatten_items(d.iteritems())
        return ' '.join(['--%s=%s' % ('-'.join(k), v) for k, v in d1.items()])
    
    def filters(self):
        return {
           'to_args': self.to_args,
        }
