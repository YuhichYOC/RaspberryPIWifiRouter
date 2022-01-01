import subprocess

from setup import Dhcpcd, Dnsmasq, Hostapd, NetPlan, SystemdNetwork, Ufw

ALLOW_SSH = True
IS_WIFI_ROUTER_RPI_OS = True
IS_WIFI_ROUTER_UBUNTU = False
IS_WIFI_TO_LAN_ROUTER_UBUNTU = False
IS_LAN_TO_LAN_ROUTER_UBUNTU = False
IS_WIFI_CLIENT_UBUNTU = False
IS_2_WAY_ROUTER_UBUNTU = False
IS_LAN_TO_WIFI_BRIDGE_UBUNTU = False
DOMAIN_NAME = ''
WAN_INTERFACE_NAME = 'eth0'
LAN_INTERFACE_NAME = 'wlan0'
LAN_IP_ADDRESS = ''
LAN_2_WAY_ETH_INTERFACE_NAME = ''
LAN_2_WAY_ETH_IP_ADDRESS_WITH_MASK = ''
LAN_2_WAY_ETH_IP_ADDRESS_WITHOUT_MASK = ''
LAN_2_WAY_ETH_IP_ADDRESS_START_WITH_MASK = ''
LAN_2_WAY_WIFI_INTERFACE_NAME = ''
LAN_2_WAY_WIFI_IP_ADDRESS_WITH_MASK = ''
LAN_2_WAY_WIFI_IP_ADDRESS_WITHOUT_MASK = ''
LAN_2_WAY_WIFI_IP_ADDRESS_START_WITH_MASK = ''
DHCP_RANGE_FROM = ''
DHCP_RANGE_TO = ''
DHCP_2_WAY_ETH_RANGE_FROM = ''
DHCP_2_WAY_ETH_RANGE_TO = ''
DHCP_2_WAY_WIFI_RANGE_FROM = ''
DHCP_2_WAY_WIFI_RANGE_TO = ''
ESS_ID = ''
PASSPHRASE = ''


def run_ufw() -> None:
    l_runner = Ufw.Ufw()
    l_runner.allow_ssh = ALLOW_SSH
    l_runner.wan_interface = WAN_INTERFACE_NAME
    l_runner.run()
    return None


def run_ufw_2_way() -> None:
    l_runner = Ufw.Ufw()
    l_runner.is_2_way = IS_2_WAY_ROUTER_UBUNTU
    l_runner.allow_ssh = ALLOW_SSH
    l_runner.wan_interface = WAN_INTERFACE_NAME
    l_runner.lan_2_way_eth_ip_address_start_with_mask = LAN_2_WAY_ETH_IP_ADDRESS_START_WITH_MASK
    l_runner.lan_2_way_wifi_ip_address_start_with_mask = LAN_2_WAY_WIFI_IP_ADDRESS_START_WITH_MASK
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
    l_runner.is_lan_to_wifi_bridge_ubuntu = IS_LAN_TO_WIFI_BRIDGE_UBUNTU
    l_runner.lan_interface = LAN_INTERFACE_NAME
    l_runner.lan_ip_address = LAN_IP_ADDRESS
    l_runner.run()
    return None


def run_systemd_network_2_way() -> None:
    l_runner = SystemdNetwork.SystemdNetwork()
    l_runner.is_2_way = IS_2_WAY_ROUTER_UBUNTU
    l_runner.lan_interface = LAN_2_WAY_WIFI_INTERFACE_NAME
    l_runner.lan_ip_address_with_mask = LAN_2_WAY_WIFI_IP_ADDRESS_WITH_MASK
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


