from changeTextColor import changeStringFontColor, changeStringBgColor

# Lambdas:
clear = lambda: os.system("clear")

# 64x18 characters:
gui_height = 17 #terminal command line is taking one line
gui_width = 64

# Create matrix 16 x 64 chars
def createScreenMatrix():
	screen_matrix = []
		
	for i in range(gui_height):
		row_matrix = []
		for j in range(gui_width):
			row_matrix.append("")
		screen_matrix.append(row_matrix)
		
	return screen_matrix


def drawFrame(screen_matrix):
	for i in range(len(screen_matrix)):
		for j in range(len(screen_matrix[i])):
			if i < 1 or i > len(screen_matrix) - 4:
				screen_matrix[i][j] = changeStringBgColor("blue", " ")
				
			elif j < 2 or j > len(screen_matrix[i]) - 8:
				screen_matrix[i][j] = changeStringBgColor("blue", " ")
				screen_matrix[i][j] = changeStringBgColor("blue", " ")

			else:
				screen_matrix[i][j] = " "
	return screen_matrix
			
def drawVerticalLinesForBetterVisibility(screen_matrix):
	x_position = 9
	x = 0
	
	for i in range(8):
		for j in range(13):
			for k in range(3):
				screen_matrix[13-j][x_position + x + k] = changeStringBgColor("black grey", " ")
		x += 6
	return screen_matrix


notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]
notes_displayed = []

def drawPartOfPiano(screen_matrix, y_position, x_poistion, octave, start_note = 0, counter = 0):
	for i in range(12):
		note = " "
		note_index = start_note + i
		if note_index > 11 or counter > 12: break
		
		notes_displayed.append(notes[note_index] + str(octave))
	
		# string with note and octave has to be in length of 3 characters:
		if len(notes[note_index]) == 2:
			note = notes[note_index] + str(octave)
		else:
			note += notes[note_index] + str(octave)
		
		counter += 1
		
		print(note)
		for j in range(4):
			# draw first 4 chars which makes piano key:
			if len(notes[note_index]) > 1:
				pass # drawing back keys
			else:
				screen_matrix[y_position - i][j+x_poistion] = changeStringBgColor("grey", " ")
				# drawing part of white keys:
				
			if j == 0:
				pass
			else:
				# print(note)
				# draw last 3 chars which makes piano key:
				# drawing key and note on key:
				note_part = changeStringFontColor("black", note[j-1])
				note_part = changeStringBgColor("grey", note_part)
				screen_matrix[y_position - i][j+x_poistion+3] = note_part
	return counter, screen_matrix

def drawPiano(screen_matrix, octave, start_note=0):
	x = drawPartOfPiano(screen_matrix = screen_matrix, 
							  y_position = 13, 
							  x_poistion = 2, 
							  octave = octave, 
							  start_note = start_note)
	counter = x[0]
	screen_matrix = x[1]
	
	screen_matrix = drawPartOfPiano(screen_matrix = screen_matrix, 
									y_position = 13 - counter, 
									x_poistion = 2, 
									octave = octave + 1, 
									counter = counter)[1]
	return screen_matrix


def drawQuarterTime(screen_matrix):
	x_position = 9
	x = 0
	for i in range(16):
		char_number = chr(0x2488 + i)
		if i % 4 == 0:
			screen_matrix[0][x_position + x] = changeStringFontColor("black", changeStringBgColor("blue", char_number))
		else:
			screen_matrix[0][x_position + x] = changeStringBgColor("blue", char_number)
		x += 3
	return screen_matrix

def drawPatternNumber(screen_matrix, pattern_number = 1):
	text_to_print = "Pattern: " + str(pattern_number)
	axisx_start_printing = (gui_width - len(text_to_print))
	for i in range(len(text_to_print)):
		screen_matrix[gui_height-1][axisx_start_printing + i] = changeStringBgColor("blue", text_to_print[i])

	return screen_matrix

