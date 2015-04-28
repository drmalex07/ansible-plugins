from netaddr import IPAddress, IPNetwork


class FilterModule(object):
    '''Provide additional network-address--related Jinja2 filters for Ansible'''
    
    @staticmethod
    def ipv4_to_cidr(address, netmask=None, prefixlen=None):
        a = IPAddress(address)
        n = IPNetwork(a)
        if netmask:
            assert prefixlen is None, 'Cannot provide both netmask and prefixlen'
            m = IPAddress(netmask)
            assert m.is_netmask(), 'A valid netmask is required' 
            n.prefixlen = m.netmask_bits() 
        else:
            assert prefixlen, 'Provide either netmask or prefixlen'
            n.prefixlen = int(prefixlen)
        return str(n.cidr)

    @staticmethod
    def ipv4_in_cidr(address, network):
        return (IPAddress(address) in IPNetwork(network))

    def filters(self):
        return {
           'ipv4_to_cidr': self.ipv4_to_cidr,
           'ipv4_in_cidr': self.ipv4_in_cidr,
        }
