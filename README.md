# CUDA, cuDNN, FFmpeg, Gstreamer compiled OpenCV 4.5.0
# Installation on Jetson Nano

### Initial Step
Keep the system up-to-date
```sh
$ sudo apt-get update
$ sudo apt-get upgrade
```
Since OpenCV 4.5.0 installation on Jetson Nano eats above 4+ GB RAM, we need to install the dphys-swapfile that will create extra RAM temporarily
```sh
$ sudo apt-get install dphys-swapfile
```
Open up /etc/dphys-swapfile
```sh
$ sudo gedit /etc/dphys-swapfile
```
and do the following changes
![alt text](https://github.com/scriptbiggie/jetson-nano/blob/main/image.png?raw=true)
After saving, be sure that an extra space is created 
![alt text](https://github.com/scriptbiggie/jetson-nano/blob/main/image1.png?raw=true)
Reboot afterwards
```sh
$ sudo reboot
```
### Next Step

If so far so good, issue opencv_4.3.0_install.sh that will automatically 
  - Install all the necessary dependencies,
  - download OpenCV 4.5.0, 
  - build and compile it, 
  - removing dphys-swapfile after the finalization of the compilation

Keep in mind that the whole process is gonna be 2+ hours of long.
WARNING: Please refer to opencv_4.3.0_install.sh in the case of some errors, e.g. compilation related "dependency errors"

### The Limbo Step
If the execution of opencv_4.3.0_install.sh completed smoothly, issue 
```sh
$ python3 opencv_check.py
```
and see if OpenCV 4.5.0 has been installed with CUDA, cuDNN, FFmpeg and Gstreamer.

### Last Step
Since all the necessary steps are already done, you may want to delete the redundant OpenCV files. To do that, issue
```sh
$ sudo rm -rf ~/opencv
$ sudo rm -rf ~/opencv_contrib
```

