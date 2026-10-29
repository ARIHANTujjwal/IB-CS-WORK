
import os
from datetime import datetime

valid_lines = 0
successful_requests = 0
error_requests = 0
total_time = 0


server_totals = {}
server_counts = {}

try:
 
    with open("data/server_logs.csv", "r") as file:
        line_number = 0

        for line in file:
            line_number = line_number + 1

            if line_number == 1:
                continue 
          
            line = line.strip()
            parts = line.split(",")

           
            while len(parts) > 4 and parts[-1].strip() == "":
                parts.pop()

            if len(parts) != 4:
                print("Warning on line", line_number, ": Wrong number of fields.")
                continue

            server_id = parts[1].strip()

            if server_id == "":
                print("Warning on line", line_number, ": Missing server ID.")
                continue

           
            try:
                response_time = float(parts[2])
                status_code = int(parts[3])
            except ValueError:
                print("Warning on line", line_number, ": Invalid number.")
                continue

           
            if response_time < 0 or str(response_time) in ["nan", "inf", "-inf"]:
                print("Warning on line", line_number, ": Invalid response time.")
                continue

            if status_code < 100 or status_code > 599:
                print("Warning on line", line_number, ": Invalid status code.")
                continue

            valid_lines = valid_lines + 1
            total_time = total_time + response_time

            if status_code == 200:
                successful_requests = successful_requests + 1

            if status_code >= 400:
                error_requests = error_requests + 1

            if server_id not in server_totals:
                server_totals[server_id] = 0
                server_counts[server_id] = 0

            server_totals[server_id] = server_totals[server_id] + response_time
            server_counts[server_id] = server_counts[server_id] + 1

    if valid_lines > 0:
        average = total_time / valid_lines
        average_text = str(round(average, 2)) + " ms"
    else:
        average = 0
        average_text = "N/A (no valid records)"

 
    LATENCY_THRESHOLD = average

    os.makedirs("reports", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

   
    with open("reports/summary_report.txt", "w") as report:
        report.write("CLOUD SERVER LOG ANALYSIS REPORT\n")
        report.write("Valid records: " + str(valid_lines) + "\n")
        report.write("Successful requests (200): " + str(successful_requests) + "\n")
        report.write("Error responses (400 or above): " + str(error_requests) + "\n")
        report.write("Overall average: " + average_text + "\n")

   
    with open("reports/summary_report.txt", "a") as report:
        report.write("\nPer-server latency breakdown\n")

        for server_id in server_totals:
            count = server_counts[server_id]
            server_average = server_totals[server_id] / count
            report.write(server_id + ": " + str(count) + " requests, ")
            report.write("average " + str(round(server_average, 2)) + " ms\n")

        report.write("\nLatency alerts\n")
        report.write("Threshold (overall average): " + average_text + "\n")
        alert_found = False

        for server_id in server_totals:
            server_average = server_totals[server_id] / server_counts[server_id]

            if server_average > LATENCY_THRESHOLD:
                report.write("ALERT: " + server_id + " averages ")
                report.write(str(round(server_average, 2)) + " ms\n")
                alert_found = True

        if valid_lines == 0:
            report.write("No valid records to check.\n")
        elif alert_found == False:
            report.write("No servers exceeded the threshold.\n")

  
    if os.path.exists("logs/audit.log"):
        if os.path.getsize("logs/audit.log") > 2048:
          
            archive_time = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            archive_name = "logs/audit_archive_" + archive_time + ".log"
            os.rename("logs/audit.log", archive_name)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/audit.log", "a") as audit:
        audit.write("[" + timestamp + "] SUCCESS: ")
        audit.write("Processed " + str(valid_lines) + " logs. ")
        audit.write("Average: " + average_text + "\n")

    print("Finished. Check reports/summary_report.txt and logs/audit.log.")


except FileNotFoundError:
    print("File or folder missing. Check that data/server_logs.csv exists.")
except PermissionError:
    print("Access denied. Check your file and folder permissions.")
except IOError:
    print("A file could not be read, written, or renamed.")
finally:
    print("Process attempt finished.")


