from django.db import models

# Create your models here.
class Ability(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return "%s the ability" % self.name

class Stat(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return "%s the stat" % self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abilities = models.ManyToManyField(Ability, through='PokemonAbility')
    stats = models.ManyToManyField(Stat, through='PokemonStat')
    
    def __str__(self):
        return "%s the pokemon" % self.name

class PokemonAbility(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)

class PokemonStat(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    stat = models.ForeignKey(Stat, on_delete=models.CASCADE)
