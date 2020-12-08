import os

from conans  import ConanFile, tools

class RobConan(ConanFile):
    name = 'robb'
    license = 'prop'
    url = 'https://github.com/datalogics-robb/cmake-swig'
    description = 'proof of concept'
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {
        'verbose': [True, False],
        }
    default_options = {
        'verbose': True,
    }
    generators = 'cmake', 'virtualenv', 'json'

    def build_requirements(self):
        self.build_requires('doxygen_installer/1.8.20@datalogics/stable')
        self.build_requires('swig/4.0.2@')
        
    def requirements(self):
        # Deeper requirements listed first so that overriding works.
        self.requires('zlib/APPROVED@datalogics/alias', private=True)
        if self.settings.os == 'Linux' and self.settings.arch == 'x86':
            # We can't get AdoptOpenJDK 8 for Linux i686 so get it elsewhere
            self.requires('java_installer/8.0.272@datalogics/stable', private=True)
        else:
            self.requires('adopt_open_jdk/8.0.272@datalogics/stable', private=True)
