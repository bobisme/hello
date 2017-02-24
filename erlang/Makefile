default: hello.beam

%.beam: %.erl
	erlc $<

run: hello.beam
	erl -noshell -s hello start -s init stop
