## 아래 메시지가 나오며, 종료가 되지 않을 경우    

The JVM should have exited but did not.  
The following non-daemon threads are still running (DestroyJavaVM is OK):  
Thread[AWT-EventQueue-0,6,main], stackTrace:sun.misc.Unsafe#park  
java.util.concurrent.locks.LockSupport#park  
java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject#await  
java.awt.EventQueue#getNextEvent  
java.awt.EventDispatchThread#pumpOneEventForFilters  
java.awt.EventDispatchThread#pumpEventsForFilter  
java.awt.EventDispatchThread#pumpEventsForHierarchy  
java.awt.EventDispatchThread#pumpEvents  
java.awt.EventDispatchThread#pumpEvents  
java.awt.EventDispatchThread#run  
  
Thread[DestroyJavaVM,5,main], stackTrace:  
Thread[AWT-Shutdown,5,system], stackTrace:java.lang.Object#wait  
sun.awt.AWTAutoShutdown#run  
java.lang.Thread#run  
  
  
## -Jjmeterengine.force.system.exit=true  실행 옵션에 추가



You can add -Jjmeterengine.force.system.exit=true on the command line when launching JMeter, or add jmeterengine.force.system.exit=true to JMETER_HOME/bin/jmeter.properties.


https://stackoverflow.com/questions/52987152/the-jvm-should-have-exited-but-did-not
