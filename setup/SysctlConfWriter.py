import re
import subprocess

from . import FileEntity


class SysctlConfWriter:

    @staticmethod
    def uncomment_ip_forward() -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/sysctl.conf'
        fe.read()
        l_p = re.compile('^#net\\.ipv4\\.ip_forward=')
        new_content = []
        for line in fe.content:
            l_m = l_p.match(line)
            if l_m is not None:
                new_content.append('net.ipv4.ip_forward=1')
            else:
                new_content.append(line)
        fe.content = new_content
        fe.write()
        return None

    @staticmethod
    def call_sysctl_p() -> None:
        subprocess.call(['sysctl', '-p'])
        return None

    def run(self) -> None:
        self.uncomment_ip_forward()
        self.call_sysctl_p()
        return None
