# Точка входа в систему подбора комплектующих для ПК
from modules.catalog import load_catalog
from modules.builder import build_pc_by_budget

def main():
    cpu_list = load_catalog("data/cpu.json")
    print(f"Загружено {len(cpu_list)} процессоров")

if __name__ == "__main__":
    main()