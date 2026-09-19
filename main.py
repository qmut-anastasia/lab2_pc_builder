# Точка входа в систему подбора комплектующих для ПК
from modules.catalog import load_catalog
from modules.compatibility import check_cpu_motherboard

def main():
    cpu_list = load_catalog("data/cpu.json")
    print(f"Загружено {len(cpu_list)} процессоров")

if __name__ == "__main__":
    main()