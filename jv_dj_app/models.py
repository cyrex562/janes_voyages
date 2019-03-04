from django.db import models


# Create your models here.

class Voyage(models.Model):
    """

    """
    ship = models.ForeignKey("Ship", null=True, on_delete=models.CASCADE)
    # port visits
    captain = models.ManyToManyField("Captain", blank=True)
    sources = models.ManyToManyField("Source", blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "id: {}, start_date: {}, end_date: {}, ship: {}, captain: {}".format(self.id, self.start_date,
                                                                                    self.end_date, self.ship,
                                                                                    self.captain)


class Ship(models.Model):
    """

    """
    name = models.CharField(max_length=255, blank=True)
    flag = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    home_port = models.ForeignKey("Port", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "id: {}, name: {}, flag: {}, description: {}, home_port: {}".format(self.id, self.name, self.flag,
                                                                                   self.description, self.home_port)


class Port(models.Model):
    """

    """
    name = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey("Location", null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)


class PortVisit(models.Model):
    """

    """
    voyage = models.ForeignKey("Voyage", null=True, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    # transactions
    port = models.ForeignKey("Port", null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    start_port = models.BooleanField(blank=True, default=False)
    end_port = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return "id: {}, start: {}, end: {}, port: {}, start port? {}, end port?: {}".format(self.id, self.start_date,
                                                                                            self.end_date, self.port,
                                                                                            self.start_port,
                                                                                            self.end_port)


class Transaction(models.Model):
    port_visit = models.ForeignKey("PortVisit", null=True, on_delete=models.CASCADE)
    item = models.ForeignKey("Item", null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True)
    BOUGHT = "bought"
    SOLD = "sold"
    BOUGHT_SOLD_CHOICES = (
        (BOUGHT, "bought"),
        (SOLD, "sold")
    )
    bought_sold = models.CharField(choices=BOUGHT_SOLD_CHOICES, max_length=255, default=BOUGHT)
    description = models.TextField(blank=True)


class Source(models.Model):
    source = models.CharField(max_length=512, blank=True)
    description = models.TextField(blank=True)


class Captain(models.Model):
    name = models.CharField(max_length=512, blank=True)
    description = models.TextField(blank=True)


class Item(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)


class Location(models.Model):
    name = models.CharField(max_length=255, blank=True)
    geo_name = models.CharField(max_length=255, blank=True)
    latitude = models.IntegerField(blank=True)
    longitude = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

# END OF FILE
