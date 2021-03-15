import subprocess

from setup import Dnsmasq, Hostapd, IpTables

IS_WIFI_ROUTER = True
APPROVE_CONNECTION_FROM_WAN = False
DOMAIN_NAME = ''
WAN_INTERFACE_NAME = 'eth0'
LAN_INTERFACE_NAME = 'wlan0'
GATEWAY4 = ''
WAN_IP_ADDRESS = ''
LAN_IP_ADDRESS = ''
DHCP_RANGE_FROM = ''
DHCP_RANGE_TO = ''
ESS_ID = ''
PASSPHRASE = ''


def run_iptables() -> None:
    l_runner = IpTables.IpTables()
    l_runner.approve_connection_from_wan = APPROVE_CONNECTION_FROM_WAN
    l_runner.wan = WAN_INTERFACE_NAME
    l_runner.lan = LAN_INTERFACE_NAME
    l_runner.run()
    return None


def run_dnsmasq() -> None:
    l_runner = Dnsmasq.Dnsmasq()
    l_runner.domain_name = DOMAIN_NAME
    l_runner.wan_interface_name = WAN_INTERFACE_NAME
    l_runner.lan_interface_name = LAN_INTERFACE_NAME
    l_runner.range_from = DHCP_RANGE_FROM
    l_runner.range_to = DHCP_RANGE_TO
    l_runner.router_ip = LAN_IP_ADDRESS
    l_runner.run()
    return None


def run_hostapd() -> None:
    if IS_WIFI_ROUTER:
        l_runner = Hostapd.Hostapd()
        l_runner.interface = LAN_INTERFACE_NAME
        l_runner.ess_id = ESS_ID
        l_runner.passphrase = PASSPHRASE
        l_runner.run()
    return None


def enable_hostapd() -> None:
    if IS_WIFI_ROUTER:
        subprocess.call(['systemctl', 'unmask', 'hostapd'])
        subprocess.call(['systemctl', 'enable', 'hostapd'])
    return None


def disable_systemd_resolved() -> None:
    subprocess.call(['systemctl', 'stop', 'systemd-resolved'])
    subprocess.call(['systemctl', 'disable', 'systemd-resolved'])
    subprocess.call(['systemctl', 'mask', 'systemd-resolved'])
    return None


def run() -> None:
    run_iptables()
    run_dnsmasq()
    run_hostapd()
    enable_hostapd()
    disable_systemd_resolved()
    return None


if __name__ == '__main__':
    run()
