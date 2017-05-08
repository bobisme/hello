hello: ./src/hello.cr
	crystal build --release $<

run: ./src/hello.cr
	crystal run $<

run-bin: hello
	./$<
