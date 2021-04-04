import subprocess

from setup import Dhcpcd, Dnsmasq, Hostapd, NetPlan, SystemdNetwork, Ufw

ALLOW_SSH = True
IS_WIFI_ROUTER_RPI_OS = True
IS_WIFI_ROUTER_UBUNTU = False
IS_WIFI_TO_LAN_ROUTER = False
IS_LAN_TO_LAN_ROUTER = False
IS_WIFI_CLIENT = False
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
    l_runner = Dhcpcd.Dhcpcd()
    l_runner.lan_interface = LAN_INTERFACE_NAME
    l_runner.lan_ip_address = LAN_IP_ADDRESS
    l_runner.run()
    return None


def run_systemd_network() -> None:
    l_runner = SystemdNetwork.SystemdNetwork()
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
    l_runner = Hostapd.Hostapd()
    l_runner.lan_interface = LAN_INTERFACE_NAME
    l_runner.ess_id = ESS_ID
    l_runner.passphrase = PASSPHRASE
    l_runner.run()
    return None


def run_netplan() -> None:
    l_runner = NetPlan.NetPlan()
    l_runner.is_wifi_router_ubuntu = IS_WIFI_ROUTER_UBUNTU
    l_runner.is_wifi_to_lan_router = IS_WIFI_TO_LAN_ROUTER
    l_runner.is_wifi_client = IS_WIFI_CLIENT
    l_runner.wan_interface_name = WAN_INTERFACE_NAME
    l_runner.lan_interface_name = LAN_INTERFACE_NAME
    l_runner.lan_ip_address = LAN_IP_ADDRESS
    l_runner.ess_id = ESS_ID
    l_runner.passphrase = PASSPHRASE
    l_runner.run()
    return None


def enable_hostapd() -> None:
    subprocess.call(['systemctl', 'unmask', 'hostapd'])
    subprocess.call(['systemctl', 'enable', 'hostapd'])
    return None


def disable_systemd_resolved() -> None:
    subprocess.call(['systemctl', 'stop', 'systemd-resolved'])
    subprocess.call(['systemctl', 'disable', 'systemd-resolved'])
    subprocess.call(['systemctl', 'mask', 'systemd-resolved'])
    return None


def run() -> None:
    if IS_WIFI_ROUTER_RPI_OS:
        run_ufw()
        run_dhcpcd()
        run_dnsmasq()
        run_hostapd()
        enable_hostapd()
    elif IS_WIFI_ROUTER_UBUNTU:
        run_ufw()
        run_systemd_network()
        run_dnsmasq()
        run_hostapd()
        run_netplan()
        enable_hostapd()
        disable_systemd_resolved()
    elif IS_WIFI_TO_LAN_ROUTER:
        run_ufw()
        run_dnsmasq()
        run_netplan()
        disable_systemd_resolved()
    elif IS_LAN_TO_LAN_ROUTER:
        run_ufw()
        run_dnsmasq()
        run_netplan()
        disable_systemd_resolved()
    elif IS_WIFI_CLIENT:
        run_netplan()
    return None


if __name__ == '__main__':
    run()
