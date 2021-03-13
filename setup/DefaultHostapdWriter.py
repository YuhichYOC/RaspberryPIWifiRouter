import re

from . import FileEntity


class DefaultHostapdWriter:

    @staticmethod
    def write() -> None:
        fe = FileEntity.FileEntity()
        fe.path = '/etc/default/hostapd'
        fe.read()
        l_p = re.compile('^#DAEMON_CONF=')
        new_content = []
        for line in fe.content:
            l_m = l_p.match(line)
            if l_m is not None:
                new_content.append('DAEMON_CONF="/etc/hostapd/hostapd.conf"')
            else:
                new_content.append(line)
        fe.content = new_content
        fe.write()
        return None

    def run(self) -> None:
        self.write()
        return None
