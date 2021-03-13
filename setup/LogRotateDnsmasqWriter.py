from . import FileEntity


class LogRotateDnsmasqWriter:

    @staticmethod
    def write() -> None:
        content = [
            '/var/log/dnsmasq.log {',
            '    missingok',
            '    rotate 9',
            '    maxsize 100M',
            '}',
        ]
        fe = FileEntity.FileEntity()
        fe.path = '/etc/logrotate.d/dnsmasq'
        fe.content = content
        fe.write()
        return None

    def run(self) -> None:
        self.write()
        return None
