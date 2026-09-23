def check_cpu_motherboard(cpu, motherboard):
    return cpu["socket"] == motherboard["socket"]

def check_ram_motherboard(ram, motherboard):
    return ram["type"] == motherboard["ram_type"]