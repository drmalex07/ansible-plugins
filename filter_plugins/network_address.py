
class FilterModule(object):
    '''Provide additional network-address--related Jinja2 filters for Ansible'''
    
    @staticmethod
    def ipv4_to_cidr(address, netmask):
        assert netmask, 'A netmask is required' 
        netmask_bits = sum([
            bin(int(x)).count('1') for x in netmask.split('.')])
        return '%s/%d' % (address, netmask_bits)

    def filters(self):
        return {
           'ipv4_to_cidr': self.ipv4_to_cidr,
        }
