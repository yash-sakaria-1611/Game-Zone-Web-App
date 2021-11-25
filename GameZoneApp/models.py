from django.db import models

class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    game_name = models.CharField(max_length=100)
    game_type = models.CharField(max_length=100)
    age_rest = models.IntegerField()
    height_rest = models.IntegerField()
    rate = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'game'

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    debitcard_id = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    house_no = models.IntegerField()
    street_no = models.IntegerField()
    pin_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer'
