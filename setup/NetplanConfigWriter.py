from . import FileEntity


class NetplanConfigWriter:

    def __init__(self):
        self.f_is_wifi_router = True
        self.f_wan_interface_name = ''
        self.f_wan_ip_address = ''
        self.f_lan_interface_name = ''
        self.f_lan_ip_address = ''
        self.f_gateway4 = ''
        self.f_ess_id = ''
        self.f_passphrase = ''

    @property
    def is_wifi_router(self) -> bool:
        return self.f_is_wifi_router

    @property
    def wan_interface_name(self) -> str:
        return self.f_wan_interface_name

    @property
    def wan_ip_address(self) -> str:
        return self.f_wan_ip_address

    @property
    def lan_interface_name(self) -> str:
        return self.f_lan_interface_name

    @property
    def lan_ip_address(self) -> str:
        return self.f_lan_ip_address

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

    @wan_interface_name.setter
    def wan_interface_name(self, arg: str):
        self.f_wan_interface_name = arg

    @wan_ip_address.setter
    def wan_ip_address(self, arg: str):
        self.f_wan_ip_address = arg

    @lan_interface_name.setter
    def lan_interface_name(self, arg: str):
        self.f_lan_interface_name = arg

    @lan_ip_address.setter
    def lan_ip_address(self, arg: str):
        self.f_lan_ip_address = arg

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
            '  renderer: NetworkManager',
            '  ethernets:',
            '    ' + self.wan_interface_name + ':',
            '      dhcp4: false',
            '      addresses: [',
            '        ' + self.wan_ip_address + '/24',
            '      ]',
            '      gateway4: ' + self.gateway4,
            '      nameservers: ',
            '        addresses: [',
            '          8.8.8.8,',
            '          8.8.4.4,',
            '        ]',
        ]
        self.write_to_file(content)
        return None

    def write_lan_ap(self) -> None:
        content = [
            'network:',
            '  version: 2',
            '  renderer: NetworkManager',
            '  ethernets:',
            '    ' + self.lan_interface_name + ':',
            '      dhcp4: false',
            '      addresses: [',
            '        ' + self.lan_ip_address + '/24',
            '      ]',
            '      gateway4: ' + self.gateway4,
            '  wifis:',
            '    ' + self.wan_interface_name + ':',
            '      dhcp4: false',
            '      addresses: [',
            '        ' + self.wan_ip_address + '/24',
            '      ]',
            '      access-points:',
            '        ' + self.ess_id + ':',
            '          password: ' + self.passphrase,
            '      gateway4: ' + self.gateway4,
            '      nameservers: ',
            '        addresses: [',
            '          8.8.8.8,',
            '          8.8.4.4,',
            '        ]',
        ]
        self.write_to_file(content)
        return None

    def run(self) -> None:
        if self.is_wifi_router:
            self.write_wifi_router()
        else:
            self.write_lan_ap()
        return None
