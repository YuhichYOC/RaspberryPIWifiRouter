import os
import subprocess

from . import FileEntity


class Hostapd:

    def __init__(self):
        self.f_lan_interface = ''
        self.f_ess_id = ''
        self.f_passphrase = ''

    @property
    def lan_interface(self) -> str:
        return self.f_lan_interface

    @property
    def ess_id(self) -> str:
        return self.f_ess_id

    @property
    def passphrase(self) -> str:
        return self.f_passphrase

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
        fe = FileEntity.FileEntity()
        fe.path = '/etc/default/hostapd'
        fe.replace_regexp('^#?DAEMON_CONF=', 'DAEMON_CONF="/etc/hostapd/hostapd.conf"')
        return None

    def write_hostapd_conf(self) -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/hostapd/hostapd.conf'
        fe.rewrite([
            'interface=' + self.lan_interface,
            'driver=nl80211',
            'hw_mode=b',
            'channel=1',
            'macaddr_acl=0',
            'auth_algs=1',
            'ignore_broadcast_ssid=0',
            'ieee80211ac=0',
            'wmm_enabled=1',
            'ieee80211d=1',
            'ieee80211h=1',
            'country_code=JP',
            'local_pwr_constraint=3',
            'spectrum_mgmt_required=1',
            'wpa=2',
            'wpa_key_mgmt=WPA-PSK',
            'wpa_pairwise=CCMP',
            'rsn_pairwise=CCMP',
            'ssid=' + self.ess_id,
            'wpa_passphrase=' + self.passphrase,
        ])
        return None

    def run(self) -> None:
        self.install_hostapd()
        self.create_directory()
        self.write_default_hostapd()
        self.write_hostapd_conf()
        return None