def run_dnsmasq_2_way() -> None:
    l_runner = Dnsmasq.Dnsmasq()
    l_runner.is_2_way = IS_2_WAY_ROUTER_UBUNTU
    l_runner.domain_name = DOMAIN_NAME
    l_runner.lan_2_way_eth_interface_name = LAN_2_WAY_ETH_INTERFACE_NAME
    l_runner.lan_2_way_eth_ip_address_without_mask = LAN_2_WAY_ETH_IP_ADDRESS_WITHOUT_MASK
    l_runner.lan_2_way_wifi_interface_name = LAN_2_WAY_WIFI_INTERFACE_NAME
    l_runner.lan_2_way_wifi_ip_address_without_mask = LAN_2_WAY_WIFI_IP_ADDRESS_WITHOUT_MASK
    l_runner.dhcp_2_way_eth_range_from = DHCP_2_WAY_ETH_RANGE_FROM
    l_runner.dhcp_2_way_eth_range_to = DHCP_2_WAY_ETH_RANGE_TO
    l_runner.dhcp_2_way_wifi_range_from = DHCP_2_WAY_WIFI_RANGE_FROM
    l_runner.dhcp_2_way_wifi_range_to = DHCP_2_WAY_WIFI_RANGE_TO
    l_runner.router_ip = LAN_IP_ADDRESS
    l_runner.run()
    return None


def run_hostapd() -> None:
    l_runner = Hostapd.Hostapd()
    l_runner.is_lan_to_wifi_bridge_ubuntu = IS_LAN_TO_WIFI_BRIDGE_UBUNTU
    l_runner.lan_interface = LAN_INTERFACE_NAME
    l_runner.ess_id = ESS_ID
    l_runner.passphrase = PASSPHRASE
    l_runner.run()
    return None


def run_hostapd_2_way() -> None:
    l_runner = Hostapd.Hostapd()
    l_runner.lan_interface = LAN_2_WAY_WIFI_INTERFACE_NAME
    l_runner.ess_id = ESS_ID
    l_runner.passphrase = PASSPHRASE
    l_runner.run()
    return None


def run_netplan() -> None:
    l_runner = NetPlan.NetPlan()
    l_runner.is_wifi_router_ubuntu = IS_WIFI_ROUTER_UBUNTU
    l_runner.is_wifi_to_lan_router_ubuntu = IS_WIFI_TO_LAN_ROUTER_UBUNTU
    l_runner.is_lan_to_lan_router_ubuntu = IS_LAN_TO_LAN_ROUTER_UBUNTU
    l_runner.is_wifi_client_ubuntu = IS_WIFI_CLIENT_UBUNTU
    l_runner.is_lan_to_wifi_bridge_ubuntu = IS_LAN_TO_WIFI_BRIDGE_UBUNTU
    l_runner.wan_interface_name = WAN_INTERFACE_NAME
    l_runner.lan_interface_name = LAN_INTERFACE_NAME
    l_runner.lan_ip_address = LAN_IP_ADDRESS
    l_runner.ess_id = ESS_ID
    l_runner.passphrase = PASSPHRASE
    l_runner.run()
    return None


def run_netplan_2_way() -> None:
    l_runner = NetPlan.NetPlan()
    l_runner.is_2_way_router_ubuntu = IS_2_WAY_ROUTER_UBUNTU
    l_runner.wan_interface_name = WAN_INTERFACE_NAME
    l_runner.lan_2_way_interface_name = LAN_2_WAY_ETH_INTERFACE_NAME
    l_runner.lan_2_way_ip_address_with_mask = LAN_2_WAY_ETH_IP_ADDRESS_WITH_MASK
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
    elif IS_WIFI_TO_LAN_ROUTER_UBUNTU:
        run_ufw()
        run_dnsmasq()
        run_netplan()
        disable_systemd_resolved()
    elif IS_LAN_TO_LAN_ROUTER_UBUNTU:
        run_ufw()
        run_dnsmasq()
        run_netplan()
        disable_systemd_resolved()
    elif IS_WIFI_CLIENT_UBUNTU:
        run_netplan()
    elif IS_2_WAY_ROUTER_UBUNTU:
        run_ufw_2_way()
        run_systemd_network_2_way()
        run_dnsmasq_2_way()
        run_hostapd_2_way()
        run_netplan_2_way()
        enable_hostapd()
        disable_systemd_resolved()
    elif IS_LAN_TO_WIFI_BRIDGE_UBUNTU:
        run_hostapd()
        run_netplan()
        run_systemd_network()
        enable_hostapd()
    return None


if __name__ == '__main__':
    run()
