#/bin/bash
UNAME_S=$(uname -s)
export VERBOSE=1
export BUILD_TYPE="Debug" # or RelWithDebInfo or Release if you want a crash
case X$UNAME_S in
   XAIX)
    # for AIX
       CC=/opt/freeware/bin/gcc
       CFLAGS='-fexceptions -pthread -mcpu=power8 -maix64 -mvsx'
       CXX=/opt/freeware/bin/g++
       CXXFLAGS='-pthread -mcpu=power8 -maix64 -mvsx'
       OBJECT_MODE=64
       JAVA_HOME=/usr/java8_64
       PATH=/usr/java8_64/bin:/opt/freeware/bin:$PATH
       export CC CFLAGS CXX CXXFLAGS OBJECT_MODE JAVA_HOME PATH
       mkdir -p cmake_aix && \
	   cmake -B cmake_aix -S . -DSWIG_EXECUTABLE=/opt/freeware/bin/swig -DCMAKE_CPP_FLAGS="-I/usr/java8_64/include/aix -I/usr/java8_64/include" -DCMAKE_BUILD_TYPE=$BUILD_TYPE -DBUILD_JAVA=ON -DCMAKE_C_COMPILER=$CC -DCMAKE_CXX_COMPILER=$CXX -DCMAKE_CXX_FLAGS="$CXXFLAGS" -DCMAKE_C_FLAGS="$CFLAGS" 
       (cd cmake_aix && /opt/freeware/bin/make && LIBPATH=`(cd ./lib && pwd )` /opt/freeware/bin/make test )
    ;;
   XLinux)
       rm -rf build_lnx && \
	mkdir -p build_lnx && \
	conan install . -if build_lnx -pr llvm-toolset-7 -s build_type=Debug  --build missing --update  "$@" \
	&& conan build . -bf build_lnx
       ;;
esac
