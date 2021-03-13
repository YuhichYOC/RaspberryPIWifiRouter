import subprocess

from setup import \
    DefaultHostapdWriter, \
    DnsmasqConfWriter, \
    HostapdConfWriter, \
    IpTablesWriter, \
    LogRotateDnsmasqWriter, \
    NetplanConfigWriter, \
    NetworkManagerConfWriter, \
    PackageInstaller, \
    ProcSysNetIpv4IpForwardWriter, \
    ResolvConfWriter, \
    SysctlConfWriter, \
    SystemdResolvedConfWriter

IS_WIFI_ROUTER = True
APPROVE_CONNECTION_FROM_WAN = False
WAN = 'eth0'
LAN = 'wlan0'
GATEWAY4 = ''
ETH_IP_ADDRESS = ''
WLAN_IP_ADDRESS = ''
RANGE_FROM = ''
RANGE_TO = ''
ESS_ID = ''
PASSPHRASE = ''


def run_package_installer() -> None:
    l_runner = PackageInstaller.PackageInstaller()
    l_runner.is_wifi_router = IS_WIFI_ROUTER
    l_runner.run()
    return None


def run_netplan_config_writer() -> None:
    l_runner = NetplanConfigWriter.NetplanConfigWriter()
    l_runner.is_wifi_router = IS_WIFI_ROUTER
    l_runner.eth_interface_name = WAN
    l_runner.eth_ip_address = ETH_IP_ADDRESS
    l_runner.wlan_interface_name = LAN
    l_runner.wlan_ip_address = WLAN_IP_ADDRESS
    l_runner.gateway4 = GATEWAY4
    l_runner.ess_id = ESS_ID
    l_runner.passphrase = PASSPHRASE
    l_runner.run()
    return None


def run_sysctl_conf_writer() -> None:
    l_runner = SysctlConfWriter.SysctlConfWriter()
    l_runner.run()
    return None


def run_proc_sys_net_ipv4_ip_forward_writer() -> None:
    l_runner = ProcSysNetIpv4IpForwardWriter.ProcSysNetIpv4IpForwardWriter()
    l_runner.run()
    return None


def run_ip_tables_writer() -> None:
    l_runner = IpTablesWriter.IpTablesWriter()
    l_runner.approve_connection_from_wan = APPROVE_CONNECTION_FROM_WAN
    l_runner.wan = WAN
    l_runner.lan = LAN
    l_runner.run()
    return None


def run_default_hostapd_writer() -> None:
    if IS_WIFI_ROUTER:
        l_runner = DefaultHostapdWriter.DefaultHostapdWriter()
        l_runner.run()
    return None


def run_hostapd_conf_writer() -> None:
    if IS_WIFI_ROUTER:
        l_runner = HostapdConfWriter.HostapdConfWriter()
        l_runner.interface = LAN
        l_runner.ess_id = ESS_ID
        l_runner.passphrase = PASSPHRASE
        l_runner.run()
    return None


def call_systemctl_stop_dnsmasq() -> None:
    subprocess.call(['systemctl', 'stop', 'dnsmasq'])
    return None


def run_dnsmasq_conf_writer() -> None:
    l_runner = DnsmasqConfWriter.DnsmasqConfWriter()
    l_runner.interface = LAN
    l_runner.self_ip_address = ETH_IP_ADDRESS
    l_runner.range_from = RANGE_FROM
    l_runner.range_to = RANGE_TO
    l_runner.run()
    return None


def run_log_rotate_dnsmasq_writer() -> None:
    l_runner = LogRotateDnsmasqWriter.LogRotateDnsmasqWriter()
    l_runner.run()
    return None


def run_systemd_resolved_conf_writer() -> None:
    l_runner = SystemdResolvedConfWriter.SystemdResolvedConfWriter()
    l_runner.run()
    return None


def run_network_manager_conf_writer() -> None:
    l_runner = NetworkManagerConfWriter.NetworkManagerConfWriter()
    l_runner.run()
    return None


def run_resolv_conf_writer() -> None:
    l_runner = ResolvConfWriter.ResolvConfWriter()
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
    run_package_installer()
    run_netplan_config_writer()
    run_sysctl_conf_writer()
    run_proc_sys_net_ipv4_ip_forward_writer()
    run_ip_tables_writer()
    run_default_hostapd_writer()
    run_hostapd_conf_writer()
    call_systemctl_stop_dnsmasq()
    run_dnsmasq_conf_writer()
    run_log_rotate_dnsmasq_writer()
    run_systemd_resolved_conf_writer()
    run_network_manager_conf_writer()
    run_resolv_conf_writer()
    enable_hostapd()
    disable_systemd_resolved()
    return None


if __name__ == '__main__':
    run()
