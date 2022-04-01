# pylint: disable=W0703
"""Server entry point."""
import traceback

from slib.init import SInit
from slib.log import SLog
from server.server import SServer

if __name__ == "__main__":
    try:
        SInit.init(log_all_conf=False)
        SServer.init(debug=False)

    except Exception as e:
        SLog.error(e)
        SLog.error(traceback.format_exc())

        print(e)
        print(traceback.format_exc())
