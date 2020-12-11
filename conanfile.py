import os

from conans  import ConanFile, CMake, tools

class RobConan(ConanFile):
    name = 'CMakeSwig'
    version = '1.0.0'
    license = 'prop'
    url = 'https://github.com/datalogics-robb/cmake-swig'
    description = 'proof of concept'
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {
        'verbose': [True, False],
        'build_java': [True, False],
        'build_python': [True, False],
        'build_dotnet': [True, False],
        }
    default_options = {
        'verbose': True,
        'build_java': True,
        'build_python': False,
        'build_dotnet': False,
    }
    generators = 'cmake', 'virtualenv', 'json'

    def build_requirements(self):
        self.build_requires('doxygen_installer/1.8.20@datalogics/stable')
        self.build_requires('swig/4.0.2@')
        
    def requirements(self):
        # Deeper requirements listed first so that overriding works.
        self.requires('catch2/2.13.3@', private=True)
        self.requires('zlib/APPROVED@datalogics/alias', private=True)
        if self.settings.os == 'Linux' and self.settings.arch == 'x86':
            # We can't get AdoptOpenJDK 8 for Linux i686 so get it elsewhere
            self.requires('java_installer/8.0.272@datalogics/stable', private=True)
        else:
            self.requires('adopt_open_jdk/8.0.272@datalogics/stable', private=True)

    def configure_cmake(self):
        cmake = CMake(self,
                      msbuild_verbosity="normal" if self.options.verbose else "minimal")
        cmake.definitions['CMAKE_VERBOSE_MAKEFILE'] = str(self.options.verbose).upper()
        if self.settings.os == "Macos":
            cmake.generator = "Xcode"
        if cmake.generator.startswith("Visual Studio"):
            # Conan doesn't usually pass this to Visual Studio builds, but APDFL's CMakeLists.txt
            # depends on it
            cmake.definitions['CMAKE_BUILD_TYPE'] = cmake.build_type
        # Enable building Java
        cmake.definitions['BUILD_JAVA'] = 'ON' if self.options.build_java else 'OFF'
        # Enable building CSharp
        cmake.definitions['BUILD_DOTNET'] = 'ON' if self.options.build_dotnet else 'OFF'
        # Enable building Python
        cmake.definitions['BUILD_PYTHON'] = 'ON' if self.options.build_python else 'OFF'

        # If you're ever wondering what commands these are executing, put
        # CONAN_PRINT_RUN_COMMANDS=1 into the environment.
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()
        cmake.test()

