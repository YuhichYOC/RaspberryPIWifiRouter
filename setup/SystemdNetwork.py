from . import FileEntity


class SystemdNetwork:

    def __init__(self):
        self.f_lan_interface = ''
        self.f_lan_ip_address = ''

    @property
    def lan_interface(self) -> str:
        return self.f_lan_interface

    @property
    def lan_ip_address(self) -> str:
        return self.f_lan_ip_address

    @lan_interface.setter
    def lan_interface(self, arg: str):
        self.f_lan_interface = arg

    @lan_ip_address.setter
    def lan_ip_address(self, arg: str):
        self.f_lan_ip_address = arg

    def write(self) -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/systemd/network/' + self.lan_interface + '.network'
        fe.rewrite([
            '[Match]',
            'Name=' + self.lan_interface,
            '',
            '[Network]',
            'Address=' + self.lan_ip_address + '/24',
        ])
        return None

    def run(self) -> None:
        self.write()
        return None
