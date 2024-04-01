# Exemple de proiecte FreeStyle si Pipeline-uri Jenkins folosite la cursul de SCC (Sisteme Cloud si Containerizare)

## Cuprins

1. [Instalare Jenkins](#instalare-jenkins)



## Instalare Jenkins
Exista mai multe tutoriale cu diverse optiuni de instalare.
Recomand utilizarea documentatiei de pe site-ul: https://jenkins.io, mentiunut si actualizat de comunitatea Jenkins.
Unele versiuni de tutoriale pot fi vechi si nu mai gasiti fie site-ul fie pasii descrisi in documentatie sau in inregistrarea video.


### Pregatire Ubuntu. Actualizare de executat comenzile:

    sudo su -
    apt update
    apt upgrade


### Instalare Java Open JDK: 
Urmati pasii din ghidul de instalare online:
https://www.jenkins.io/doc/book/installing/linux/#installation-of-java

    Verificare instalare Java:
    
    java --version

    Daca Java s-a instalat, ar trebui afisata versiunea de Open JDK instalata.
    Verificati in pagina web de instalare varianta actualizata a raspunsului asteptat.
    Este posibil sa gasiti o versiune mai noua de Java decat cea de pe site, de ex, in loc de 
    "openjdk version 17.0.8" sa fie "openjdk version 17.0.10".
    Nu ar trebui sa fie probleme cat timp avem aceeasi versiune majora '17' de Java.

### Instalare Jenkins: 
Urmati pasii din ghidul de instalare online:
https://www.jenkins.io/doc/book/installing/linux/

Jenkins este instalat ca serviciu. Se poate verifica ca ruleaza cu comanda:

    ps aux | grep jenkins

    Ar trebui primit un raspuns de genul:
    cip@ubuntu2:~$ ps aux | grep jenkins
    jenkins      655 13.3  5.7 3139948 228220 ?      Ssl  14:05   0:14 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=/var/cache/jenkins/war --httpPort=8080

Poate fi folosit si ca serviciu sau se poate opri serviciu si se poate rula dintr-un terminal.
Verificare rulare Jenkins ca serviciu:

    $ systemctl status jenkins
    ● jenkins.service - Jenkins Continuous Integration Server
         Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; vendor preset: enabled)
         Active: active (running) since Mon 2024-04-01 14:06:38 EEST; 5min ago
       Main PID: 655 (java)
          Tasks: 39 (limit: 4599)
         Memory: 286.7M
            CPU: 15.548s
         CGroup: /system.slice/jenkins.service
                 └─655 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=/var/cache/jenkins/war --httpPor>
    
    apr 01 14:06:15 ubuntu2 jenkins[655]: Jenkins initial setup is required. An admin user has been created and a password generated.
    apr 01 14:06:15 ubuntu2 jenkins[655]: Please use the following password to proceed to installation:
    apr 01 14:06:15 ubuntu2 jenkins[655]: bb18df0d3a7a498ca4d92489d526f3d0
    apr 01 14:06:15 ubuntu2 jenkins[655]: This may also be found at: /var/lib/jenkins/secrets/initialAdminPassword
    apr 01 14:06:15 ubuntu2 jenkins[655]: *************************************************************
    apr 01 14:06:15 ubuntu2 jenkins[655]: *************************************************************
    apr 01 14:06:15 ubuntu2 jenkins[655]: *************************************************************
    apr 01 14:06:38 ubuntu2 jenkins[655]: 2024-04-01 11:06:38.696+0000 [id=31]        INFO        jenkins.InitReactorRunner$1#onAttained:>
    apr 01 14:06:38 ubuntu2 jenkins[655]: 2024-04-01 11:06:38.726+0000 [id=24]        INFO        hudson.lifecycle.Lifecycle#onReady: Jen>
    apr 01 14:06:38 ubuntu2 systemd[1]: Started Jenkins Continuous Integration Server.

    systemctl is

