from . import FileEntity


class Dhcpcd:

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
        source.path = 'templates/etc/dhcpcd.conf'
        source.read()
        source.content_replace('LAN_INTERFACE_NAME', self.lan_interface)
        source.content_replace('LAN_IP_ADDRESS', self.lan_ip_address)
        target = FileEntity.FileEntity()
        target.path = '/etc/dhcpcd.conf'
        target.append(source.content)
        return None

    def run(self) -> None:
        self.write()
        return None
