import wiringpi as wpi
import time
import gpio.tone as tone
import threading

BUZZER_PIN = 26
#total_count = 0
thd = False

lock = threading.Lock()

def init():
	wpi.wiringPiSetup()
	wpi.softToneCreate(BUZZER_PIN)

def play(notes):
	for note in notes:
		wpi.softToneWrite(BUZZER_PIN, note[0])
		time.sleep(note[1])
		wpi.softToneWrite(BUZZER_PIN, 0)
	
def octave():
	octave = [
		(NOTE_C4, 0.5), 
		(NOTE_D4, 0.5),
		(NOTE_E4, 0.5),
		(NOTE_F4, 0.5),
		(NOTE_G4, 0.5),
		(NOTE_A4, 0.5),
		(NOTE_B4, 0.5),
		(NOTE_C5, 0.5) ]
         
	play(octave)

def school_bell():
		
	notes = [
		(NOTE_G4, 0.35), (NOTE_G4, 0.35), (NOTE_A4, 0.35), (NOTE_A4, 0.35),
		(NOTE_G4, 0.35), (NOTE_G4, 0.35), (NOTE_E4, 0.70), (NOTE_G4, 0.35),
		(NOTE_G4, 0.35), (NOTE_E4, 0.35), (NOTE_E4, 0.35), (NOTE_D4, 0.70),
		(NOTE_G4, 0.35), (NOTE_G4, 0.35), (NOTE_A4, 0.35), (NOTE_A4, 0.35),
		(NOTE_G4, 0.35), (NOTE_G4, 0.35), (NOTE_E4, 0.70), (NOTE_G4, 0.35),
		(NOTE_E4, 0.35), (NOTE_D4, 0.35), (NOTE_E4, 0.35), (NOTE_C4, 0.70) ]


	play(notes)

def mute(pin):
	pin = BUZZER_PIN
	wpi.softToneWrite(pin, 0)
	time.sleep(0.3)

def siren(pin):	
	duration = 300/8;
	
	#global total_count
	#total_count += 1
	
	global thd
	thd = True

	lock.acquire()
		
	if(thd):
		for i in range(0, 4):
			wpi.softToneWrite(BUZZER_PIN, 20*i)
			time.sleep(duration * 0.2/1000)

	
		for i in range(120, 24, -1):
			wpi.softToneWrite(BUZZER_PIN, 20*i)
			time.sleep(duration * 0.2/1000)

		for i in range(25, 121):
			wpi.softToneWrite(BUZZER_PIN, 20*i)
			time.sleep(duration * 0.2/1000)

		for i in range(3, -1, -1):
			wpi.softToneWrite(BUZZER_PIN, 20*i)
			time.sleep(duration * 0.2/1000)
	
	lock.release()
	mute(BUZZER_PIN);


if __name__ == '__main__':
	init()	
	# octave()
	school_bell()
	time.sleep(0.1)
	# siren()


