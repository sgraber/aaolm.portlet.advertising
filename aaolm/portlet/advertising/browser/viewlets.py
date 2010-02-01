from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase


class AdvertisingPaypalViewlet(ViewletBase):
    """Render paypal button in a viewlet."""
    
    render = ViewPageTemplateFile('advertising_paypal.pt')
    
    def update(self):
        pass

class AdvertisingAdsenseTopViewlet(ViewletBase):
    """Render adsense template in a viewlet around the title area."""
    
    render = ViewPageTemplateFile('advertising_adsense_top.pt')
    
    def update(self):
        pass

class AdvertisingAdsenseBottomViewlet(ViewletBase):
    """Render adsense template in a viewlet below the content area."""
    
    render = ViewPageTemplateFile('advertising_adsense_bottom.pt')
    
    def update(self):
        pass

class AdvertisingBannerViewlet(ViewletBase):
    """Render advertising banner in a viewlet at the portal top."""
    
    render = ViewPageTemplateFile('advertising_banner.pt')
    
    def update(self):
        pass