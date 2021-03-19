from . import FileEntity


class NetPlan:

    def __init__(self):
        self.f_is_test_ap = False
        self.f_is_wifi_router = True
        self.f_wan_interface_name = ''
        self.f_lan_interface_name = ''
        self.f_ess_id = ''
        self.f_passphrase = ''

    @property
    def is_test_ap(self) -> bool:
        return self.f_is_test_ap

    @property
    def is_wifi_router(self) -> bool:
        return self.f_is_wifi_router

    @property
    def wan_interface_name(self) -> str:
        return self.f_wan_interface_name

    @property
    def lan_interface_name(self) -> str:
        return self.f_lan_interface_name

    @property
    def ess_id(self) -> str:
        return self.f_ess_id

    @property
    def passphrase(self) -> str:
        return self.f_passphrase

    @is_test_ap.setter
    def is_test_ap(self, arg: bool):
        self.f_is_test_ap = arg

    @is_wifi_router.setter
    def is_wifi_router(self, arg: bool):
        self.f_is_wifi_router = arg

    @wan_interface_name.setter
    def wan_interface_name(self, arg: str):
        self.f_wan_interface_name = arg

    @lan_interface_name.setter
    def lan_interface_name(self, arg: str):
        self.f_lan_interface_name = arg

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

    def write_test_router(self) -> None:
        content = [
            'network:',
            '  version: 2',
            '  renderer: NetworkManager',
            '  ethernets:',
            '    ' + self.wan_interface_name + ':',
            '      dhcp4: trie',
            '    ' + self.lan_interface_name + ':',
            '      dhcp4: true',
        ]
        self.write_to_file(content)
        return None

    def write_wifi_router(self) -> None:
        content = [
            'network:',
            '  version: 2',
            '  renderer: NetworkManager',
            '  ethernets:',
            '    ' + self.wan_interface_name + ':',
            '      dhcp4: true',
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
            '      dhcp4: true',
            '  wifis:',
            '    ' + self.wan_interface_name + ':',
            '      dhcp4: true',
            '      access-points:',
            '        ' + self.ess_id + ':',
            '          password: ' + self.passphrase,
        ]
        self.write_to_file(content)
        return None

    def run(self) -> None:
        if self.is_test_ap:
            self.write_test_router()
        elif self.is_wifi_router:
            self.write_wifi_router()
        else:
            self.write_lan_ap()
        return None
