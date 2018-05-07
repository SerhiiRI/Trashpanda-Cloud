# Comenda montowania kontenera na serveru 

 sudo docker run -it -p 80:5000 -v /var/log/trashpanda:/var/log/trashpanda:Z risernx/trashpanda
 
 ```:Z``` - dotyczy SELinux
