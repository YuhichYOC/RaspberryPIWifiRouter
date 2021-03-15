from . import FileEntity


class ResolvDnsmasqConfWriter:

    @staticmethod
    def write() -> None:
        content = [
            'nameserver 8.8.8.8',
            'nameserver 8.8.4.4',
        ]
        fe = FileEntity.FileEntity()
        fe.path = '/etc/resolv.dnsmasq.conf'
        fe.content = content
        fe.write()
        return None

    def run(self) -> None:
        self.write()
        return None
