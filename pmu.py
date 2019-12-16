import sys

'''
PMU : Python 3 Memory Usage library
'''


def size_to_str(size):
    if size <= 0:
        return "ERROR : size <= 0"
    for unit in ['   ', 'Kio', 'Mio', 'Gio', 'Tio']:
        if size < 1024.0:
            return "%4.1f %s" % (size, unit)
        size /= 1024.0
    return ">= 1 Pio"


def view(min_size=1024, max_items=10):
    print("╔══════════════════════╦═══════════════╗")
    print("║ Name                 ║          Size ║")
    print("╠══════════════════════╬═══════════════╣")

    for name, size in sorted(((name, sys.getsizeof(value)) for name, value in globals().items()),
                             key=lambda x: -x[1])[:max_items]:
        if size >= min_size:
            print("║ {:<20} ║  {:>12} ║".format(name, size_to_str(size)))

    print("╚══════════════════════╩═══════════════╝")

