# 탐지 방법
공유기에 들어가는 탐지 시스템의 탐지 방법에 대한 정리


## 목차
1. ARP-Spoofing
2. Port-Scan
3. OS-Scan
4. UDP-Flooding
5. ACK-Flooding
6. HTTP-Flooding
7. Host-bruteforce
8. URL-Phishing


## 1. ARP-Spoofing

- ### ARP Spoofing 증상
   1. 네트워크 속도 저하
   2. 정기적인 ARP 패킷 다량 수신
   3. 악성 코드가 웹 페이지 시작 부분에 위치
   
- ### 탐지 방법
   1. ARP Table 모니터링 - 중복된 MAC 주소나 빈번한 MAC주소 변경을 감지
   2. ARP 패킷 검사 - 불필요한 ARP 패킷을 탐지
   3. ARP 캐시 모니터링 - ARP캐시에 있는 엔트리들의 변경이나 중복된 MAC주소 엔트리를 감지


## 2. Port-Scan

**포트 스캔(port scan)** 은 운영 중인 서버에서 열려있는 TCP/UDP 포트를 검색하는 것을 의미하며,  
다른 말로는 해당 네트워크를 돌면서 살아있는 호스트, 포트를 찾는 것을 의미하는 **Sweep**이라 불리기도 한다.

- ### Port-Scan 증상
   1. 네트워크 성능 저하가 발생할 수 있음 (네트워크 트래픽의 이상한 증가)
   2. 로그 확대 - 대량의 접근 시도를 기록하여 로그 파일의 크기가 커진다.
   3. 서비스 거부 현상 발생 (Denial of Service, DoS)
   4. 대상 시스템의 CPU 및 메모리 리소스의 이상한 사용량 (포트 스캔이 진행되면서 리소스 과도 사용 포착 가능) 
   
- ### 탐지 방법
   1. Honeypots - 가짜 포트를 제공하여 공격자를 유인
   2. Intrusion Detection Systems(IDS) - 네트워크 트래픽을 실시간으로 모니터링하여 포트 스캔과 같은 이상 활동 탐지

## 3. OS-Scan
**운영 체제 스캔(OS Scan)** 은 특정 호스트의 운영 체제를 식별하려는 공격 형태다.  
공격자가 대상 시스템에 대해 추가 정보를 수집하여 취약점을 찾고, 특정 운영 체제 특화 공격을  
하기 위해 사용된다.


## 4. UDP-Flooding

## 5. ACK-Flooding

## 6. HTTP-Flooding

## 7. Host-bruteforce

## 8. URL-Phishing