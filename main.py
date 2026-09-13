import data_collector
import system_health

system_info = data_collector.collect_system_info()
system_usage = data_collector.collect_system_usage()


print("===== SYSTEM HEALTH REPORT ======\n")

print(f"Uptime : {data_collector.get_uptime()}")

for name, value in system_info.items():
    print(f"{name}:    {value}")

print()

for name, value in system_usage.items():
    print(f"{name}:     {value}%   - {system_health.check_health(value)}")
