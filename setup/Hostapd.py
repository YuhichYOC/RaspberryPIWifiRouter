import os
import subprocess

from . import FileEntity


class Hostapd:

    def __init__(self):
        self.f_is_lan_to_wifi_bridge_ubuntu = False
        self.f_lan_interface = ''
        self.f_ess_id = ''
        self.f_passphrase = ''

    @property
    def is_lan_to_wifi_bridge_ubuntu(self) -> bool:
        return self.f_is_lan_to_wifi_bridge_ubuntu

    @property
    def lan_interface(self) -> str:
        return self.f_lan_interface

    @property
    def ess_id(self) -> str:
        return self.f_ess_id

    @property
    def passphrase(self) -> str:
        return self.f_passphrase

    @is_lan_to_wifi_bridge_ubuntu.setter
    def is_lan_to_wifi_bridge_ubuntu(self, arg: bool):
        self.f_is_lan_to_wifi_bridge_ubuntu = arg

    @lan_interface.setter
    def lan_interface(self, arg: str):
        self.f_lan_interface = arg

    @ess_id.setter
    def ess_id(self, arg: str):
        self.f_ess_id = arg

    @passphrase.setter
    def passphrase(self, arg: str):
        self.f_passphrase = arg

    @staticmethod
    def install_hostapd() -> None:
        subprocess.call(['apt', 'install', '-y', 'hostapd'])
        return None

    @staticmethod
    def create_directory() -> None:
        if os.path.isdir('/etc/hostapd/'):
            return None
        os.mkdir('/etc/hostapd/')
        return None

    @staticmethod
    def write_default_hostapd() -> None:
        target = FileEntity.FileEntity()
        target.path = '/etc/default/hostapd'
        target.content_replace_regexp('templates/etc/default/hostapd')
        return None

    def write_hostapd_conf(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/hostapd/hostapd.conf'
        source.read()
        source.content_replace('LAN_INTERFACE_NAME', self.lan_interface)
        source.content_replace('ESS_ID', self.ess_id)
        source.content_replace('PASSPHRASE', self.passphrase)
        target = FileEntity.FileEntity()
        target.path = '/etc/hostapd/hostapd.conf'
        target.rewrite(source.content)
        return None

    def write_hostapd_conf_with_bridge(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/hostapd/hostapd_with_bridge.conf'
        source.read()
        source.content_replace('LAN_INTERFACE_NAME', self.lan_interface)
        source.content_replace('ESS_ID', self.ess_id)
        source.content_replace('PASSPHRASE', self.passphrase)
        target = FileEntity.FileEntity()
        target.path = '/etc/hostapd/hostapd.conf'
        target.rewrite(source.content)
        return None

    def run(self) -> None:
        self.install_hostapd()
        self.create_directory()
        self.write_default_hostapd()
        if self.is_lan_to_wifi_bridge_ubuntu:
            self.write_hostapd_conf_with_bridge()
        else:
            self.write_hostapd_conf()
        return None
