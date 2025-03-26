import platform
import os
import socket
import subprocess
import psutil

def get_system_info():
    info = {}
    uname = platform.uname()
    info['System'] = uname.system
    info['Node Name'] = uname.node
    info['Version'] = uname.version
    info['Architecture'] = uname.machine
    info['Processor'] = uname.processor
    return info

def get_network_info():
    interfaces = psutil.net_if_addrs()
    network_info = {}
    for interface, addrs in interfaces.items():
        iface_info = {'addresses': []}
        for addr in addrs:
            iface_info['addresses'].append({
                'family': addr.family,
                'address': addr.address,
                'netmask': addr.netmask,
                'broadcast': addr.broadcast,
            })
        network_info[interface] = iface_info
    return network_info

def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        part_info = {
            'device': partition.device,
            'mount_point': partition.mountpoint,
            'file_system': partition.fstype,
            'total': usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': usage.percent,
        }
        disk_info.append(part_info)
    return disk_info

def get_ram_info():
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()
    ram_info = {
        'total': virtual_memory.total,
        'available': virtual_memory.available,
        'used': virtual_memory.used,
        'free': virtual_memory.free,
        'percent': virtual_memory.percent,
        'swap_total': swap_memory.total,
        'swap_free': swap_memory.free,
        'swap_used': swap_memory.used,
        'swap_percent': swap_memory.percent,
    }
    return ram_info

def get_cpu_info():
    cpu_info = {
        'count': psutil.cpu_count(logical=True),
        'cores': psutil.cpu_count(logical=False),
        'freq': psutil.cpu_freq().current,
    }
    return cpu_info

def main():
    print("System Information:")
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"  {key}: {value}")

    print("\nNetwork Interfaces:")
    network_info = get_network_info()
    for interface, info in network_info.items():
        print(f"  Interface: {interface}")
        for addr in info['addresses']:
            print(f"    Address Type: {addr['family']}, Address: {addr['address']}")

    print("\nDisk Partitions:")
    disk_info = get_disk_info()
    for partition in disk_info:
        print(f"  Device: {partition['device']}, Mount Point: {partition['mount_point']}, File System:
{partition['file_system']}")
        print(f"    Total: {partition['total']}, Used: {partition['used']}, Free: {partition['free']}, Percent:
{partition['percent']}")

    print("\nRAM Information:")
    ram_info = get_ram_info()
    for key, value in ram_info.items():
        print(f"  {key}: {value}")

    print("\nCPU Information:")
    cpu_info = get_cpu_info()
    for key, value in cpu_info.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()