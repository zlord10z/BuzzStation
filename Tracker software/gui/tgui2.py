import os, sys
import time
from changeTextColor import changeStringBgColor

# Lambdas:
clear = lambda: os.system("clear")

# 64x18 characters:
gui_height = 17 #terminal command line is taking one line
gui_width = 64

class TrackerGUI:
	# Create matrix 16 x 64 chars
	def createScreenMatrix(self):
		screen_matrix = []
		for i in range(gui_height):
			screen_matrix.append([])
		return screen_matrix

	# Append matrix with spaces characters:
	def fillMatrix(self, screen_matrix):
		for i in range(gui_height):
			for j in range(gui_width):
				screen_matrix[i].append(" ")	
		return screen_matrix

	# This function: 
	# Draws numbers on the left, from 1-16, which represents quaternotes in pattern
	# Draws 1char-width frames which separates 8 tracks
	# Fills with solid color part of right part of the screen, which create space for other information like actual BPM value
	def drawNumbersAndFrames(self, first_number, screen_matrix):
		for i in range(16):
			id_number = str(first_number + i)
			print(id_number)
			i += 1

			# Draw Numbers 1-16
			if(len(id_number) > 1):
				screen_matrix[i][0] = changeStringBgColor("blue", id_number[0])
				screen_matrix[i][1] = changeStringBgColor("blue", id_number[1])

			else:
				screen_matrix[i][1] = changeStringBgColor("blue", id_number)
				screen_matrix[i][0] = changeStringBgColor("blue", " ")

			# Draw horizontal frame at the top on the screen:
			# On that line, there will be displayed names of samples, assigned to each track
			for j in range(len(screen_matrix[0])):
				screen_matrix[0][j] = changeStringBgColor("blue", " ")

			# Draw vertical frames and fill on the right side:
			for j in range(len(screen_matrix)):
				tracks = 1
				for k in range(len(screen_matrix[0])):
					if(k % 6 == 1 and k > 1 and tracks <= 8):
						screen_matrix[j][k] = changeStringBgColor("blue", " ")
						tracks += 1
					elif(tracks > 8):
						screen_matrix[j][k] = changeStringBgColor("blue", " ")
		return screen_matrix

	def markTrackWithSampleName(self, list_of_samples, screen_matrix):
			# Samples are stored as path to file
			# Extracting names and abbreviate to first 4 letters with ellipsis on the end:
			for i in range(len(list_of_samples)):
				sample_path = list_of_samples[i]
				sample_path = sample_path.split("/")
				sample_name = sample_path[-1]
				sample_name = sample_name.split(".")
				sample_name = sample_name[0]
				sample_name = sample_name[:4] + "…"
				list_of_samples[i] = sample_name

			if(len(list_of_samples) < 8):
				x = 8 - len(list_of_samples)
				for i in range(x):
					list_of_samples.append("Empty")

			tracks = 1
			for i in range(len(screen_matrix[0])):
				if(i % 6 == 2 and tracks <= 8):
					for j in range(5):
						screen_matrix[0][i+j] = changeStringBgColor("blue", list_of_samples[tracks-1][j])
					tracks += 1
			return screen_matrix

	# create string from chars matrix (screen_matrix) and print it out
	def printScreenMatrix(self, screen_matrix):
		frame = ""
		for i in range(len(screen_matrix)):
			for j in range(len(screen_matrix[0])):
				frame += screen_matrix[i][j]
		print(frame)


	def createAndPrint(self, list_of_samples):
		clear()
		screen_matrix = self.createScreenMatrix()
		sceeen_matrix = self.fillMatrix(screen_matrix)
		screen_matrix = self.drawNumbersAndFrames(1, screen_matrix)
		screen_matrix = self.markTrackWithSampleName(list_of_samples, screen_matrix)
		self.printScreenMatrix(screen_matrix)



t_GUI = TrackerGUI()
t_GUI.createAndPrint(["folder/kick_deep_132.mp3"])

try:
	while True: pass
except Exception as e:
	print(e)
finally:
	pass
