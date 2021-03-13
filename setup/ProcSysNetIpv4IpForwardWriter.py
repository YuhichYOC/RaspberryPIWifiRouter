from . import FileEntity


class ProcSysNetIpv4IpForwardWriter:

    @staticmethod
    def write() -> None:
        content = ['1']
        fe = FileEntity.FileEntity()
        fe.path = '/proc/sys/net/ipv4/ip_forward'
        fe.content = content
        fe.write()
        return None

    def run(self) -> None:
        self.write()
        return None
