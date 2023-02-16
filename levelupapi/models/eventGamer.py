from django.db import models


class EventGamer(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name='events')
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='event_attendee')