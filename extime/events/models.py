from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    class Meta:
        unique_together = (("name", "date"),)

    def __str__(self):
        return "{name} - {date}".format(name=self.name, date=self.date)


class Klass(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_time = models.TimeField()

    class Meta:
        unique_together = (("name", "event"),)

    def __str__(self):
        return self.name


class Entry(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    bib = models.CharField(max_length=255)
    guess = models.DurationField(blank=True, null=True)

    class Meta:
        unique_together = (("person", "klass"), ("bib", "event"))

    def save(self, *args, **kwargs):
        self.event_id = self.klass.event_id
        super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        return "{name}, {klass}".format(name=self.person.name, klass=str(self.klass))


class Result(models.Model):
    STATUS_CHOICES = (
        ('ok', 'ok'),
        ('dnf', 'did not finish'),
        ('dns', 'did not start'),
        ('dsq', 'disqualified'),
    )
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    time = models.DurationField(blank=True, null=True)
    difference = models.DurationField(blank=True, null=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)

    def __str__(self):
        return "{entry}".format(entry=str(self.entry))

