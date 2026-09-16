import data_collector
import system_health

system_info = data_collector.collect_system_info()
system_usage = data_collector.collect_system_usage()


print("===== SYSTEM HEALTH REPORT ======\n")


for name, value in system_info.items():
    print(f"{name + ':':<20} {value}")

print(f"{'Uptime:':<20} {data_collector.get_uptime()}")

print()

for name, value in system_usage.items():
    print(f"{name +':':<10} {str(value) +'%':<10}   - {system_health.check_health(value):>10}")
