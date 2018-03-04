# PhysiologicalDataStudiesMBand
Physiological signals recorded with a Microsoft Band 2 are processed and modeled with a basic bayesian model.

Here I will explain the method to access to the raw data from the band since I think it's what most people could be interested on.

# Raw Data recording with Microsoft Band
Microsoft Band don't let you get the real time raw data in a straightforward way but with a couple of apps it is easy to get a method for real time data streaming from the sensors.
Since the band is synchronized with the phone, the easiest way to get the raw data was to use an app, what I used is called BandCompanion, it is free and works pretty fine.
To access to the data in real time from your computer I download SSHelper app which allows you to access your phone through SSH. In particular you can use sshfs to mount the file system of your phone into your computer.

## Prerequisites
    * SSHelper
    * BandCompanion

## Instructions
    1. Connect your phone to your computer through usb and activate bluetooth.
    2. Share connection with your phone to your computer to be in the same network and ensure fast data transmission.
    3. Synch your Band with your phone
	4. Open SSHelper and BandCompanion
	5. Search for your phone IP in your computer
		5.a ifconfig
		5.b sudo nmap -sO 192.168.XX.1/24

	6. Mount your phone data into some folder, e.g. "./band"
        sudo sshfs -p 2222 admin@192.168.XX.YYY:/data/data/com.arachnoid.sshelper/home/SDCard/CompanionForBand ./band

    Thats it, you should be able to access the data
    
	At the end to disconnect your phone file system from your computer with: umount ./band
