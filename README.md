<div align="center">
<img src="https://raw.githubusercontent.com/Morfeu5z/Trashpanda-Cloud/version/static/pic/trashpanda.PNG">
<a href="https://hub.docker.com/r/risernx/trashpanda">Link to docker repo with server | </a>
<a href="http://trashpanda.pwsz.nysa.pl">| Link to Trashpanda Cloud</a>
</div>

### Few words about
<div align="justify">
<p>Trashpanda was created as school project in 2018, by students of the 3rd year of Computer Science.
<p>The main idea was to set our own server and create a cloud with data from many users. Log in is possible via Google accounts. All files are authomatically set as public, unless user change it manually to private.
<p>When the new file is added, application search through already existing files and compares them with new one by using hash sum. When it finds 2 identical, instead of adding new file, it creates new path to alredy existing one.
<p>When user wants to delete a file, it comes to bin. It will be deleted after cleaning the bin, unless other users use this file. In that situation path between the file and user that wants to delete it will be destroyed, but file and its other connections will remain untouched.
<p>Application also allows to update files, therefore the previous version will be saved as old and new one will become current. It makes possible to restore previous versions. In a meantime, server searches through database and removes old files, not used and without connection with any user.
</div>

### Technology & Languages
>* Python
>* JS
>* HTML
>* CSS
>* Flask
>* Docker
>* MySQL

### Team
>>* __Front-end:__
>* Aleksander Sinkowski
>* Aleksandra Pawlaczyk
>* Marcin Ochociński
>>* __Back-end:__
>* Serhii Riznychuk
>* Mikołaj Rychel
