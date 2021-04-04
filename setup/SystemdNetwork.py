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
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/systemd/network/lan_interface.network'
        source.read()
        source.content_replace('LAN_INTERFACE', self.lan_interface)
        source.content_replace('LAN_IP_ADDRESS', self.lan_ip_address)
        target = FileEntity.FileEntity()
        target.path = '/etc/systemd/network/' + self.lan_interface + '.network'
        target.rewrite(source.content)
        return None

    def run(self) -> None:
        self.write()
        return None
