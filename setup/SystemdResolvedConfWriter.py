import re

from . import FileEntity


class SystemdResolvedConfWriter:

    @staticmethod
    def write() -> None:
        l_p = re.compile('^#DNSStubListener=')
        fe = FileEntity.FileEntity()
        fe.path = '/etc/systemd/resolved.conf'
        fe.read()
        new_content = []
        for line in fe.content:
            l_m = l_p.match(line)
            if l_m is not None:
                new_content.append('DNSStubListener=no')
            else:
                new_content.append(line)
        fe.content = new_content
        fe.write()
        return None

    def run(self) -> None:
        self.write()
        return None
