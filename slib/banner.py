# pylint: disable=R0903
'''
 Generate the ASCII art text form the following site:
 URL: https://patorjk.com/software/taag/#p=display&f=Slant&t=SLIB
 Font: Slant
'''

class SBanner():
    '''Show banner.'''

    @staticmethod
    def show_banner():
        '''Show banner.'''

        banner = r'''
   ___________________    ____  ________________ 
  / ___/ ___/_  __/   |  / __ \/_  __/ ____/ __ \
  \__ \\__ \ / / / /| | / /_/ / / / / __/ / /_/ /
 ___/ /__/ // / / ___ |/ _, _/ / / / /___/ _, _/ 
/____/____//_/ /_/  |_/_/ |_| /_/ /_____/_/ |_|                                    
        '''

        print('=================================================')
        print(banner)
        print('=================================================')
