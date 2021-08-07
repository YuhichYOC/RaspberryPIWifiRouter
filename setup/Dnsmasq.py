import os
import subprocess

from . import FileEntity


class Dnsmasq:

    def __init__(self):
        self.f_domain_name = ''
        self.f_lan_interface_name = ''
        self.f_range_from = ''
        self.f_range_to = ''
        self.f_router_ip = ''
        self.f_is_2_way = False
        self.f_lan_2_way_eth_interface_name = ''
        self.f_lan_2_way_eth_ip_address_without_mask = ''
        self.f_lan_2_way_wifi_interface_name = ''
        self.f_lan_2_way_wifi_ip_address_without_mask = ''
        self.f_dhcp_2_way_eth_range_from = ''
        self.f_dhcp_2_way_eth_range_to = ''
        self.f_dhcp_2_way_wifi_range_from = ''
        self.f_dhcp_2_way_wifi_range_to = ''

    @property
    def domain_name(self) -> str:
        return self.f_domain_name

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

    @property
    def is_2_way(self) -> bool:
        return self.f_is_2_way

    @property
    def lan_2_way_eth_interface_name(self) -> str:
        return self.f_lan_2_way_eth_interface_name

    @property
    def lan_2_way_eth_ip_address_without_mask(self) -> str:
        return self.f_lan_2_way_eth_ip_address_without_mask

    @property
    def lan_2_way_wifi_interface_name(self) -> str:
        return self.f_lan_2_way_wifi_interface_name

    @property
    def lan_2_way_wifi_ip_address_without_mask(self) -> str:
        return self.f_lan_2_way_wifi_ip_address_without_mask

    @property
    def dhcp_2_way_eth_range_from(self) -> str:
        return self.f_dhcp_2_way_eth_range_from

    @property
    def dhcp_2_way_eth_range_to(self) -> str:
        return self.f_dhcp_2_way_eth_range_to

    @property
    def dhcp_2_way_wifi_range_from(self) -> str:
        return self.f_dhcp_2_way_wifi_range_from

    @property
    def dhcp_2_way_wifi_range_to(self) -> str:
        return self.f_dhcp_2_way_wifi_range_to

    @domain_name.setter
    def domain_name(self, arg: str):
        self.f_domain_name = arg

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

    @is_2_way.setter
    def is_2_way(self, arg: bool):
        self.f_is_2_way = arg

    @lan_2_way_eth_interface_name.setter
    def lan_2_way_eth_interface_name(self, arg: str):
        self.f_lan_2_way_eth_interface_name = arg

    @lan_2_way_eth_ip_address_without_mask.setter
    def lan_2_way_eth_ip_address_without_mask(self, arg: str):
        self.f_lan_2_way_eth_ip_address_without_mask = arg

    @lan_2_way_wifi_interface_name.setter
    def lan_2_way_wifi_interface_name(self, arg: str):
        self.f_lan_2_way_wifi_interface_name = arg

    @lan_2_way_wifi_ip_address_without_mask.setter
    def lan_2_way_wifi_ip_address_without_mask(self, arg: str):
        self.f_lan_2_way_wifi_ip_address_without_mask = arg

    @dhcp_2_way_eth_range_from.setter
    def dhcp_2_way_eth_range_from(self, arg: str):
        self.f_dhcp_2_way_eth_range_from = arg

    @dhcp_2_way_eth_range_to.setter
    def dhcp_2_way_eth_range_to(self, arg: str):
        self.f_dhcp_2_way_eth_range_to = arg

    @dhcp_2_way_wifi_range_from.setter
    def dhcp_2_way_wifi_range_from(self, arg: str):
        self.f_dhcp_2_way_wifi_range_from = arg

    @dhcp_2_way_wifi_range_to.setter
    def dhcp_2_way_wifi_range_to(self, arg: str):
        self.f_dhcp_2_way_wifi_range_to = arg

    @staticmethod
    def install_dnsmasq() -> None:
        subprocess.call(['apt', 'install', '-y', 'dnsmasq'])
        return None

    @staticmethod
    def rename_conf_if_exists() -> None:
        if os.path.isfile('/etc/dnsmasq.conf'):
            subprocess.call(['mv', '/etc/dnsmasq.conf', '/etc/dnsmasq.conf.org'])
        return None

    def write_etc_dnsmasq_conf(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/dnsmasq.conf'
        source.read()
        source.content_replace('DOMAIN_NAME', self.domain_name)
        source.content_replace('LAN_INTERFACE_NAME', self.lan_interface_name)
        source.content_replace('DHCP_RANGE_FROM', self.range_from)
        source.content_replace('DHCP_RANGE_TO', self.range_to)
        source.content_replace('ROUTER_IP_ADDRESS', self.router_ip)
        target = FileEntity.FileEntity()
        target.path = '/etc/dnsmasq.conf'
        target.rewrite(source.content)
        return None

    def write_2_way_etc_dnsmasq_conf(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/dnsmasq.2way.conf'
        source.read()
        source.content_replace('DOMAIN_NAME', self.domain_name)
        source.content_replace('LAN_2_WAY_ETH_INTERFACE_NAME', self.lan_2_way_eth_interface_name)
        source.content_replace('LAN_2_WAY_ETH_IP_ADDRESS_WITHOUT_MASK', self.lan_2_way_eth_ip_address_without_mask)
        source.content_replace('LAN_2_WAY_WIFI_INTERFACE_NAME', self.lan_2_way_wifi_interface_name)
        source.content_replace('LAN_2_WAY_WIFI_IP_ADDRESS_WITHOUT_MASK', self.lan_2_way_wifi_ip_address_without_mask)
        source.content_replace('DHCP_2_WAY_ETH_RANGE_FROM', self.dhcp_2_way_eth_range_from)
        source.content_replace('DHCP_2_WAY_ETH_RANGE_TO', self.dhcp_2_way_eth_range_to)
        source.content_replace('DHCP_2_WAY_WIFI_RANGE_FROM', self.dhcp_2_way_wifi_range_from)
        source.content_replace('DHCP_2_WAY_WIFI_RANGE_TO', self.dhcp_2_way_wifi_range_to)
        source.content_replace('ROUTER_IP_ADDRESS', self.router_ip)
        target = FileEntity.FileEntity()
        target.path = '/etc/dnsmasq.conf'
        target.rewrite(source.content)
        return None

    @staticmethod
    def write_etc_resolv_dnsmasq_conf() -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/resolv.dnsmasq.conf'
        source.read()
        target = FileEntity.FileEntity()
        target.path = '/etc/resolv.dnsmasq.conf'
        target.rewrite(source.content)
        return None

    @staticmethod
    def write_etc_logrotate_d_dnsmasq() -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/logrotate.d/dnsmasq'
        source.read()
        target = FileEntity.FileEntity()
        target.path = '/etc/logrotate.d/dnsmasq'
        target.rewrite(source.content)
        return None

    def write(self) -> None:
        if self.is_2_way:
            self.write_2_way_etc_dnsmasq_conf()
        else:
            self.write_etc_dnsmasq_conf()
        self.write_etc_resolv_dnsmasq_conf()
        self.write_etc_logrotate_d_dnsmasq()
        return None

    def run(self) -> None:
        self.install_dnsmasq()
        self.rename_conf_if_exists()
        self.write()
        return None
