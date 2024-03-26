import numpy as np
import ssl, socket
import csv
from datetime import datetime

## 현재 시간을 반환해주는 함수 ##
def cur_time():
    time = datetime.now()
    time_s = "[%s:%s:%s]" % (time.hour, time.minute, time.second)
    return time_s

## HTTPS 연결 요청 함수 ##
def https_connect(url):
    ctx = ssl.create_default_context()
    s = ctx.wrap_socket(socket.socket(), server_hostname=url)
    s.connect((url, 443))
    return s

# 소켓 연결 제한 시간 설정
socket.setdefaulttimeout(2)

print(cur_time(), "Program start..!")

# 읽어올 URL 출발/종료 지점 지정
src = 0
dst = 120000

urldata = np.genfromtxt("normal1.csv", delimiter=',', dtype="|U")
urllist = urldata[src:dst]
print(cur_time(), "URL loading complete..!")

scheme_s = "https://"

convert_url = []
failed_url = []
failed_url_err = []
index = src
suc_count = 0
failed_count = 0
for url in urllist:
    print(cur_time(), "[%d/%d] " % (index + 1, dst), end='')
    index += 1
    try:
        https_connect(url)
        url = scheme_s + url
        convert_url.append(url)
        suc_count += 1
        print(url, "-> conversion succeed!!")
    except Exception as e:
        failed_url.append(url)
        failed_url_err.append(e)
        print(url, "-> conversion failed..")
        failed_count += 1
        pass

print(cur_time(), "Convert complete..!")

# 변환 성공한 URL들을 CSV 파일 형식으로 저장
f = open("normal_convert.csv", 'a', encoding="UTF-8", newline="")
csv_wr = csv.writer(f)
for i in range(len(convert_url)):
    csv_wr.writerow([convert_url[i]])

print(cur_time(), "Create normal_convert.csv file complete..!")
f.close()

# 변환에 실패한 URL들을 CSV 파일 형식으로 저장
f = open("normal_failed.csv", 'a', encoding="euc_kr", newline="")
csv_wr = csv.writer(f)
for i in range(len(failed_url)):
    csv_wr.writerow([failed_url[i], failed_url_err[i]])

print(cur_time(), "Create normal_failed.csv file complete..!")
print(cur_time(), "result : total = %d / success = %d / fail = %d" % (dst - src, suc_count, failed_count))

f.close()
