import os

import yaml
from fastapi.testclient import TestClient
from future.utils import raise_from
from tavern._plugins.rest.tavernhook import TavernRestPlugin
from tavern.schemas.extensions import import_ext_function
from tavern.util import exceptions


class FastApiTestClient(TestClient):
    def __init__(self, **kwargs):
        app_location = os.getenv("FASTAPI_APP_LOCATION", False)
        if not app_location:
            try:
                app_location = kwargs["app"]["location"]
            except KeyError as e:
                msg = "Need to specify app location (in the form my.module:application)"
                raise_from(exceptions.MissingKeysError(msg), e)
                return
        fastapi_app = import_ext_function(app_location)
        TestClient.__init__(self, fastapi_app)


def load_plugin_schema():
    schema_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "schema.yaml"
    )
    with open(schema_path, "r") as schema_file:
        return yaml.load(schema_file, Loader=yaml.FullLoader)


class FastAPIRestPlugin(TavernRestPlugin):
    session_type = FastApiTestClient
    schema = load_plugin_schema()
