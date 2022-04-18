# Raspberry Pi Web Bookshelf
Raspberry Pi Bookshelf for the Web

This project aims to get the Rasberry Pi Bookshelf available through a webpage.

The newer versions of Raspberry Pi OS comes with a **Bookshelf** (https://github.com/raspberrypi-ui/bookshelf) application, which is nice, but has some downsides:

 - Need to compile it yourself if you switch to a distro that does not include the application
 - Cannot be used from mobile phones or computers running other operating systems

This project is being hosted by myself and can be accessed at https://bookshelf.brunojesus.pt

## How to run it yourself
This site is available as a docker image at DockerHub at [brunofjesus/rpi-web-bookshelf](https://hub.docker.com/r/brunofjesus/rpi-web-bookshelf).

You can also run it in you machine as long as you have Python 3.9 and PIP with the following commands:
```
pip install -r requirements.txt
python main.py
```
