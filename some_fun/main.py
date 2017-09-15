def main(mbox, res1, res2):
	mbox_file = open(mbox, "r")
	result1_file = open(res1, "w")
	result2_file = open(res2, "w")

	lines = mbox_file.readlines()

	l_from = []
	l_date = []
	l_subject = []

	# from (date): subject
	for line in lines:
		if 'From: ' in line:
			l_from.append(line.split('From: ')[-1].rstrip())
		elif '.org; ' in line:
			l_date.append(" ({0}): ".format(line.split('.org; ')[-1].rstrip()))
		elif 'Subject: ' in line:
			l_subject.append(line.split('Subject: ')[-1].rstrip())

	for item in zip(l_from, l_date, l_subject):
		result1_file.write('{0}\n{1}\n'.format(''.join(item), 50*'-'))
		print('{0}\n{1}'.format(''.join(item), 50*'-'))

	# from: quantity
	dict_ = {i:l_from.count(i) for i in l_from}
	for value in sorted(dict_):
		result2_file.write('{0}: {1}\n'.format(value, dict_[value]))
		print('{0}: {1}'.format(value, dict_[value]))

	result1_file.close()
	result2_file.close()
	mbox_file.close()

main("mbox.txt", "result_1.txt", "result_2.txt")
