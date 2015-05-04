import re

size_units = {
  'k': 10**3,
  'm': 10**6,
  'g': 10**9,
  'K': 2**10,
  'M': 2**20,
  'G': 2**30,
  'KiB': 2**10,
  'MiB': 2**20,
  'GiB': 2**30,
}

class FilterModule(object):
    '''Provide Jinja2 filters for Ansible
    
    Provide handy conversions between/to file size representations. 
    '''
    
    @staticmethod
    def from_filesize(s):
        '''Parse a human-friendly file size'''
        match_number = re.match('[\d]+([.]\d+)?', s)
        if not match_number:
            raise ValueError('Failed to parse a number')
        n = float(match_number.group(0))
        u = s[match_number.end():].strip()
        if not u in size_units:
            raise ValueError('Cannot recognize unit %s' % (u))
        return n * size_units[u] 
    
    @staticmethod
    def as_filesize(n, u='K', precision=1):
        '''Convert a number to a human-friendly file size'''
        if not u in size_units:
            raise ValueError('Cannot recognize unit %s' % (u))
        n = float(n) / size_units[u]
        return '%.*f%s' %(n, precision, u)

    def filters(self):
        return {
           'from_filesize': self.from_filesize,
           'as_filesize': self.as_filesize,
        }
