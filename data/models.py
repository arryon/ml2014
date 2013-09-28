from django.db import models

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

def find_tag(tag):
	lookup = {
		"ankle left":"010-000-024-033",
		"ankle right": "010-000-030-096",
		"chest" : "020-000-033-111",
		"waist" : "020-000-032-221"
	}

	return lookup[tag]