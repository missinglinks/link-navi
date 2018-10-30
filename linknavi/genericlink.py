class Link(object):

    def __init__(self, url, domain, subdomain):
        self.url = url
        self.domain = domain
        self.subdomain = subdomain

    def json(self):
        return {
            "url": self.url,
            "domain": self.domain,
            "subdomain": self.subdomain
        }

class GenericLinkFactory(object):

    def __init__(self):
        pass  

    def __call__(self, url):
        content = url.split("//")[-1].split("/")[0]
        content = content.split(".")

        if len(content) == 2:
            return Link(url, ".".join(content), None )
        elif len(content) == 3:
            subdomain = content[0]
            if subdomain == "www":
                subdomain = None
            return Link(url, ".".join(content[-2:]), subdomain)