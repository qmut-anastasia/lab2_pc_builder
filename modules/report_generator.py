def generate_report(build):
    if not build:
        return "Сборка пуста"
    
    report = "Конфигурация ПК:\n"
    for component, name in build.items():
        report += f"- {component}: {name}\n"
    return report