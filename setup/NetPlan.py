import subprocess

from . import FileEntity


class NetPlan:

    def __init__(self):
        self.f_is_wifi_router_ubuntu = False
        self.f_is_wifi_to_lan_router_ubuntu = False
        self.f_is_lan_to_lan_router_ubuntu = False
        self.f_is_wifi_client_ubuntu = False
        self.f_is_2_way_router_ubuntu = False
        self.f_wan_interface_name = ''
        self.f_lan_interface_name = ''
        self.f_lan_ip_address = ''
        self.f_lan_2_way_interface_name = ''
        self.f_lan_2_way_ip_address_with_mask = ''
        self.f_ess_id = ''
        self.f_passphrase = ''

    @property
    def is_wifi_router_ubuntu(self) -> bool:
        return self.f_is_wifi_router_ubuntu

    @property
    def is_wifi_to_lan_router_ubuntu(self) -> bool:
        return self.f_is_wifi_to_lan_router_ubuntu

    @property
    def is_lan_to_lan_router_ubuntu(self) -> bool:
        return self.f_is_lan_to_lan_router_ubuntu

    @property
    def is_wifi_client_ubuntu(self) -> bool:
        return self.f_is_wifi_client_ubuntu

    @property
    def is_2_way_router_ubuntu(self) -> bool:
        return self.f_is_2_way_router_ubuntu

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
    def lan_2_way_interface_name(self) -> str:
        return self.f_lan_2_way_interface_name

    @property
    def lan_2_way_ip_address_with_mask(self) -> str:
        return self.f_lan_2_way_ip_address_with_mask

    @property
    def ess_id(self) -> str:
        return self.f_ess_id

    @property
    def passphrase(self) -> str:
        return self.f_passphrase

    @is_wifi_router_ubuntu.setter
    def is_wifi_router_ubuntu(self, arg: bool):
        self.f_is_wifi_router_ubuntu = arg

    @is_wifi_to_lan_router_ubuntu.setter
    def is_wifi_to_lan_router_ubuntu(self, arg: bool):
        self.f_is_wifi_to_lan_router_ubuntu = arg

    @is_lan_to_lan_router_ubuntu.setter
    def is_lan_to_lan_router_ubuntu(self, arg: bool):
        self.f_is_lan_to_lan_router_ubuntu = arg

    @is_wifi_client_ubuntu.setter
    def is_wifi_client_ubuntu(self, arg: bool):
        self.f_is_wifi_client_ubuntu = arg

    @is_2_way_router_ubuntu.setter
    def is_2_way_router_ubuntu(self, arg: bool):
        self.f_is_2_way_router_ubuntu = arg

    @wan_interface_name.setter
    def wan_interface_name(self, arg: str):
        self.f_wan_interface_name = arg

    @lan_interface_name.setter
    def lan_interface_name(self, arg: str):
        self.f_lan_interface_name = arg

    @lan_ip_address.setter
    def lan_ip_address(self, arg: str):
        self.f_lan_ip_address = arg

    @lan_2_way_interface_name.setter
    def lan_2_way_interface_name(self, arg: str):
        self.f_lan_2_way_interface_name = arg

    @lan_2_way_ip_address_with_mask.setter
    def lan_2_way_ip_address_with_mask(self, arg: str):
        self.f_lan_2_way_ip_address_with_mask = arg

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
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/netplan/99_wifi_router_ubuntu.yaml'
        source.read()
        source.content_replace('WAN_INTERFACE_NAME', self.wan_interface_name)
        target = FileEntity.FileEntity()
        target.path = '/etc/netplan/99-config.yaml'
        target.rewrite(source.content)
        return None

    def write_wifi_to_lan_router_ubuntu(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/netplan/99_wifi_to_lan_ap_ubuntu.yaml'
        source.read()
        source.content_replace('LAN_INTERFACE_NAME', self.lan_interface_name)
        source.content_replace('LAN_IP_ADDRESS', self.lan_ip_address)
        source.content_replace('WAN_INTERFACE_NAME', self.wan_interface_name)
        source.content_replace('ESS_ID', self.ess_id)
        source.content_replace('PASSPHRASE', self.passphrase)
        target = FileEntity.FileEntity()
        target.path = '/etc/netplan/99-config.yaml'
        target.rewrite(source.content)
        return None

    def write_lan_to_lan_router_ubuntu(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/netplan/99_lan_to_lan_ap_ubuntu.yaml'
        source.read()
        source.content_replace('WAN_INTERFACE_NAME', self.wan_interface_name)
        source.content_replace('LAN_INTERFACE_NAME', self.lan_interface_name)
        source.content_replace('LAN_IP_ADDRESS', self.lan_ip_address)
        target = FileEntity.FileEntity()
        target.path = '/etc/netplan/99-config.yaml'
        target.rewrite(source.content)
        return None

    def write_wifi_client_ubuntu(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/netplan/99_wifi_client_ubuntu.yaml'
        source.read()
        source.content_replace('LAN_INTERFACE_NAME', self.lan_interface_name)
        source.content_replace('WAN_INTERFACE_NAME', self.wan_interface_name)
        source.content_replace('ESS_ID', self.ess_id)
        source.content_replace('PASSPHRASE', self.passphrase)
        target = FileEntity.FileEntity()
        target.path = '/etc/netplan/99-config.yaml'
        target.rewrite(source.content)
        return None

    def write_2_way_router_ubuntu(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/netplan/99_2_way_router_ubuntu.yaml'
        source.read()
        source.content_replace('WAN_INTERFACE_NAME', self.wan_interface_name)
        source.content_replace('LAN_2_WAY_INTERFACE_NAME', self.lan_2_way_interface_name)
        source.content_replace('LAN_2_WAY_ETH_IP_ADDRESS_WITH_MASK', self.lan_2_way_ip_address_with_mask)
        target = FileEntity.FileEntity()
        target.path = '/etc/netplan/99-config.yaml'
        target.rewrite(source.content)
        return None

    def run(self) -> None:
        if self.is_wifi_router_ubuntu:
            self.write_wifi_router_ubuntu()
        elif self.is_wifi_to_lan_router_ubuntu:
            self.install_network_manager()
            self.write_wifi_to_lan_router_ubuntu()
        elif self.is_lan_to_lan_router_ubuntu:
            self.write_lan_to_lan_router_ubuntu()
        elif self.is_wifi_client_ubuntu:
            self.install_network_manager()
            self.write_wifi_client_ubuntu()
        elif self.is_2_way_router_ubuntu:
            self.write_2_way_router_ubuntu()
        return None
