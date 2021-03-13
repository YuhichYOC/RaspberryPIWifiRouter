import os
import re

from . import FileEntity


class NetworkManagerConfWriter:

    @staticmethod
    def if_exists() -> None:
        l_p_main = re.compile('^[main]')
        l_p_dns = re.compile('^dns=')
        fe = FileEntity.FileEntity()
        fe.path = '/etc/NetworkManager/NetworkManager.conf'
        fe.read()
        new_content = []
        for line in fe.content:
            l_m_main = l_p_main.match(line)
            l_m_dns = l_p_dns.match(line)
            if l_m_main is not None:
                new_content.append(line)
                new_content.append('dns=none')
            elif l_m_dns is not None:
                new_content.append('')
            else:
                new_content.append(line)
        fe.content = new_content
        fe.write()
        return None

    @staticmethod
    def if_not_exists() -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/NetworkManager/NetworkManager.conf'
        content = [
            '[main]',
            'dns=none',
        ]
        fe.content = content
        fe.write()
        return None

    def run(self) -> None:
        if os.path.isfile('/etc/NetworkManager/NetworkManager.conf'):
            self.if_exists()
        else:
            self.if_not_exists()
        return None
