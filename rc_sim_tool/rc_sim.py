#!/usr/bin/env python
from __future__ import print_function
from math import radians
from time import sleep
from os import path, getenv
import sys
import time
import threading
import serial
import argparse

# if PAPARAZZI_SRC and PAPARAZZI_HOME not set, then assume the tree containing this
# file is a reasonable substitute
PPRZ_HOME = getenv("PAPARAZZI_HOME", path.normpath(path.join(path.dirname(path.abspath(__file__)), '../../../')))
PPRZ_SRC = getenv("PAPARAZZI_SRC", path.normpath(path.join(path.dirname(path.abspath(__file__)), '../../../')))
sys.path.append(PPRZ_SRC + "/sw/lib/python") # settings_xml
sys.path.append(PPRZ_HOME + "/var/lib/python") # pprzlink
sys.path.append(PPRZ_HOME + "/sw/ext/pprzlink") # pprzlink
from pprzlink.ivy import IvyMessagesInterface
from pprzlink.message import PprzMessage
from settings_xml_parse import PaparazziACSettings

class Guidance(object):
	def __init__(self, ac_id):
		self.ac_id = ac_id
		self._interface = None
		self.ap_mode = None
		try:
			settings = PaparazziACSettings(self.ac_id)
		except Exception as e:
			print(e)
			return
		try:
			self.ap_mode = settings.name_lookup['mode'] # try classic name
		except Exception as e:
			try:
				self.ap_mode = settings.name_lookup['ap'] # in case it is a generated autopilot
			except Exception as e:
				print(e)
				print("ap_mode setting not found, mode change not possible.")
		self._interface = IvyMessagesInterface("sim_rc_4ch")

	def shutdown(self):
		if self._interface is not None:
			print("Shutting down ivy interface...")
			self._interface.shutdown()
			self._interface = None

	def __del__(self):
		self.shutdown()

	def set_guided_mode(self):
		"""
		change mode to GUIDED.
		"""
		if self.ap_mode is not None:
			msg = PprzMessage("ground", "DL_SETTING")
			msg['ac_id'] = self.ac_id
			msg['index'] = self.ap_mode.index
			try:
				msg['value'] = self.ap_mode.ValueFromName('Guided')  # AP_MODE_GUIDED
			except ValueError:
				try:
					msg['value'] = self.ap_mode.ValueFromName('GUIDED')  # AP_MODE_GUIDED
				except ValueError:
					msg['value'] = 19 # fallback to fixed index
			print("Setting mode to GUIDED: %s" % msg)
			self._interface.send(msg)

	def set_nav_mode(self):
		"""
		change mode to NAV.
		"""
		if self.ap_mode is not None:
			msg = PprzMessage("ground", "DL_SETTING")
			msg['ac_id'] = self.ac_id
			msg['index'] = self.ap_mode.index
			try:
				msg['value'] = self.ap_mode.ValueFromName('Nav')  # AP_MODE_NAV
			except ValueError:
				try:
					msg['value'] = self.ap_mode.ValueFromName('NAV')  # AP_MODE_NAV
				except ValueError:
					msg['value'] = 13 # fallback to fixed index
			print("Setting mode to NAV: %s" % msg)
			self._interface.send(msg)

	def rc_4_channel_output(self, mode=2, throttle=0.0, roll=0.0, pitch=0.0, yaw=0.0):
		"""
		move at specified velocity in meters/sec with absolute heading (if already in GUIDED mode)
		"""
		msg = PprzMessage("datalink", "RC_4CH")
		msg['ac_id'] = self.ac_id
		msg['mode'] = mode
		msg['throttle'] = throttle
		msg['roll'] = roll
		msg['pitch'] = pitch
		msg['yaw'] = yaw
		print("move at vel body: %s" % msg)
		self._interface.send_raw_datalink(msg)



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--acid", help="aircraft ID", dest='acid', default=1, type=int)
	parser.add_argument("-p", "--plan", help="RC Plan file", dest='plan_file', default="plan.csv", type=str)
	args = parser.parse_args()
	guidance = Guidance(args.acid)
	sleep(0.1)
	guidance.set_guided_mode()
	start_time = time.time()
	plan = open(args.plan_file)

	for l in plan.readlines():
		values = l.split(',')
		plan_time = int(values[0])
		plan_mode = int(values[1])
		plan_throttle = int(values[2])
		plan_roll = int(values[3])
		plan_pitch = int(values[4])
		plan_yaw = int(values[5])
		start_time = time.time()
		while (time.time()-start_time < plan_time):
			guidance.rc_4_channel_output(mode=plan_mode, throttle=plan_throttle, roll=plan_roll, pitch=plan_pitch, yaw=plan_yaw)
			sleep(0.1)


if __name__ == '__main__':
    main()