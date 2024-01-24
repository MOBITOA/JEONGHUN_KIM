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

- ### Port-Scan 증상
   1. 네트워크 성능 저하가 발생할 수 있음
   2. 로그 확대 - 대량의 접근 시도를 기록하여 로그 파일의 크기가 커진다.
   
- ### 탐지 방법
   1. Honeypots - 가짜 포트를 제공하여 공격자를 유인
   2. 