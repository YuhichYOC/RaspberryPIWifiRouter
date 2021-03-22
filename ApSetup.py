import subprocess

from setup import Dhcpcd, Dnsmasq, Hostapd, NetPlan, Ufw

IS_TEST_AP = False
ALLOW_SSH = True
# Wifi router setup supports only Raspberry PI OS. Because I don't know how to fix the IP address
# of the wifi interface, not connecting any wifi network but has this own IP address, with netplan.
IS_WIFI_ROUTER = True
DOMAIN_NAME = ''
WAN_INTERFACE_NAME = 'eth0'
LAN_INTERFACE_NAME = 'wlan0'
LAN_IP_ADDRESS = ''
DHCP_RANGE_FROM = ''
DHCP_RANGE_TO = ''
ESS_ID = ''
PASSPHRASE = ''


def run_ufw() -> None:
    l_runner = Ufw.Ufw()
    l_runner.allow_ssh = ALLOW_SSH
    l_runner.wan_interface = WAN_INTERFACE_NAME
    l_runner.run()
    return None


def run_dhcpcd() -> None:
    if IS_WIFI_ROUTER:
        l_runner = Dhcpcd.Dhcpcd()
        l_runner.lan_interface = LAN_INTERFACE_NAME
        l_runner.lan_ip_address = LAN_IP_ADDRESS
        l_runner.run()
    return None


def run_dnsmasq() -> None:
    l_runner = Dnsmasq.Dnsmasq()
    l_runner.domain_name = DOMAIN_NAME
    l_runner.lan_interface_name = LAN_INTERFACE_NAME
    l_runner.range_from = DHCP_RANGE_FROM
    l_runner.range_to = DHCP_RANGE_TO
    l_runner.router_ip = LAN_IP_ADDRESS
    l_runner.run()
    return None


def run_hostapd() -> None:
    if IS_WIFI_ROUTER:
        l_runner = Hostapd.Hostapd()
        l_runner.lan_interface = LAN_INTERFACE_NAME
        l_runner.ess_id = ESS_ID
        l_runner.passphrase = PASSPHRASE
        l_runner.run()
    return None


def run_netplan() -> None:
    if IS_WIFI_ROUTER:
        return None
    l_runner = NetPlan.NetPlan()
    l_runner.is_test_ap = IS_TEST_AP
    l_runner.is_wifi_router = IS_WIFI_ROUTER
    l_runner.wan_interface_name = WAN_INTERFACE_NAME
    l_runner.lan_interface_name = LAN_INTERFACE_NAME
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
    if IS_WIFI_ROUTER:
        return None
    subprocess.call(['systemctl', 'stop', 'systemd-resolved'])
    subprocess.call(['systemctl', 'disable', 'systemd-resolved'])
    subprocess.call(['systemctl', 'mask', 'systemd-resolved'])
    return None


def run() -> None:
    run_ufw()
    run_dhcpcd()
    run_dnsmasq()
    run_hostapd()
    run_netplan()
    enable_hostapd()
    disable_systemd_resolved()
    return None


if __name__ == '__main__':
    run()
