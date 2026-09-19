import report_builder


final_report = report_builder.build_report()

print(final_report)

with open("system_health_report.txt", "w") as file:
    file.write(final_report)
