import subprocess


class IpTablesWriter:

    def __init__(self):
        self.f_approve_connection_from_wan = False
        self.f_wan = ''
        self.f_lan = ''

    @property
    def approve_connection_from_wan(self) -> bool:
        return self.f_approve_connection_from_wan

    @property
    def wan(self) -> str:
        return self.f_wan

    @property
    def lan(self) -> str:
        return self.f_lan

    @approve_connection_from_wan.setter
    def approve_connection_from_wan(self, arg: bool):
        self.f_approve_connection_from_wan = arg

    @wan.setter
    def wan(self, arg: str):
        self.f_wan = arg

    @lan.setter
    def lan(self, arg: str):
        self.f_lan = arg

    @staticmethod
    def call_iptables_masquerade(a_interface: str) -> None:
        subprocess.call(
            [
                'iptables',
                '-t', 'nat',
                '-A', 'POSTROUTING',
                '-o', a_interface,
                '-j', 'MASQUERADE'
            ]
        )
        return None

    @staticmethod
    def call_iptables_wan_to_lan(a_wan: str, a_lan: str) -> None:
        subprocess.call(
            [
                'iptables',
                '-A', 'FORWARD',
                '-i', a_wan,
                '-o', a_lan,
                '-m', 'state', '--state', 'RELATED,ESTABLISHED',
                '-j', 'ACCEPT'
            ]
        )
        return None

    @staticmethod
    def call_iptables_lan_to_wan(a_lan: str, a_wan: str) -> None:
        subprocess.call(
            [
                'iptables',
                '-A', 'FORWARD',
                '-i', a_lan,
                '-o', a_wan,
                '-j', 'ACCEPT'
            ]
        )
        return None

    def write_wan_to_lan(self) -> None:
        self.call_iptables_masquerade(self.wan)
        self.call_iptables_wan_to_lan(self.wan, self.lan)
        self.call_iptables_lan_to_wan(self.lan, self.wan)
        return None

    def write_lan_to_wan(self) -> None:
        self.call_iptables_masquerade(self.lan)
        self.call_iptables_wan_to_lan(self.lan, self.wan)
        self.call_iptables_lan_to_wan(self.wan, self.lan)
        return None

    @staticmethod
    def call_persistent() -> None:
        subprocess.call(['/etc/init.d/netfilter-persistent', 'save'])
        return None

    def run(self) -> None:
        self.write_wan_to_lan()
        if self.approve_connection_from_wan:
            self.write_lan_to_wan()
        self.call_persistent()
        return None
