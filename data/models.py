from django.db import models

class Tags(object):
	lookup = {
		"ankle left":"010-000-024-033",
		"ankle right": "010-000-030-096",
		"chest" : "020-000-033-111",
		"waist" : "020-000-032-221"
	}

class Instance(models.Model):

	person = models.CharField(max_length=1)
	sequence = models.IntegerField(max_length=1)

	tag_choices = (
		("010-000-024-033","ankle left"),
		("010-000-030-096","ankle right"),
		("020-000-033-111","chest"),
		("020-000-032-221","waist")
	)

	tag = models.CharField(max_length=15, choices=tag_choices)

	datetime = models.DateTimeField()

	x = models.FloatField()

	y = models.FloatField()

	z = models.FloatField()

	activity = models.CharField(max_length=255)

def find_tag(tag, reverse=False):
	if reverse:
		for key in Tags.lookup:
			if tag == Tags.lookup[key]:
				return key
	else:
		return Tags.lookup[tag]

def get_tag_arrays(data):
	result = []
	for key in Tags.lookup:
		result.append(data.filter(tag=find_tag(key)))

	return result

def get_x_y_z(data):
	ordered = data.order_by('datetime')
	return [[d.x for d in ordered],[d.y for d in ordered],[d.z for d in ordered]]

def get_fft_real(data):
	ordered = data.order_by('datetime')
	return [[d.fftx for d in data],[d.ffty for d in data],[d.fftz for d in data]]

def get_fft_imag(data):
	ordered = data.order_by('datetime')
	return [[d.fftx_imag for d in data],[d.ffty_imag for d in data],[d.fftz_imag for d in data]]


class ContinuousSequence(models.Model):
	instances = models.ManyToManyField(Instance)

	input_x = models.TextField()
	input_y = models.TextField()
	input_z = models.TextField()
