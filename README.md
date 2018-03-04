# Physiological Data with Microsoft Band
In this project Physiological signals recorded with a Microsoft Band 2 are processed and modeled with a basic bayesian model.

The bayesian model and its explanation and results (It's in spanish) are in the jupyter notebook, I used the *pymc* library. The model is inspired in some examples from the book [Bayesian Inference for Hacker](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers).

# Raw Data recording with Microsoft Band
I will explain the method to access to the raw data from the band since It's something that took me some time to figure out and I think some people could find it useful.

Microsoft Band don't let you get the real time raw data in a straightforward way but with a couple of apps it is easy to get a method for real time data streaming from the sensors.
Since the band is synchronized with the phone, the easiest way to get the raw data was to use an app, what I used is called BandCompanion, it is free and works pretty fine.
To access to the data in real time from your computer I download SSHelper app which allows you to access your phone through SSH. In particular you can use sshfs to mount the file system of your phone into your computer.

## Prerequisites
### Phone
- SSHelper
- BandCompanion
### Computer
- sshfs
- nmap

## Instructions
1. Connect your phone to your computer through usb and activate bluetooth.
2. Share connection with your phone to your computer to be in the same network and ensure fast data transmission.
3. Synch your Band with your phone
4. Open SSHelper and BandCompanion. You should be able to see your physiological data in BandCompanion

5. Find out your phone IP in your computer
	5.a `ifconfig`
	5.b `sudo nmap -sO 192.168.XX.1/24`

6. Mount your phone data into some folder, e.g. "./band", complete the XX.YYY with the your phone IP
    ```sudo sshfs -p 2222 admin@192.168.XX.YYY:/data/data/com.arachnoid.sshelper/home/SDCard/CompanionForBand ./band```

That's it, you should be able to access the data, `band.py` is a python script to print the beats per minute (BPM), galvanic skin response (GSR) and body temperature.

At the end to disconnect your phone file system from your computer with: `umount ./band`
