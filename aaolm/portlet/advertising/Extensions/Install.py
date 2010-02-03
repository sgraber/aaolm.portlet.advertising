from zope.component import getUtility
from zope.component import getMultiAdapter
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from Products.CMFCore.utils import getToolByName
from StringIO import StringIO

    
def install(portal):
    """Install portlet, skins, and viewlets"""
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-aaolm.portlet.advertising:default')
    return "Ran all import steps."


def uninstall(portal):
    """Uninstall portlets from slots, skins layer, and viewlets."""
    
    out = []
    cp = getToolByName(portal, 'portal_controlpanel', None)
    setup_tool = getToolByName(portal, 'portal_setup')

    # Remove import steps
    setup_tool.runAllImportStepsFromProfile('profile-aaolm.portlet.advertising:uninstall')
    out.append('Ran runAllImportStepsFromProfile.')

    # Remove installed portlets from columns
    id_portlets = ('advertisingportlet',
                   )
                   
    rightcol = getUtility(IPortletManager, name=u'plone.rightcolumn', context=portal)
    right = getMultiAdapter((portal, rightcol,), IPortletAssignmentMapping, context=portal)
    leftcol = getUtility(IPortletManager, name=u'plone.leftcolumn', context=portal)
    left = getMultiAdapter((portal, leftcol,), IPortletAssignmentMapping, context=portal)
    
    for portlet in id_portlets:
        if portlet in right:
            del right[portlet]
            out.append('Removed %s portlet from right column.' % portlet) 
        if portlet in left:
            del left[portlet]
            out.append('Removed %s portlet from left column.' % portlet)
            
    out.append('Ran all uninstall steps.')
    
    return "\n".join(out)
