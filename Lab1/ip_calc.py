import re


def get_mask(raw_address):
    """
    Returns mask decimal and binary from raw IP address
    :param raw_address: str
    :return: decimal_mask, binary_mask
    >>> get_mask('192.168.10.10/16')
    ('255.255.0.0', '11111111111111110000000000000000')
    """
    prefix = int(raw_address[-2:])
    str_mask_bin = '1' * prefix + '0' * (32 - prefix)
    lst_mask_bin = str_mask_bin[:8], str_mask_bin[8:16], str_mask_bin[16:24], str_mask_bin[24:]
    mask_dec = '.'.join([str(int(i, 2)) for i in lst_mask_bin])
    return mask_dec, str_mask_bin


def convert_ip_to_bin(ip):
    """
    Converts IP address to binary
    :param ip: str
    :return:
    >>> convert_ip_to_bin('192.168.10.10')
    '11000000.10101000.00001010.00001010'
    """
    ip_lst = ip.split('.')
    bin_ip = '.'.join([bin(int(x) + 256)[3:] for x in ip_lst])
    return bin_ip

def get_ip_from_raw_address(raw_address: str):
    """
    Returns an IP address
    :param raw_address: str
    :return: str
    >>> get_ip_from_raw_address('192.168.10.10/16')
    '192.168.10.10'
    """
    if type(raw_address) != str:
        return None
    return raw_address[:-3]


def get_network_address_from_raw_address(raw_address: str) -> str:
    """
    Для визначення номера мережі та номера вузла потрібно з IP-адресою та маскою
    виконати додаткові обчислення. Для обчислення номера мережі за заданою IP-адресою та
    маскою необхідно виконати побітове “І” (AND) між адресою та маскою. Таку операцію
    називають накладанням маски на адресу.

    :param raw_address:str
    :return:str
    >>> get_network_address_from_raw_address('192.168.10.10/16')
    '192.168.0.0'
    """
    if type(raw_address) != str:
        return None
    ip = get_ip_from_r  aw_address(raw_address)
    mask_dec, mask_bin = get_mask(raw_address)
    net_address = '.'.join(
        [str(int(ip.split('.')[i]) & int(mask_dec.split('.')[i])) for i in range(len(ip.split('.')))])
    return net_address


def get_broadcast_address_from_raw_address(raw_address: str) -> str:
    """
    Returns broadcast address from raw_address
    :param raw_address: str
    :return: broadcast_address: str
    >>> get_broadcast_address_from_raw_address('192.168.10.10/16')
    '192.168.255.255'
    """
    if type(raw_address) != str:
        return None
    ip = get_ip_from_raw_address(raw_address)
    mask_dec, mask_bin = get_mask(raw_address)
    inverted_mask = '.'.join([str(255 - int(x)) for x in mask_dec.split('.')])
    broadcast_address = '.'.join([str(int(ip.split('.')[i]) | int(inverted_mask.split('.')[i]))
                                  for i in range(len(ip.split('.')))])
    return broadcast_address


def get_binary_mask_from_raw_address(raw_address: str) -> str:
    """
    Returns binary mask from raw address
    :param raw_address: str
    :return: subnet_mask, str
    >>> get_binary_mask_from_raw_address('192.168.10.10/16')
    '11111111.11111111.00000000.00000000'
    """
    if type(raw_address) != str:
        return None
    bin_mask = get_mask(raw_address)[1]
    return '.'.join([bin_mask[:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:]])


def get_first_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    Returns first usable ip address
    :param raw_address: str
    :return: first_node, str
    >>> get_first_usable_ip_address_from_raw_address('192.168.10.10/16')
    '192.168.0.1'
    """
    if type(raw_address) != str:
        return None
    network_address = get_network_address_from_raw_address(raw_address).split('.')
    first_node = '.'.join(network_address[:-1]) + '.' + str(int(network_address[-1]) + 1)
    return first_node


def get_penultimate_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    Returns penultimate usable ip address
    :param raw_address: str
    :return: pre-last node, str
    >>> get_penultimate_usable_ip_address_from_raw_address('192.168.10.10/16')
    '192.168.255.253'
    """
    if type(raw_address) != str:
        return None
    broadcast = get_broadcast_address_from_raw_address(raw_address).split('.')
    prelast_node = '.'.join(broadcast[:-1]) + '.' + str(int(broadcast[-1]) - 2)
    return prelast_node


def get_number_of_usable_hosts_from_raw_address(raw_address: str) -> int:
    """
    Returns the number of available IP adresses
    :param raw_address: str
    :return: int
    >>> get_number_of_usable_hosts_from_raw_address('192.168.10.10/16')
    65534
    """
    if type(raw_address) != str:
        return None
    prefix = int(raw_address[-2:])
    return (2**(32 - prefix)) - 2


def get_ip_class_from_raw_address(raw_address: str) -> str:
    """
    Returns a class of ip address
    :param raw_address: str
    :return: class of ip address, e.g 'A' or 'B', str
    >>> get_ip_class_from_raw_address('192.168.10.10/16')
    'C'
    """
    if type(raw_address) != str:
        return None
    ip_first_part = raw_address.split('.')[0]
    if int(ip_first_part) in range(1, 126):
        return 'A'
    if int(ip_first_part) in range(128, 192):
        return 'B'
    if int(ip_first_part) in range(192, 224):
        return 'C'
    if int(ip_first_part) in range(224, 240):
        return 'D'
    if int(ip_first_part) in range(240, 248):
        return 'E'


def check_private_ip_address_from_raw_address(raw_address: str) -> bool:
    """
    Is an address a private one?
    :param raw_address: str
    :return: True if address is private, else False
    >>> check_private_ip_address_from_raw_address('192.168.10.10/16')
    True
    """
    if type(raw_address) != str:
        return None
    prefix = int(raw_address[-2:])
    ip_address = get_ip_from_raw_address(raw_address).split('.')
    if (ip_address[0] == '10' and prefix == 8) or (ip_address[:2] == ['172', '16'] and prefix == 12) or \
            (ip_address[:2] == ['192', '168'] and prefix == 16):
        return True
    return False


if __name__ == '__main__':
    address = input()
    if re.findall('^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))$', address):
        print('IP address: {}'.format(get_ip_from_raw_address(address)))
        print('Network address: {}'.format(get_network_address_from_raw_address(address)))
        print('Broadcast address: {}'.format(get_broadcast_address_from_raw_address(address)))
        print('Binary Subnet Mask: {}'.format(get_binary_mask_from_raw_address(address)))
        print('First usable host IP: {}'.format(get_first_usable_ip_address_from_raw_address(address)))
        print('Penultimate usable host IP: {}'.format(get_penultimate_usable_ip_address_from_raw_address(address)))
        print('Number of usable Hosts: {}'.format(get_number_of_usable_hosts_from_raw_address(address)))
        print('IP class: {}'.format(get_ip_class_from_raw_address(address)))
        print('IP type private: {}'.format(check_private_ip_address_from_raw_address(address)))
    elif re.findall('^([0-9]{1,3}\.){3}[0-9]{1,3}$', address):
        print('Missing prefix')
    else:
        print('Error')
