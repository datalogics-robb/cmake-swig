#/bin/bash

export CC=/opt/freeware/bin/gcc
export CXX=/opt/freeware/bin/g++
export CXXFLAGS='-mcpu=power8 -pthread -mvsx -maix64 -std=c++14'
export CFLAGS='-mcpu=power8 -pthread -mvsx -maix64'
export JAVA_HOME=/usr/java8_64
export VERBOSE=1

mkdir -p build
cmake -S . -B build
cmake --build build
$JAVA_HOME/bin/java -Djava.library.path=build -cp target/testexception-1.0-SNAPSHOT.jar TestException
