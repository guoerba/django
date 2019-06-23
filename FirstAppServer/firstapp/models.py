from django.db import models


class HandynastyPrefecture(models.Model):
    prefecture = models.CharField(max_length=24)
    state = models.ForeignKey('HandynastyState', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.prefecture,self.state)

    class Meta:
        managed = False
        db_table = 'HanDynasty_Prefecture'


class HandynastyState(models.Model):
    state = models.CharField(max_length=12)

    def __str__(self):
        return self.state

    class Meta:
        managed = False
        db_table = 'HanDynasty_State'
