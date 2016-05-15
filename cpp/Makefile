CXXFLAGS := -Wall -Wextra -Werror -pedantic -xc++ -std=c++14
CXX := clang++-3.5

hello: hello.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

run: hello
	./hello