Oprire si dezactivare serviciu Jenkins:

    

    sudo systemctl stop jenkins
    sudo systemctl disable jenkins

    #Verificarifdf
    1)
    $ systemctl is-active jenkins
    inactive

    2) 
    $ ps aux | grep jenkins
    # ne asteptam sa nu gasi nici un proces Jenkins

    3) 
    $ systemctl status jenkins
    ○ jenkins.service - Jenkins Continuous Integration Server
         Loaded: loaded (/lib/systemd/system/jenkins.service; disabled; vendor preset: enabled)
         Active: inactive (dead)
    
    apr 01 14:15:27 ubuntu2 jenkins[655]: 2024-04-01 11:15:27.513+0000 [id=26]        INFO        jenkins.model.Jenkins$16#onAttained: Co>
    apr 01 14:15:27 ubuntu2 jenkins[655]: 2024-04-01 11:15:27.514+0000 [id=26]        INFO        jenkins.model.Jenkins#_cleanUpDisconnec>
    apr 01 14:15:27 ubuntu2 jenkins[655]: 2024-04-01 11:15:27.520+0000 [id=26]        INFO        jenkins.model.Jenkins#_cleanUpShutdownP>
    apr 01 14:15:27 ubuntu2 jenkins[655]: 2024-04-01 11:15:27.520+0000 [id=26]        INFO        jenkins.model.Jenkins#_cleanUpPersistQu>
    apr 01 14:15:27 ubuntu2 jenkins[655]: 2024-04-01 11:15:27.526+0000 [id=26]        INFO        jenkins.model.Jenkins#_cleanUpAwaitDisc>
    apr 01 14:15:27 ubuntu2 jenkins[655]: 2024-04-01 11:15:27.526+0000 [id=26]        INFO        hudson.lifecycle.Lifecycle#onStatusUpda>
    apr 01 14:15:27 ubuntu2 jenkins[655]: 2024-04-01 11:15:27.528+0000 [id=26]        INFO        o.e.j.s.handler.ContextHandler#doStop: >
    apr 01 14:15:27 ubuntu2 systemd[1]: jenkins.service: Deactivated successfully.
    apr 01 14:15:27 ubuntu2 systemd[1]: Stopped Jenkins Continuous Integration Server.
    apr 01 14:15:27 ubuntu2 systemd[1]: jenkins.service: Consumed 16.032s CPU time.

