from gui_tracker import createScreenMatrix, fillMatrix, drawNumbersAndFrames, markTrackWithSampleName, printScreenMatrix, drawSwingBPMnMasterVolumeValue
from changeTextColor import changeStringBgColor, changeStringFontColor


def createVerticalGreyLines(screen_matrix):
	# screen's hight of 17 characters:
	for y in range(17):
		track_position = 2
		# 8 tracks:
		for i in range(8):
			# 5 characters ength for track:
			for j in range(5):
				# each second i
				if y % 2 == 1:
					screen_matrix[y][track_position + j] = changeStringBgColor("black grey", screen_matrix[y][track_position + j])
			track_position += 6
	
	return screen_matrix

def drawInformationThatItIsPlalist(screen_matrix):
	# x is char on x axis, where the tracks ends, and the song info starts:
	x = 2 + 6*8
	info_text = " [Playlist]" 
	# Draw "Song Name:" text
	for i in range(64 - x):
		if i <= len(info_text)-1:
			screen_matrix[0][x + i] = changeStringBgColor("blue", info_text[i])
	return screen_matrix

def drawMenu(screen_matrix, selected = None):
	gui_width = 64
	# x is char on x axis, where the tracks ends, and the song info starts:
	x = 2 + 6*8
	info_text = "    Menu: "
	# Draw "Song Name:" text
	for i in range(gui_width - x):
		if i <= len(info_text)-1:
			screen_matrix[5][x + i] = changeStringBgColor("blue", info_text[i])

	# playlist button:
	button_text = " Save "
	for i in range(gui_width - x):
		if i <= len(button_text) - 1:
			if selected == 0:
				screen_matrix[6][x + i] = formatTextAsSelected(button_text[i])
			else:
				screen_matrix[6][x + i] = button_text[i]

	# clone pattern:
	button_text = " Load "
	for i in range(gui_width - x):
		if i <= len(button_text)-1:
			if selected == 1:
				screen_matrix[6][x + i + 7] = formatTextAsSelected(button_text[i])
			else: 
				screen_matrix[6][x + i + 7] = button_text[i]

	return screen_matrix

def drawInfoAboutInstrument(screen_matrix, selected_instrument):
	gui_width = 64
	x = 2 + 6*8
	text_line_1 = "Inst. info:"
	for i in range(len(text_line_1)):
		screen_matrix[8][x + i + 1] = changeStringBgColor("blue", text_line_1[i])
	
	lines = []
	if selected_instrument == "Drums":
		text_line_1 = " Drums and"
		text_line_2 = "  Samples"
		lines = [text_line_1, text_line_2]
	else:
		text_line_1 = "Midi Port: " + selected_instrument[1]
		text_line_2 = " Channel: " + selected_instrument[-1]
		lines = [text_line_1, text_line_2]
		

	for i in range(len(lines)):
		for j in range(len(lines[i])):
			screen_matrix[9 + i][x + j + 1] = changeStringBgColor("blue", lines[i][j])

	
	return screen_matrix

def main(list_of_instruments = ["Drums", "M1CH1"]):
	screen_matrix = createScreenMatrix()
	screen_matrix = fillMatrix(screen_matrix)
	screen_matrix = drawNumbersAndFrames(first_number = 1, screen_matrix = screen_matrix)
	screen_matrix = markTrackWithSampleName(screen_matrix = screen_matrix, list_of_samples = list_of_instruments)
	screen_matrix = drawInformationThatItIsPlalist(screen_matrix)
	screen_matrix = drawMenu(screen_matrix)
	screen_matrix = drawSwingBPMnMasterVolumeValue(screen_matrix)
	screen_matrix = drawInfoAboutInstrument(screen_matrix, list_of_instruments[1])
	screen_matrix = createVerticalGreyLines(screen_matrix)
	printScreenMatrix(screen_matrix)
	
if __name__ == "__main__":
	main()
