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
        target = FileEntity.FileEntity()
        target.path = '/etc/default/ufw'
        target.content_replace_regexp('templates/etc/default/ufw')
        return None

    @staticmethod
    def edit_etc_ufw_sysctl_conf() -> None:
        target = FileEntity.FileEntity()
        target.path = '/etc/ufw/sysctl.conf'
        target.content_replace_regexp('templates/etc/ufw/sysctl.conf')
        return None

    def append_etc_ufw_before_rules(self) -> None:
        source = FileEntity.FileEntity()
        source.path = 'templates/etc/ufw/before.rules'
        source.read()
        source.content_replace('WAN_INTERFACE_NAME', self.wan_interface)
        target = FileEntity.FileEntity()
        target.path = '/etc/ufw/before.rules'
        target.append(source.content)
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
