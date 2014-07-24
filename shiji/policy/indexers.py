from plone.indexer.decorator import indexer
from shiji.content.issue import IIssue
from shiji.content.bulletin import IBulletin
from shiji.content.diary import IDiary


@indexer(IIssue)
def category(obj):
    return obj.category

@indexer(IIssue)
def origin(obj):
    return obj.origin

@indexer(IIssue)
def track(obj):
    return obj.track

@indexer(IBulletin, IDiary)
def date(obj):
    return obj.date

@indexer(IBulletin)
def duty(obj):
    return obj.duty

@indexer(IBulletin)
def building(obj):
    return obj.building

