# Install script for directory: /home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/SEAL-3.4/seal" TYPE FILE FILES
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/batchencoder.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/biguint.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/ciphertext.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/ckks.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/modulus.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/context.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/decryptor.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/intencoder.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/encryptionparams.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/encryptor.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/evaluator.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/galoiskeys.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/intarray.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/keygenerator.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/kswitchkeys.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/memorymanager.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/modulus.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/plaintext.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/publickey.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/randomgen.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/randomtostd.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/relinkeys.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/seal.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/secretkey.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/serialization.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/smallmodulus.h"
    "/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/valcheck.h"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/kabe/Downloads/Thesis/SEAL-Python-master/SEAL/native/src/seal/util/cmake_install.cmake")

endif()

