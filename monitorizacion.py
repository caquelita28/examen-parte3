import psutil

# Obtener información del CPU
uso_cpu = psutil.cpu_percent(interval=1)  # Intervalo de 1 segundo
print(f"Uso de CPU es: {uso_cpu}%")
