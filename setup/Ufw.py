import re
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

    def run(self) -> None:
        if self.allow_ssh:
            subprocess.call(['ufw', 'allow', 'ssh'])
        fe = FileEntity.FileEntity()
        new_content = []
        fe.path = '/etc/default/ufw'
        fe.read()
        l_p = re.compile('^#?DEFAULT_FORWARD_POLICY=')
        for line in fe.content:
            l_m = l_p.match(line)
            if l_m is not None:
                new_content.append('DEFAULT_FORWARD_POLICY="ACCEPT"')
            else:
                new_content.append(line)
        fe.content = new_content
        fe.write()
        new_content.clear()
        fe.path = '/etc/ufw/sysctl.conf'
        fe.read()
        l_p = re.compile('^#?net/ipv4/ip_forward=')
        for line in fe.content:
            l_m = l_p.match(line)
            if l_m is not None:
                new_content.append('net/ipv4/ip_forward=1')
            else:
                new_content.append(line)
        fe.content = new_content
        fe.write()
        fe.path = '/etc/ufw/before.rules'
        fe.read()
        fe.content.append('*nat')
        fe.content.append(':POSTROUTING ACCEPT [0:0]')
        fe.content.append('-A POSTROUTING -o ' + self.wan_interface + ' -j MASQUERADE')
        fe.content.append('COMMIT')
        fe.write()
        subprocess.call(['ufw', 'allow', '53'])
        subprocess.call(['ufw', 'enable'])
        return None
