# pylint: disable=R0903
'''Initialize all configurations when program start running.'''
from slib.banner import SBanner
from slib.config import SConfig
from slib.sqlite import SSqlite
from slib.cache import SCache
from slib.log import SLog
from slib.log import SLogLevel

class SInit():
    '''Initialize all configurations in slib when program start running.'''

    @staticmethod
    def init(show_banner=True, log_all_conf=False):
        '''Initialize all configurations when program start running.'''

        if show_banner is True:
            SBanner.show_banner()

        SLog.init()
        SConfig.init()

        SLog.set_level(SLogLevel.DEBUG)

        SCache.init()
        SSqlite.init()

        if log_all_conf is True:
            SLog.debug('All Configurations:')
            pairs = SConfig.get_all_key_and_value_pairs()
            for key, val in pairs:
                SLog.debug(f'{key} = {val}')
