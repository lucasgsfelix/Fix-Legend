
import re
import time

#from datetime import datetime
import datetime


def fix_time(time_value, fix):


	time_value = datetime.datetime.strptime(time_value, '%H:%M:%S,%f')

	#time_value = time.mktime(time_value.timetuple())

	fix = datetime.datetime.strptime("00:01:00,000", '%H:%M:%S,%f')

	#import datetime

	time_value = time_value + datetime.timedelta(seconds=60)


	try:
		return str(time_value).split(' ')[1].replace('.', ',')
	except:
		return str(time_value).replace('.', ',')


if __name__ == '__main__':


	file_name = "My Name Is Khan 2010 Hindi BRRip 720p x264 AAC 5.1...Hon3y.srt"

	# time in seconds
	time_subtract = 60

	with open(file_name, 'r', encoding='utf-8') as sub_file:

		sub = sub_file.read().split('\n')

		time_regex = r'[\d]{2}:[\d]{2}:[\d]{2},[\d]{3}'

		arrow = ' --> '

		timestamps = []

		for index, sub_step in enumerate(sub):

			results = [(a.end()) for a in list(re.finditer(time_regex, sub_step))]

			if results:

				sub_step = sub_step.split(arrow)

				sub_step = list(map(lambda x: fix_time(x, time_subtract), sub_step))

				if ',' not in sub_step[0]:
					print(sub_step[0])

				if ',' not in sub_step[0]:

					sub_step[0] += ',000'

				if ',' not in sub_step[1]:

					sub_step[1] += ',000'

				sub[index] = sub_step[0] + arrow + sub_step[1]

	with open("new_sub.srt", 'w', encoding='utf-8') as new_file:

		new_file.write('\n'.join(sub))
