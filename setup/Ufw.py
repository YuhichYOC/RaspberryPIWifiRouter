import subprocess

from . import FileEntity


class Ufw:

    def __init__(self):
        self.f_is_2_way = False
        self.f_allow_ssh = False
        self.f_wan_interface = ''
        self.f_lan_2_way_eth_ip_address_start_with_mask = ''
        self.f_lan_2_way_wifi_ip_address_start_with_mask = ''

    @property
    def is_2_way(self) -> bool:
        return self.f_is_2_way

    @property
    def allow_ssh(self) -> bool:
        return self.f_allow_ssh

    @property
    def wan_interface(self) -> str:
        return self.f_wan_interface

    @property
    def lan_2_way_eth_ip_address_start_with_mask(self) -> str:
        return self.f_lan_2_way_eth_ip_address_start_with_mask

    @property
    def lan_2_way_wifi_ip_address_start_with_mask(self) -> str:
        return self.f_lan_2_way_wifi_ip_address_start_with_mask

    @is_2_way.setter
    def is_2_way(self, arg: bool):
        self.f_is_2_way = arg

    @allow_ssh.setter
    def allow_ssh(self, arg: bool):
        self.f_allow_ssh = arg

    @wan_interface.setter
    def wan_interface(self, arg: str):
        self.f_wan_interface = arg

    @lan_2_way_eth_ip_address_start_with_mask.setter
    def lan_2_way_eth_ip_address_start_with_mask(self, arg: str):
        self.f_lan_2_way_eth_ip_address_start_with_mask = arg

    @lan_2_way_wifi_ip_address_start_with_mask.setter
    def lan_2_way_wifi_ip_address_start_with_mask(self, arg: str):
        self.f_lan_2_way_wifi_ip_address_start_with_mask = arg

    @staticmethod
    def install_ufw() -> None:
        subprocess.call(['apt', 'install', '-y', 'ufw'])
        return None

    @staticmethod
    def edit_etc_default_ufw() -> None:
        target = FileEntity.FileEntity()
        target.path = '/etc/default/ufw'
        target.content_replace_regexp('templates/etc/default/ufw')
        return None

    @staticmethod
    def edit_etc_ufw_sysctl_conf() -> None:
        target = FileEntity.FileEntity()
        target.path = '/etc/ufw/sysctl.conf'
        target.content_replace_regexp('templates/etc/ufw/sysctl.conf')
        return None

    def append_etc_ufw_before_rules(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/ufw/before.rules'
        source.read()
        source.content_replace('WAN_INTERFACE_NAME', self.wan_interface)
        target = FileEntity.FileEntity()
        target.path = '/etc/ufw/before.rules'
        target.append(source.content)
        return None

    def append_etc_ufw_before_rules_2_way(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/ufw/before.2way.rules'
        source.read()
        source.content_replace('LAN_2_WAY_ETH_IP_ADDRESS_START_WITH_MASK',
                               self.lan_2_way_eth_ip_address_start_with_mask)
        source.content_replace('LAN_2_WAY_WIFI_IP_ADDRESS_START_WITH_MASK',
                               self.lan_2_way_wifi_ip_address_start_with_mask)
        source.content_replace('WAN_INTERFACE_NAME', self.wan_interface)
        target = FileEntity.FileEntity()
        target.path = '/etc/ufw/before.rules'
        target.append(source.content)
        return None

    def run(self) -> None:
        self.install_ufw()
        self.edit_etc_default_ufw()
        self.edit_etc_ufw_sysctl_conf()
        if self.is_2_way:
            self.append_etc_ufw_before_rules_2_way()
        else:
            self.append_etc_ufw_before_rules()
        if self.allow_ssh:
            subprocess.call(['ufw', 'allow', 'ssh'])
        subprocess.call(['ufw', 'allow', '53'])
        subprocess.call(['ufw', 'allow', '67'])
        subprocess.call(['ufw', 'allow', '68'])
        subprocess.call(['ufw', 'allow', 'http'])
        subprocess.call(['ufw', 'allow', 'https'])
        subprocess.call(['ufw', 'enable'])
        return None
