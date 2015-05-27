import RPi.GPIO as GPIO
from flask import Flask, jsonify, render_template, request
import spidev
import time
import os
import threading
import sched
import json
history = []

OUTPUT_PORT=8030
sleeptime = 3.0
GPIO.setmode(GPIO.BOARD)
ControlPin = [26]
for pin in ControlPin:
	print 'setting pin: ', pin
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

app= Flask(__name__)

@app.route("/")
def hello():
  jsonify({"message":"use /lamp/value "})

@app.route("/lamp/<int:newValue>")
def setLamp(newValue):
  if newValue:
    print ' setting lamp on' 
  else:
    print ' turning lamp off'  
  GPIO.output(ControlPin[0],newValue)
  return "thank you" 



if __name__=="__main__":
  app.run(host='0.0.0.0',port=OUTPUT_PORT,debug=True)

