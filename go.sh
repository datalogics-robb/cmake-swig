#/bin/bash
UNAME_S=$(uname -s)
export VERBOSE=1

case X$UNAME_S in
   XAIX)
    # for AIX
mkdir -p build_aix && \
	conan install . -if build_aix -pr gcc-8-aix71-64 -s build_type=Debug --build missing --update  "$@" \
	&& conan build . -bf build_aix
    ;;
   XLinux)
       rm -rf build_lnx && \
	mkdir -p build_lnx && \
	conan install . -if build_lnx -pr llvm-toolset-7 -s build_type=Debug  --build missing --update  "$@" \
	&& conan build . -bf build_lnx
       ;;
esac