Pentru invatare, recomand rularea Jenkins de catre utilizatorul curent din terminal. Dupa oprirea serviciului Jenkins, deschideti o consola si tastati
      
    $ jenkins

    La prima rulare, ar trebui sa apara un mesaj similar cu cel de mai jos:

    Running from: /usr/share/java/jenkins.war
    webroot: /home/cip/.jenkins/war
    2024-04-01 11:23:06.207+0000 [id=1]	INFO	winstone.Logger#logInternal: Beginning extraction from war file
    2024-04-01 11:23:06.356+0000 [id=1]	WARNING	o.e.j.s.handler.ContextHandler#setContextPath: Empty contextPath
    2024-04-01 11:23:06.434+0000 [id=1]	INFO	org.eclipse.jetty.server.Server#doStart: jetty-10.0.20; built: 2024-01-29T20:46:45.278Z; git: 3a745c71c23682146f262b99f4ddc4c1bc41630c; jvm 17.0.10+7-Ubuntu-122.04.1
    2024-04-01 11:23:06.824+0000 [id=1]	INFO	o.e.j.w.StandardDescriptorProcessor#visitServlet: NO JSP Support for /, did not find org.eclipse.jetty.jsp.JettyJspServlet
    2024-04-01 11:23:06.915+0000 [id=1]	INFO	o.e.j.s.s.DefaultSessionIdManager#doStart: Session workerName=node0
    2024-04-01 11:23:07.669+0000 [id=1]	INFO	hudson.WebAppMain#contextInitialized: Jenkins home directory: /home/cip/.jenkins found at: $user.home/.jenkins
    2024-04-01 11:23:07.849+0000 [id=1]	INFO	o.e.j.s.handler.ContextHandler#doStart: Started w.@3c8bdd5b{Jenkins v2.451,/,file:///home/cip/.jenkins/war/,AVAILABLE}{/home/cip/.jenkins/war}
    2024-04-01 11:23:07.887+0000 [id=1]	INFO	o.e.j.server.AbstractConnector#doStart: Started ServerConnector@5d740a0f{HTTP/1.1, (http/1.1)}{0.0.0.0:8080}
    2024-04-01 11:23:07.911+0000 [id=1]	INFO	org.eclipse.jetty.server.Server#doStart: Started Server@1d76aeea{STARTING}[10.0.20,sto=0] @2267ms
    2024-04-01 11:23:07.918+0000 [id=25]	INFO	winstone.Logger#logInternal: Winstone Servlet Engine running: controlPort=disabled
    2024-04-01 11:23:08.288+0000 [id=31]	INFO	jenkins.InitReactorRunner$1#onAttained: Started initialization
    2024-04-01 11:23:08.389+0000 [id=31]	INFO	jenkins.InitReactorRunner$1#onAttained: Listed all plugins
    2024-04-01 11:23:09.395+0000 [id=31]	INFO	jenkins.InitReactorRunner$1#onAttained: Prepared all plugins
    2024-04-01 11:23:09.398+0000 [id=30]	INFO	jenkins.InitReactorRunner$1#onAttained: Started all plugins
    2024-04-01 11:23:09.463+0000 [id=30]	INFO	jenkins.InitReactorRunner$1#onAttained: Augmented all extensions
    2024-04-01 11:23:09.991+0000 [id=30]	INFO	jenkins.InitReactorRunner$1#onAttained: System config loaded
    2024-04-01 11:23:09.991+0000 [id=30]	INFO	jenkins.InitReactorRunner$1#onAttained: System config adapted
    2024-04-01 11:23:09.991+0000 [id=30]	INFO	jenkins.InitReactorRunner$1#onAttained: Loaded all jobs
    2024-04-01 11:23:09.993+0000 [id=30]	INFO	jenkins.InitReactorRunner$1#onAttained: Configuration for all jobs updated
    2024-04-01 11:23:10.136+0000 [id=31]	INFO	jenkins.install.SetupWizard#init: 
    
    *************************************************************
    *************************************************************
    *************************************************************
    
    Jenkins initial setup is required. An admin user has been created and a password generated.
    Please use the following password to proceed to installation:
    
    7705z9add9y7439xb508fa32196237c1                                             <---------- PAROLA INITIALA DE ADMIN
    
    This may also be found at: /home/cip/.jenkins/secrets/initialAdminPassword   <---------- FISIER CU PAROLA INITIALA DE ADMIN
    
    *************************************************************
    *************************************************************
    *************************************************************
    
    2024-04-01 11:23:10.476+0000 [id=45]	INFO	hudson.util.Retrier#start: Attempt #1 to do the action check updates server
    2024-04-01 11:23:33.331+0000 [id=30]	INFO	jenkins.InitReactorRunner$1#onAttained: Completed initialization
    2024-04-01 11:23:33.360+0000 [id=24]	INFO	hudson.lifecycle.Lifecycle#onReady: Jenkins is fully up and running
    2024-04-01 11:23:34.985+0000 [id=45]	INFO	h.m.DownloadService$Downloadable#load: Obtained the updated data file for hudson.tasks.Maven.MavenInstaller
    2024-04-01 11:23:34.986+0000 [id=45]	INFO	hudson.util.Retrier#start: Performed the action check updates server successfully at the attempt #1



#### !!! De observat parola de admin generata la prima rulare in mesajul de mai sus.
####     Daca parola nu apare in mesaj, poate fi gasita in fisierul indicat in mesajul de mai sus.

Oprirea serviciului Jenkins se poate face cu `Ctrl-C` din consola unde a fost pornit

### Jenkins isi va face un director local ~/.jenkins
Aici vom regasi directoare si fisiere aferente proiectelor si pipeline-urilor folosite.


## Acces server Jenkins din browseer, dupa instalare si pornire din terminal

* Se solicita parola de administrator. Trebuie introdusa parola afisate in terminal la pornire sau daca nu se afiseaza, trebuie luata parola din fisierul mentionat in mesajul de mai sus

![image](https://github.com/crchende/jenkinsdemo/assets/57460107/149ec74a-6e4b-4e37-91a1-afd265058bea)





