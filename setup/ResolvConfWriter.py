import subprocess

from . import FileEntity


class ResolvConfWriter:

    @staticmethod
    def unlink_resolv() -> None:
        subprocess.call(['unlink', '/etc/resolv.conf'])
        return None

    @staticmethod
    def write() -> None:
        content = [
            'nameserver 9.9.9.9',
            'nameserver 8.8.8.8',
            'nameserver 8.8.4.4',
        ]
        fe = FileEntity.FileEntity()
        fe.path = '/etc/resolv.conf'
        fe.content = content
        fe.write()
        return None

    def run(self) -> None:
        self.unlink_resolv()
        self.write()
        return None
