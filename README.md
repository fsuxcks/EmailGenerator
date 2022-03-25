# Email Generator
## Generates up to 500 email accounts per session. Fast and Easy.
### How it works
Simply its just sends request to email generating web site, drags email and does it up to 500 times with up to 8 threads. Emails are fake, so you cant use it in good services like Instagram or Facebook. And you cant get mails also. Check the **screens**.
***
### Dependencies:
+ Python 3.X
+ Requets 2.27.1
+ BeautifulSoup 4.10.0
+ Progress 1.6
+ **Works only on Windows.**
***
### Instalation
> git clone https://github.com/fsuxcks/EmailGenerator
> 
> cd EmailGenerator
> 
> pip install -r requirements.txt
>
>python emailgenerator.py
***
### Features
1. Fast and Easy
2. Up to 500 emails per session
3. Up to 8 Threads
4. Generates 500 emails in 1 minute
***
### Work to do:
+ Change GUI (**NOT DONE**)
+ Save to TXT file (**NOT DONE**)
***
## Updates
### Version 2.3
+ Port to Linux
+ Parser: lxml -> html.parser
+ Delays change
+ Threads more than amount of emails bug fix
+ Added requirements.txt
+ Other bugs

### Version 2.2
+ Improved progress bar
+ Script testings for server durability
+ Limit of threads: 7 -> 8
+ Speed: 500 emails / 1 minute

### Version 2.1
+ Fixed import bug

### Version 2.0
+ Added Threads -> 7
+ Limit of emails: 100 -> 500
+ Added progress bar
+ Fixed a lot of bugs
+ At the end, script checks if all threads are finished and then shows all emails


