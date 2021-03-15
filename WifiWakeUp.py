import subprocess

LAN_INTERFACE_NAME = 'wlan0'
LAN_IP_ADDRESS = ''
ESS_ID = ''
PASSPHRASE = ''


class FileEntity:

    def __init__(self):
        self.f_content = []
        self.f_path = ''

    @property
    def path(self) -> str:
        return self.f_path

    @property
    def content(self) -> list:
        return self.f_content

    @path.setter
    def path(self, arg: str):
        self.f_path = arg

    @content.setter
    def content(self, arg: list):
        self.f_content = arg

    def read(self) -> None:
        self.content.clear()
        with open(self.path, 'r') as f:
            lines = f.read().split('\n')
            for line in lines:
                self.content.append(line)
        return None

    def write(self) -> None:
        with open(self.path, 'w') as f:
            for line in self.content:
                f.write(line)
                f.write('\n')
        return None


class HostapdConfEditor:

    def __init__(self):
        self.f_ess_id = ''
        self.f_passphrase = ''

    @property
    def ess_id(self) -> str:
        return self.f_ess_id

    @property
    def passphrase(self) -> str:
        return self.f_passphrase

    @ess_id.setter
    def ess_id(self, arg: str):
        self.f_ess_id = arg

    @passphrase.setter
    def passphrase(self, arg: str):
        self.f_passphrase = arg

    def edit(self) -> None:
        fe = FileEntity()
        fe.path = '/etc/hostapd/hostapd.conf'
        fe.read()
        new_content = []
        for line in fe.content:
            if line.startswith('ssid='):
                new_content.append('ssid=' + self.ess_id)
            elif line.startswith('wpa_passphrase='):
                new_content.append('wpa_passphrase=' + self.passphrase)
            else:
                new_content.append(line)
        fe.content = new_content
        fe.write()
        return None

    def run(self) -> None:
        self.edit()
        return None


def restart_network_manager() -> None:
    subprocess.call(['systemctl', 'restart', 'NetworkManager'])
    return None


def add_ip_to_interface() -> None:
    subprocess.call(['ip', 'addr', 'add', LAN_IP_ADDRESS + '/24', 'dev', LAN_INTERFACE_NAME])
    return None


def edit_hostapd_conf() -> None:
    l_runner = HostapdConfEditor()
    l_runner.ess_id = ESS_ID
    l_runner.passphrase = PASSPHRASE
    l_runner.run()
    return None


def restart_hostapd() -> None:
    subprocess.call(['systemctl', 'restart', 'hostapd'])
    return None


def run() -> None:
    restart_network_manager()
    add_ip_to_interface()
    edit_hostapd_conf()
    restart_hostapd()
    return None


if __name__ == '__main__':
    run()
