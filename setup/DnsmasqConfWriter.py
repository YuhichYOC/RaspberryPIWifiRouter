import os

from . import FileEntity


class DnsmasqConfWriter:

    def __init__(self):
        self.f_interface = ''
        self.f_self_ip_address = ''
        self.f_range_from = ''
        self.f_range_to = ''

    @property
    def interface(self) -> str:
        return self.f_interface

    @property
    def self_ip_address(self) -> str:
        return self.f_self_ip_address

    @property
    def range_from(self) -> str:
        return self.f_range_from

    @property
    def range_to(self) -> str:
        return self.f_range_to

    @interface.setter
    def interface(self, arg: str):
        self.f_interface = arg

    @self_ip_address.setter
    def self_ip_address(self, arg: str):
        self.f_self_ip_address = arg

    @range_from.setter
    def range_from(self, arg: str):
        self.f_range_from = arg

    @range_to.setter
    def range_to(self, arg: str):
        self.f_range_to = arg

    @staticmethod
    def delete_conf_if_exists() -> None:
        if os.path.isfile('/etc/dnsmasq.conf'):
            os.remove('/etc/dnsmasq.conf')
        return None

    def write(self) -> None:
        content = [
            'interface=' + self.interface,
            'dhcp-range=' + self.range_from + ',' + self.range_to + ',255.255.255.0,24h',
            'listen-address=127.0.0.1,' + self.self_ip_address,
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
