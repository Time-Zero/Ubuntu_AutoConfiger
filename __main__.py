#!/usr/bin/env python3.7.2  or greater  (or newer)
from symbol import pass_stmt
import urllib3
import os

class Ubuntu_AutoConfigure(object):
    def __init__(self):
        try:
            http = urllib3.PoolManager()
            http.request('GET', 'https://baidu.com')
        except urllib3.exceptions.HTTPError as e:
            print("HTTPError in  poolmanager: %s" % e.message)
            print('Some error in your internet connection,please try again later')
            exit()
    
    def get_ubuntu_version(self):
        with open('/etc/issue','r') as f:
            version = f.readline()
            # if version.startswith('Ubuntu 22.04'):
            #     return 'Ubuntu 22.04'
            # elif version.startswith('Ubuntu 20.04'):
            #     return 'Ubuntu 20.04'
            # elif version.startswith('Ubuntu 18.04'):
            #     return 'Ubuntu 18.04'
            # else:
            #     return 
            return version
    
    def up_file_permissions(self):
        os.system('sudo chmod -R 777 /etc/default/locale')
        os.system('sudo chmod -R 777 /etc/apt/sources.list')

    def change_source(self,f): 
        with open('/etc/apt/sources.list','w') as s:
            s.writelines(f.readlines())
            s.flush()
            s.close()

    def change_language(self):
        with open('/etc/default/locale','w') as f:
            new_locale = open('locale','r')
            f.writelines(new_locale.readlines())
            f.flush()
            f.close()   
    
    def fix_file(self):
        with open('fix') as  f:
            for line in f.readlines():
                os.system(line)
    
    def load_software(self):
        with open('software_list') as f:
            for line in f.readlines():
                if(not line.startswith('#')):
                    os.system(line)

    def run(self):
        try:
            version = self.get_ubuntu_version()
            if version.startswith('Ubuntu 22.04'):
                f = open('Source_Ubuntu22.04','r')
            elif version.startswith('Ubuntu 20.04'):
                f = open('Source_Ubuntu20.04','r')
            elif version.startswith('Ubuntu 18.04'):
                f = open('Source_Ubuntu18.04','r')
            else:
                raise Exception(f'{version} is not supported')
            self.up_file_permissions()
            self.change_source(f)
            self.load_software()
            self.change_language()
            self.fix_file()
            os.system('reboot')
        except Exception as e:
            print(e)
            exit()

if __name__ == '__main__':
    config = Ubuntu_AutoConfigure()
    config.run()
