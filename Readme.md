Hello

This is a script which can run and help you find a vaccine slot.
It has a timer sleep for 5 mins and every 5 mins it checks for the availability.

### Instructions

* You need to have python3 installed.
* Make sure you've argsparse and requests module installed.
* Command to install argspars and requests
    * pip3 install argparse
    * pip3 install requests
    
* To run you need to enter the pin code and date availabilty
    * Ex:- python3 main.py -p 110005 -d 15-05-2021
    
* In case it finds a slot it will show you the details
* In case it doesn't find it will show you No Slots found and will keep checking every 5 mins.
 