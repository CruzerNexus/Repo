#peaksAndValleys.py
def peaks(data):
	#goal: return indices of peaks
	peaks = []
	for num in range(len(data)):
		#run through each index of "data"
		if num+1 ==len(data):
			#if this is the final index, it will break the loop before index error
			break
		elif num == 0:
			continue
		elif data[num-1] < data[num] > data[num+1]:
			peaks.append(num)
		else:
			continue
	return peaks

def valleys(data):
	valleys = []
	for num in range(len(data)):
		if num + 1 == len(data):
			break
		elif num == 0:
			continue
		elif data[num-1] > data[num] < data[num+1]:
			valleys.append(num)
		else:
			continue
	return valleys

def peaksAndValleys(data):
	peakList = peaks(data)
	valleyList = valleys(data)
	peaksAndValleys = []
	peaksAndValleys.extend(peakList)
	peaksAndValleys.extend(valleyList)
	peaksAndValleys.sort()
	print(peaksAndValleys)
	return peaksAndValleys





#print(peaks(data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]))
#print(valleys(data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]))
print(peaksAndValleys(data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]))