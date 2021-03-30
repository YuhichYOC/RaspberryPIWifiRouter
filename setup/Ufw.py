import subprocess

from . import FileEntity


class Ufw:

    def __init__(self):
        self.f_allow_ssh = False
        self.f_wan_interface = ''

    @property
    def allow_ssh(self) -> bool:
        return self.f_allow_ssh

    @property
    def wan_interface(self) -> str:
        return self.f_wan_interface

    @allow_ssh.setter
    def allow_ssh(self, arg: bool):
        self.f_allow_ssh = arg

    @wan_interface.setter
    def wan_interface(self, arg: str):
        self.f_wan_interface = arg

    @staticmethod
    def install_ufw() -> None:
        subprocess.call(['apt', 'install', '-y', 'ufw'])
        return None

    @staticmethod
    def edit_etc_default_ufw() -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/default/ufw'
        fe.replace_regexp('^#?DEFAULT_FORWARD_POLICY=', 'DEFAULT_FORWARD_POLICY="ACCEPT"')
        return None

    @staticmethod
    def edit_etc_ufw_sysctl_conf() -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/ufw/sysctl.conf'
        fe.replace_regexp('^#?net/ipv4/ip_forward=', 'net/ipv4/ip_forward=1')
        return None

    def append_etc_ufw_before_rules(self) -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/ufw/before.rules'
        fe.append([
            '*nat',
            ':POSTROUTING ACCEPT [0:0]',
            '-A POSTROUTING -o ' + self.wan_interface + ' -j MASQUERADE',
            'COMMIT',
        ])
        return None

    def run(self) -> None:
        self.install_ufw()
        self.edit_etc_default_ufw()
        self.edit_etc_ufw_sysctl_conf()
        self.append_etc_ufw_before_rules()
        if self.allow_ssh:
            subprocess.call(['ufw', 'allow', 'ssh'])
        subprocess.call(['ufw', 'allow', '53'])
        subprocess.call(['ufw', 'allow', '67'])
        subprocess.call(['ufw', 'allow', '68'])
        subprocess.call(['ufw', 'allow', 'http'])
        subprocess.call(['ufw', 'allow', 'https'])
        subprocess.call(['ufw', 'enable'])
        return None
