import os

from . import FileEntity


class DnsmasqConfWriter:

    def __init__(self):
        self.f_domain_name = ''
        self.f_wan_interface_name = ''
        self.f_lan_interface_name = ''
        self.f_range_from = ''
        self.f_range_to = ''
        self.f_router_ip = ''

    @property
    def domain_name(self) -> str:
        return self.f_domain_name

    @property
    def wan_interface_name(self) -> str:
        return self.f_wan_interface_name

    @property
    def lan_interface_name(self) -> str:
        return self.f_lan_interface_name

    @property
    def range_from(self) -> str:
        return self.f_range_from

    @property
    def range_to(self) -> str:
        return self.f_range_to

    @property
    def router_ip(self) -> str:
        return self.f_router_ip

    @domain_name.setter
    def domain_name(self, arg: str):
        self.f_domain_name = arg

    @wan_interface_name.setter
    def wan_interface_name(self, arg: str):
        self.f_wan_interface_name = arg

    @lan_interface_name.setter
    def lan_interface_name(self, arg: str):
        self.f_lan_interface_name = arg

    @range_from.setter
    def range_from(self, arg: str):
        self.f_range_from = arg

    @range_to.setter
    def range_to(self, arg: str):
        self.f_range_to = arg

    @router_ip.setter
    def router_ip(self, arg: str):
        self.f_router_ip = arg

    @staticmethod
    def delete_conf_if_exists() -> None:
        if os.path.isfile('/etc/dnsmasq.conf'):
            os.remove('/etc/dnsmasq.conf')
        return None

    def write(self) -> None:
        content = [
            'domain-needed',
            'bogus-priv',
            'resolv-file=/etc/resolv.dnsmasq.conf',
            'local=/' + self.domain_name + '/',
            'interface=' + self.wan_interface_name,
            'interface=' + self.lan_interface_name,
            'expand-hosts',
            'domain=' + self.domain_name,
            'dhcp-range=' + self.range_from + ',' + self.range_to + ',24h',
            'dhcp-option=option:netmask,255.255.255.0',
            'dhcp-option=option:router,' + self.router_ip,
            'dhcp-option=option:dns-server,' + self.router_ip,
            'dhcp-leasefile=/var/lib/misc/dnsmasq.leases',
            'log-queries',
            'log-facility=/var/log/dnsmasq.log',
        ]
        fe = FileEntity.FileEntity()
        fe.path = '/etc/dnsmasq.conf'
        fe.content = content
        fe.write()
        return None

    def run(self) -> None:
        self.delete_conf_if_exists()
        self.write()
        return None
