from tortoise.models import Model
from tortoise import fields
import datetime


class Guild(Model):

    _id = fields.BigIntField(pk=True)
    prefix = fields.CharField(max_length=3) # add default prefix here
    blacklisted = fields.BooleanField()
    # redirect = fields.ListField(fields.IntegerField, default=list)
    # silence = fields.BooleanField(default=False)
    # spawn_boost = fields.DateTimeField(default=datetime.min)

class Trainer(Model):

    _id = fields.BigIntField(pk=True)
    selected = fields.BigIntField() # chek if its int field
    balance = fields.BigIntField()
    redeems = fields.BigIntField()
    # order_by = fields.StringField(default='number')
    # caught = fields.IntegerField(default=0)
    # released = fields.IntegerField(default=0)
    # shinies_caught = fields.IntegerField(default=0)
    # last_voted = fields.DateTimeField(default=datetime.min)
    # vote_total = fields.IntegerField(default=0)
    # vote_streak = fields.IntegerField(default=0)
    # silence = fields.BooleanField(default=False)
    started_at = fields.DatetimeField(required=True)
    # suspended = fields.BooleanField(default=False)
    # pokedex = fields.DictField(default=dict)
    # boost_expires = fields.DateTimeField(default=datetime.min)
    # rewards = fields.DictField(default=dict)
    # baltop = fields.BooleanField(default=True)
    # shiny_hunt = fields.IntegerField(default=None)
    # shiny_streak = fields.IntegerField(default=0)
    # team = fields.ObjectIdField(default=None)
    # vote_reminder = fields.BooleanField(default=False)
    # technical_machines = fields.ListField(fields.IntegerField, default=list)
    # bronze_crates = fields.IntegerField(default=0)
    # silver_crates = fields.IntegerField(default=0)
    # golden_crates = fields.IntegerField(default=0)
    # diamond_crates = fields.IntegerField(default=0)
    # deluxe_crates = fields.IntegerField(default=0)
    # shards = fields.IntegerField(default=0)
    # shiny_charm = fields.DateTimeField(default=datetime.min)
