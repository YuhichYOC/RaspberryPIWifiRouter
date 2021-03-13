import subprocess


class PackageInstaller:

    def __init__(self):
        self.f_is_wifi_router = True

    @property
    def is_wifi_router(self) -> bool:
        return self.f_is_wifi_router

    @is_wifi_router.setter
    def is_wifi_router(self, arg: bool):
        self.f_is_wifi_router = arg

    @staticmethod
    def install_hostapd() -> None:
        subprocess.call(['apt', 'install', '-y', 'hostapd'])
        return None

    @staticmethod
    def install_dnsmasq() -> None:
        subprocess.call(['apt', 'install', '-y', 'dnsmasq'])
        return None

    @staticmethod
    def install_iptables_persistent() -> None:
        subprocess.call(['apt', 'install', '-y', 'iptables-persistent'])
        return None

    def run(self) -> None:
        if self.is_wifi_router:
            self.install_hostapd()
        self.install_dnsmasq()
        self.install_iptables_persistent()
        return None
