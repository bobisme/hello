## macOS

Install LLVM, Clang and Boehm GC

    brew install llvm bdw-gc

SBT wants Java, so cask-install it

    brew cask install java

Install SBT

    brew install sbt

Compile

    sbt nativeLink

Run

    ./target/scala-2.11/scala-native-out

...or...

    sbt run
