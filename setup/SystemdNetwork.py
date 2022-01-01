from . import FileEntity


class SystemdNetwork:

    def __init__(self):
        self.f_is_2_way = False
        self.f_is_lan_to_wifi_bridge_ubuntu = False
        self.f_lan_interface = ''
        self.f_lan_ip_address = ''
        self.f_lan_ip_address_with_mask = ''

    @property
    def is_2_way(self) -> bool:
        return self.f_is_2_way

    @property
    def is_lan_to_wifi_bridge_ubuntu(self) -> bool:
        return self.f_is_lan_to_wifi_bridge_ubuntu

    @property
    def lan_interface(self) -> str:
        return self.f_lan_interface

    @property
    def lan_ip_address(self) -> str:
        return self.f_lan_ip_address

    @property
    def lan_ip_address_with_mask(self) -> str:
        return self.f_lan_ip_address_with_mask

    @is_2_way.setter
    def is_2_way(self, arg: bool):
        self.f_is_2_way = arg

    @is_lan_to_wifi_bridge_ubuntu.setter
    def is_lan_to_wifi_bridge_ubuntu(self, arg: bool):
        self.f_is_lan_to_wifi_bridge_ubuntu = arg

    @lan_interface.setter
    def lan_interface(self, arg: str):
        self.f_lan_interface = arg

    @lan_ip_address.setter
    def lan_ip_address(self, arg: str):
        self.f_lan_ip_address = arg

    @lan_ip_address_with_mask.setter
    def lan_ip_address_with_mask(self, arg: str):
        self.f_lan_ip_address_with_mask = arg

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

    def write_2_way(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/systemd/network/lan_interface.2way.network'
        source.read()
        source.content_replace('LAN_2_WAY_WIFI_INTERFACE_NAME', self.lan_interface)
        source.content_replace('LAN_2_WAY_WIFI_IP_ADDRESS_WITH_MASK', self.lan_ip_address_with_mask)
        target = FileEntity.FileEntity()
        target.path = '/etc/systemd/network/' + self.lan_interface + '.network'
        target.rewrite(source.content)
        return None

    def write_bridge_lan(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/systemd/network/bridge_lan_interface.network'
        source.read()
        source.content_replace('LAN_INTERFACE', self.lan_interface)
        target = FileEntity.FileEntity()
        target.path = '/etc/systemd/network/' + self.lan_interface + '.network'
        target.rewrite(source.content)
        return None

    def run(self) -> None:
        if self.is_2_way:
            self.write_2_way()
        elif self.is_lan_to_wifi_bridge_ubuntu:
            self.write_bridge_lan()
        else:
            self.write()
        return None
