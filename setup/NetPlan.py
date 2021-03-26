import subprocess

from . import FileEntity


class NetPlan:

    def __init__(self):
        self.f_is_wifi_router_ubuntu = True
        self.f_is_wifi_to_lan_router = False
        self.f_wan_interface_name = ''
        self.f_lan_interface_name = ''
        self.f_lan_ip_address = ''
        self.f_ess_id = ''
        self.f_passphrase = ''

    @property
    def is_wifi_router_ubuntu(self) -> bool:
        return self.f_is_wifi_router_ubuntu

    @property
    def is_wifi_to_lan_router(self) -> bool:
        return self.f_is_wifi_to_lan_router

    @property
    def wan_interface_name(self) -> str:
        return self.f_wan_interface_name

    @property
    def lan_interface_name(self) -> str:
        return self.f_lan_interface_name

    @property
    def lan_ip_address(self) -> str:
        return self.f_lan_ip_address

    @property
    def ess_id(self) -> str:
        return self.f_ess_id

    @property
    def passphrase(self) -> str:
        return self.f_passphrase

    @is_wifi_router_ubuntu.setter
    def is_wifi_router_ubuntu(self, arg: bool):
        self.f_is_wifi_router_ubuntu = arg

    @is_wifi_to_lan_router.setter
    def is_wifi_to_lan_router(self, arg: bool):
        self.f_is_wifi_to_lan_router = arg

    @wan_interface_name.setter
    def wan_interface_name(self, arg: str):
        self.f_wan_interface_name = arg

    @lan_interface_name.setter
    def lan_interface_name(self, arg: str):
        self.f_lan_interface_name = arg

    @lan_ip_address.setter
    def lan_ip_address(self, arg: str):
        self.f_lan_ip_address = arg

    @ess_id.setter
    def ess_id(self, arg: str):
        self.f_ess_id = arg

    @passphrase.setter
    def passphrase(self, arg: str):
        self.f_passphrase = arg

    @staticmethod
    def install_network_manager() -> None:
        subprocess.call(['apt', 'install', '-y', 'network-manager'])
        return None

    def write_wifi_router_ubuntu(self) -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/netplan/99-config.yaml'
        fe.rewrite([
            'network:',
            '  version: 2',
            '  renderer: networkd',
            '  ethernets:',
            '    ' + self.wan_interface_name + ':',
            '      dhcp4: true',
        ])
        return None

    def write_wifi_to_lan_ap(self) -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/netplan/99-config.yaml'
        fe.rewrite([
            'network:',
            '  version: 2',
            '  renderer: NetworkManager',
            '  ethernets:',
            '    ' + self.lan_interface_name + ':',
            '      dhcp4: true',
            '  wifis:',
            '    ' + self.wan_interface_name + ':',
            '      dhcp4: true',
            '      access-points:',
            '        ' + self.ess_id + ':',
            '          password: ' + self.passphrase,
        ])
        return None

    def write_lan_to_lan_ap(self) -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/netplan/99-config.yaml'
        fe.rewrite([
            'network:',
            '  version: 2',
            '  ethernets:',
            '    ' + self.wan_interface_name + ':',
            '      dhcp4: true',
            '    ' + self.lan_interface_name + ':',
            '      addresses: [',
            '        ' + self.lan_ip_address + '/24',
            '      ]',
            '      dhcp4: false',
        ])
        return None

    def run(self) -> None:
        if self.is_wifi_router_ubuntu:
            self.write_wifi_router_ubuntu()
        elif self.is_wifi_to_lan_router:
            self.install_network_manager()
            self.write_wifi_to_lan_ap()
        else:
            self.write_lan_to_lan_ap()
        return None
