from gui_tracker import createScreenMatrix, fillMatrix, drawNumbersAndFrames, markTrackWithSampleName, printScreenMatrix
from changeTextColor import changeStringBgColor, changeStringFontColor


def createVerticalGreyLines(screen_matrix):
	# screen's hight of 17 characters:
	for y in range(17):
		track_position = 2
		# 8 tracks:
		for i in range(8):
			# 5 characters ength for track:
			for j in range(5):
				# each second line:
				if y % 2 == 1:
					screen_matrix[y][track_position + j] = changeStringBgColor("black grey", screen_matrix[y][track_position + j])
			track_position += 6
	
	return screen_matrix

def drawInformationThatItIsPlalist(screen_matrix):
	# x is char on x axis, where the tracks ends, and the song info starts:
	x = 2 + 6*8
	info_text = "  Playlist " 
	# Draw "Song Name:" text
	for i in range(64 - x):
		if i <= len(info_text)-1:
			screen_matrix[0][x + i] = changeStringBgColor("blue", info_text[i])
	return screen_matrix

def main():
	screen_matrix = createScreenMatrix()
	screen_matrix = fillMatrix(screen_matrix)
	screen_matrix = drawNumbersAndFrames(first_number = 1, screen_matrix = screen_matrix)
	screen_matrix = markTrackWithSampleName(screen_matrix = screen_matrix, list_of_samples = ["Drums", "M1CH1"])
	screen_matrix = drawInformationThatItIsPlalist(screen_matrix)
	screen_matrix = createVerticalGreyLines(screen_matrix)
	printScreenMatrix(screen_matrix)
	
if __name__ == "__main__":
	main()
