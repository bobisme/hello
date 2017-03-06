default: hello.jar

%.jar: %.kt
	kotlinc $< -include-runtime -d $@

%.js: %.kt
	kotlinc-js $< -output $@

run: hello.jar
	java -jar hello.jar

run-js: hello.js
	node hello.js
