from flask.ext import restful
from time import sleep


class Resource(restful.Resource):
    def dispatch_request(self, *args, **kwargs):
        # XXX: Because this is a demo we want it to appear as if requests to
        # the API are slow, so we induce a delay
        sleep(2)

        return super(Resource, self).dispatch_request(*args, **kwargs)