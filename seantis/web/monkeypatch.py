from time import time

from zope.interface import implements
from zope.component import getMultiAdapter
from zope import schema
from zope.formlib import form
from zope.i18nmessageid import MessageFactory

from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget
from plone.memoize import instance, ram

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from collective.blogging import HAS_LINGUA_PLONE
from collective.blogging import _
from collective.blogging.interfaces import IBlog, IEntryMarker

PLMF = MessageFactory('plonelocales')

def patchedArchives(self):
    ts = getToolByName(self.context, 'translation_service')
    catalog = self.tools.catalog()
    entries = catalog(
        object_provides=IEntryMarker.__identifier__,
        path='/'.join(self.blog().getPhysicalPath()),
    )
    
    base_url = '%s?publish_year=' % self.blog_url
    archives = {}
    for entry in entries:
        year = archives.get(entry.publish_year, {'count':0, 'entries':{}})
        month = year['entries'].get(entry.publish_month, 0)
        
        year['entries'][entry.publish_month] = month + 1
        year['count'] = year['count'] + 1
        archives[entry.publish_year] = year
    
    # sort months and add year counts
    result = []
    for archive in archives.keys():
        year_url = '%s%s' % (base_url, archive)
        result.append({
            'year'  : archive,
            'count' : archives[archive]['count'],
            'url'   : year_url,
            # 'months': [],
            'months': sorted([(m, c, '%s&publish_month=%s' % (year_url, m), PLMF(ts.month_msgid(m), default=ts.month_english(m))) \
                                for m,c in archives[archive]['entries'].items()], reverse=True)
        })
    return sorted(result, key=lambda archive: archive['year'], reverse=True)
