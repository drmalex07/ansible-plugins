from netaddr import IPAddress, IPNetwork


class FilterModule(object):
    '''Provide additional network-address--related Jinja2 filters for Ansible'''
    
    @staticmethod
    def ipv4_to_cidr(address, netmask):
        a = IPAddress(address)
        m = IPAddress(netmask)
        assert m.is_netmask(), 'A valid netmask is required' 
        n = IPNetwork(a)
        n.prefixlen = m.netmask_bits() 
        return str(n.cidr)

    @staticmethod
    def ipv4_inside_cidr(address, network):
        a = IPAddress(address)
        n = IPNetwork(network)
        return (a in n)

    def filters(self):
        return {
           'ipv4_to_cidr': self.ipv4_to_cidr,
           'ipv4_inside_cidr': self.ipv4_inside_cidr,
        }
