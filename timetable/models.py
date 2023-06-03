from django.db import models


class Seed(models.Model):
    INTO_THE_GROUND = 'into_the_ground'
    THROUGH_SEEDLINGS = 'through_seedlings'
    BOTH = 'both'
    SOW_WAY_CHOICES = [
        (INTO_THE_GROUND, 'into_the_ground'),
        (THROUGH_SEEDLINGS, 'through_seedlings'),
        (BOTH, 'both')
    ]

    VEGETABLE = 'vegetable'
    FRUIT = 'fruit'
    HERB = 'herb'
    FLOWER = 'flower'
    MUSHROOM = 'mushroom'
    TYPE_CHOICES = [
        (FLOWER, 'flower'),
        (FRUIT, 'fruit'),
        (HERB, 'herb'),
        (MUSHROOM, 'mushroom'),
        (VEGETABLE, 'vegetable')
    ]

    name = models.CharField(max_length=200)
    sow_way = models.CharField(max_length=20, choices=SOW_WAY_CHOICES)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    image = models.CharField(max_length=200)
    stratification = models.BooleanField(default=False)
    sow_start = models.CharField(max_length=100)
    sow_end = models.CharField(max_length=100)
    expired_on = models.DateField()

    @property
    def emoji(self):
        sow_way_emoji = {'into_the_ground': '🪴', 'through_seedlings': '&#129716;', 'both': '🪴🖼'}
        return sow_way_emoji[self.sow_way]

    def coloring_cell(self, month):
        start = self.sow_start.replace('2023-', '')
        end = self.sow_end.replace('2023-', '')

        if int(end) >= month >= int(start):
            return True
        return False
