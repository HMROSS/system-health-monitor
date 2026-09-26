
import system_health
import data_collector


system_info = data_collector.collect_system_info()
system_usage = data_collector.collect_system_usage()


def build_report():

    report = ""

    report += "===== SYSTEM HEALTH REPORT ======\n\n"

    report += (f"{'Generated:':<20} {data_collector.get_timestamp()}\n")

    report += (f"\n")

    for name, value in system_info.items():
        report += (f"{name + ':':<20} {value}\n")

    report += (f"{'Uptime:':<20} {data_collector.get_uptime()}\n")

    report += (f"\n")

    for name, value in system_usage.items():
        if value is None:
            display_value = "N/A"
        else:
            display_value = str(value) + "%"

        report += (f"{name +':':<10} {display_value:<10}   - {system_health.check_health(value):>10}\n")

    return report
