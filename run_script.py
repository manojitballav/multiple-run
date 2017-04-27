#This program run all the other programs in a serial manner

import os

print "Starting to scrape all the Positive Reviews of TP-Link Router"
os.system("python scraper1.py")
print "Successfully scraper all the Positive Reviews of TP-Link Router"

print "Starting to scrape all the Critical Reviews of TP-Link Router"
os.system("python scraper2.py")
print "Successfully scraper all the Critical Reviews of TP-Link Router"

print "Starting to scrape all the Positive Reviews of D-Link Router"
os.system("python scraper3.py")
print "Successfully scraper all the Positive Reviews of D-Link Router"

print "Starting to scrape all the Critical Reviews of D-Link Router"
os.system("python scraper4.py")
print "Successfully scraper all the Critical Reviews of D-Link Router"