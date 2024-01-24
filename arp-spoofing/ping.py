# import os
# import subprocess
# import sys
# import csv

# hostname ="127.0.0.1"
# targetips = ["192.168.0.104"]

# # Executing Command
# def run_cmd(cmd):
#     try:
#         output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
#         print(str(output))
#         return str(output)
#         #return subprocess.check_output(cmd, stderr=subprocess.STDOUT)
#     except subprocess.CalledProcessError as ex:
#         if ex.returncode == 255:
#             raise RuntimeWarning(ex.output.strip())
#         raise RuntimeError('cmd execution returned exit status %d:\n%s'
#                 % (ex.returncode, ex.output.strip()))

# def init_csv():
#     fname = "rtt_stats.csv"
#     writ = csv.writer(open(fname, 'a', buffering=1), delimiter=',')
#     header = ["src", "dst", "rtt",]
#     writ.writerow(header)
# init_csv()
# def update_csv(row):
#     fname = "rtt_stats.csv"
#     writ = csv.writer(open(fname, 'a', buffering=1), delimiter=',')
#     writ.writerow(row)

# def parse_latency(src, dst, result):
#     rttstr = 'rtt min/avg/max/mdev = '
#     lenrttstr = len(rttstr)
#     index = lenrttstr + result.find(rttstr)
#     rtt = result[index:]
#     result = rtt.split('/')[0]
#     update_csv([src,dst,result])

# for targetip in targetips:
# 	#cmd1 = 'ping -c 1 ' + targetip
# 	cmd1 = ['ping', '-n', '1', targetip]
# 	result = run_cmd(cmd1)
# 	#print("Pinging from hostname ", hostname)
# 	#print("result",result)
# 	parse_latency(hostname, targetip,result)



import os
import subprocess
import sys
import csv
import locale

hostname = "127.0.0.1"
targetips = ["192.168.0.104"]

default_encoding = locale.getpreferredencoding()

def run_cmd(cmd):
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        try:
            # Try decoding with UTF-8
            return output.decode('utf-8')
        except UnicodeDecodeError:
            # If UTF-8 decoding fails, use the system default encoding
            return output.decode(default_encoding, errors='replace')
    except subprocess.CalledProcessError as ex:
        if ex.returncode == 255:
            raise RuntimeWarning(ex.output.decode(default_encoding, errors='replace').strip())
        raise RuntimeError(f'cmd execution returned exit status {ex.returncode}:\n'
                           f'{ex.output.decode(default_encoding, errors="replace").strip()}')

def init_csv():
    fname = "rtt_stats.csv"
    writ = csv.writer(open(fname, 'w', newline=''), delimiter=',')
    header = ["src", "dst", "rtt"]
    writ.writerow(header)

def update_csv(row):
    fname = "rtt_stats.csv"
    with open(fname, 'a', newline='') as file:
        writ = csv.writer(file, delimiter=',')
        writ.writerow(row)

def parse_latency(src, dst, result):
    if "time=" in result:
        time_index = result.find("time=")
        rtt = result[time_index + 5:]
        rtt = rtt.split(" ")[0]
        update_csv([src, dst, rtt])
    else:
        print("No RTT data found in ping result")

init_csv()
for targetip in targetips:
    cmd1 = ['ping', '-n', '1', '-w', '500', targetip]
    result = run_cmd(cmd1)
    parse_latency(hostname, targetip, result)