def drawSwingBPMValueAndMidiChannelNumber(screen_matrix, bpm_value = 100, swing_value = 40, channel_number = 1):
	
	text_to_print = "BPM: " + str(bpm_value) + 8 * " " + "Swing: " + str(swing_value) + 8 * " " + "Channel: " + str(channel_number)
	for i in range(len(text_to_print)):
		screen_matrix[gui_height-1][i+2] = changeStringBgColor("blue", text_to_print[i])

	return screen_matrix


def drawIsPlaying(screen_matrix, is_playing = False):
	playing_info = "Pause"
	if is_playing: playing_info = "Playing"
	axisx_start_printing = int(gui_width / 2 - len(playing_info))
	for i in range(len(playing_info)):
		screen_matrix[gui_height-3][axisx_start_printing + 1 + i] = changeStringBgColor("blue", playing_info[i])

	return screen_matrix

def drawButtons(screen_matrix, selected = None):
	button_playlist = " Playlist "
	button_new = " New "
	button_clone = " Clone "
	button_previous_pattern = " ⇽ "
	button_next_pattern = " ⇾ "
	
	toDraw =  button_previous_pattern + "?" + button_playlist + "?" + button_new + "?" +  button_clone + "?" + button_next_pattern
	question_mark_counter = 0
	for i in range(len(toDraw)):
		if toDraw[i] == "?": 
			question_mark_counter += 1
			
		elif question_mark_counter == selected:
			screen_matrix[gui_height-2][15 + i] = changeStringBgColor("grey", toDraw[i])
		else:
			screen_matrix[gui_height-2][15 + i] = toDraw[i]
	return screen_matrix

def drawNotesOnPianoRoll(screen_matrix, pattern = None):	
	x_position = 9
	y_position = 13
	if pattern is not None:
		# for 16 quarter notes:
		for i in range(16):
			# for each note in quareted (chord):
			for j in range(len(pattern[i])):
				if pattern[i][j][0] in notes_displayed:
					y = y_position -  notes_displayed.index(pattern[i][j][0]) 
					
					# quarter note displayed as 3 character square:
					for k in range(pattern[i][j][1] * 3):
						screen_matrix[y][x_position + i + k] = changeStringBgColor("white", " ")
			x_position += 3
	return screen_matrix
		
	
		
def printGUI(screen_matrix):
	toprint = ""
	for i in range(len(screen_matrix)):
		for j in range(len(screen_matrix[i])):
			toprint += screen_matrix[i][j]
	print(toprint)


def main(pattern=None):
	screen_matrix = createScreenMatrix()
	screen_matrix = drawFrame(screen_matrix)
	screen_matrix = drawVerticalLinesForBetterVisibility(screen_matrix)
	screen_matrix = drawPiano(screen_matrix, octave = 5, start_note = 1)
	screen_matrix = drawQuarterTime(screen_matrix)
	screen_matrix = drawPatternNumber(screen_matrix, pattern_number = 1)
	screen_matrix = drawSwingBPMValueAndMidiChannelNumber(screen_matrix, bpm_value = 100, swing_value = 40, channel_number = 1)
	screen_matrix = drawIsPlaying(screen_matrix, True)
	screen_matrix = drawButtons(screen_matrix, selected = None)
	screen_matrix = drawNotesOnPianoRoll(screen_matrix, pattern=None)
	printGUI(screen_matrix)


def createExamplePattern():
	pattern = []
	for i in range(16):
		l = []
		pattern.append(l)
	
	#                   note, note length
	pattern[0].append(["C#5", 1])
	pattern[0].append(["D#5", 1])
	pattern[0].append(["C#7", 1])
	pattern[4].append(["C#5", 3])
	return pattern
	
if __name__ == "__main__":
	example_pattern = createExamplePattern()
	#print(example_pattern)
	#main(pattern = example_pattern)
	main()

