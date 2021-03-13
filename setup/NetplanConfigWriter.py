import glob
import subprocess

from . import FileEntity


class NetplanConfigWriter:

    def __init__(self):
        self.f_is_wifi_router = True
        self.f_eth_interface_name = ''
        self.f_eth_ip_address = ''
        self.f_wlan_interface_name = ''
        self.f_wlan_ip_address = ''
        self.f_gateway4 = ''
        self.f_ess_id = ''
        self.f_passphrase = ''

    @property
    def is_wifi_router(self) -> bool:
        return self.f_is_wifi_router

    @property
    def eth_interface_name(self) -> str:
        return self.f_eth_interface_name

    @property
    def eth_ip_address(self) -> str:
        return self.f_eth_ip_address

    @property
    def wlan_interface_name(self) -> str:
        return self.f_wlan_interface_name

    @property
    def wlan_ip_address(self) -> str:
        return self.f_wlan_ip_address

    @property
    def gateway4(self) -> str:
        return self.f_gateway4

    @property
    def ess_id(self) -> str:
        return self.f_ess_id

    @property
    def passphrase(self) -> str:
        return self.f_passphrase

    @is_wifi_router.setter
    def is_wifi_router(self, arg: bool):
        self.f_is_wifi_router = arg

    @eth_interface_name.setter
    def eth_interface_name(self, arg: str):
        self.f_eth_interface_name = arg

    @eth_ip_address.setter
    def eth_ip_address(self, arg: str):
        self.f_eth_ip_address = arg

    @wlan_interface_name.setter
    def wlan_interface_name(self, arg: str):
        self.f_wlan_interface_name = arg

    @wlan_ip_address.setter
    def wlan_ip_address(self, arg: str):
        self.f_wlan_ip_address = arg

    @gateway4.setter
    def gateway4(self, arg: str):
        self.f_gateway4 = arg

    @ess_id.setter
    def ess_id(self, arg: str):
        self.f_ess_id = arg

    @passphrase.setter
    def passphrase(self, arg: str):
        self.f_passphrase = arg

    @staticmethod
    def remove_01() -> None:
        l_files = glob.glob('/etc/netplan/01*.yaml')
        if 0 < len(l_files):
            for file_name in l_files:
                subprocess.call(['rm', file_name])
        return None

    @staticmethod
    def remove_10() -> None:
        l_files = glob.glob('/etc/netplan/10*.yaml')
        if 0 < len(l_files):
            for file_name in l_files:
                subprocess.call(['rm', file_name])
        return None

    @staticmethod
    def write_to_file(a_content: list) -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/netplan/99-config.yaml'
        fe.content = a_content
        fe.write()
        return None

    def write_wifi_router(self) -> None:
        content = [
            'network:',
            '  version: 2',
            '  renderer: networkd',
            '  ethernets:',
            '    ' + self.eth_interface_name + ':',
            '      dhcp4: false',
            '      addresses: [',
            '        ' + self.eth_ip_address + '/24',
            '      ]',
            '      gateway4: ' + self.gateway4,
        ]
        self.write_to_file(content)
        return None

    def write_lan_ap(self) -> None:
        content = [
            'network:',
            '  version: 2',
            '  renderer: networkd',
            '  ethernets:',
            '    ' + self.eth_interface_name + ':',
            '      dhcp4: false',
            '      addresses: [',
            '        ' + self.eth_ip_address + '/24',
            '      ]',
            '      gateway4: ' + self.gateway4,
            '  wifis:',
            '    ' + self.wlan_interface_name + ':',
            '      dhcp4: false',
            '      addresses: [',
            '        ' + self.wlan_ip_address + '/24',
            '      ]',
            '      access-points:',
            '        ' + self.ess_id + ':',
            '          password: ' + self.passphrase,
            '      gateway4: ' + self.gateway4,
        ]
        self.write_to_file(content)
        return None

    def run(self) -> None:
        self.remove_01()
        self.remove_10()
        if self.is_wifi_router:
            self.write_wifi_router()
        else:
            self.write_lan_ap()
        return None
