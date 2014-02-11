from plone.indexer.decorator import indexer
from shiji.content.bulletin import IBulletin
from shiji.content.diary import IDiary


@indexer(IBulletin, IDiary)
def date(obj):
    return obj.date

@indexer(IBulletin)
def duty(obj):
    return obj.duty

@indexer(IBulletin)
def building(obj):
    return obj.building

