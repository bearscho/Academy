ThreadGroup 설정 안내  

실습 자료 중 아래와 같은 ThreadGroup를 설정하는 부분이 있는데, 설명이 부족한 것 같아 추가 설정 관련 공유 드립니다.  
. 1분마다 5명 중가  
. 최대 10명 유입  
. 측정 시간 : 10분  

위와 같은 조건은 JMeter 기본 ThreadGroup 사용하여 적용하기에는 어려운 부분입니다.  

이번 교재 업데이트 시 플러그인 사용 방식에서 기본 ThreadGroup으로 바꾸었는데,  
실습엑셀 문서에까지는 반영을 못하였고, 아래와 같은 부하유입 조건으로 바꾸어야 할 것 같습니다.  
### => 2분 동안 최대 10명까지 유입 , 측정시간 : 10분

사용하는 방법은 아래와 같습니다.  
. 최대 10명 유입 : Target Concurrency 에 10 입력(10명)
. 1분마다 5명 증가 : Ramp Up Time(min) 에 2입력 , Ramp-Up Steps Count 에 2입력
                    1분에 5명씩 유입 시 
아래는 기본 ThreadGroup을 이용하는 방법이며
- 최대 10명 유입 : Number of Threads(users) 에 10 입력  
- 2분 동안 유입 : Ramp-Up Period(in seconds) 에 120 (초) 입력
- 측정시간 10분 : Scheduler 체크 후 Duration(seconds) 에 600 (초) 입력
<img src="https://github.com/bearscho/academy/blob/master/TTA%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8/2019%EB%85%843%EC%9B%94/ThreadGroup%EC%84%A4%EC%A0%95/1.threadgroup.PNG?raw=true">

그번 강의부터는 Plugins을 사용하지 않고 기본 ThreadGroup를 사용하는 것으로 바꾸어서 설명을 안드렸으나,  
bzm - Curruncy Thread Group 이라는 플러그인을 사용하면 보다 쉽제 확인이 가능합니다. 
- 최대 10명 유입 : Target Concurrentcy 에 10 입력  
- 2분 동안 유입 : Ramp-Up Time(in) 에 2 (분) 입력
- Ramp-Up Steps Count 에는 10명을 몇단계로 나누어 유입할지를 지정하여, 2로 입력 시 10명을 2단계(5명,5명씩)으로 유입됩니다.
                      10으로 입력시에는 10명을 1명씩 순차적으로 유입됩니다.
- 측정시간 10분 : HoldTarget Rate Time(min) 에 10 (분) 입력
해당 플러그인에서는 값을 변경시마다 어떻게 유입되는지를 그래프로 확인가능합니다.
<img src=https://github.com/bearscho/academy/blob/master/TTA%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8/2019%EB%85%843%EC%9B%94/ThreadGroup%EC%84%A4%EC%A0%95/2.concurrencythreadgroup.PNG?raw=true">


  
