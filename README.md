<p align="center">
  <img width="287" height="258" src="ressources/BLAMER.png">
</p>

<p align="center">
  Blamer is a tool designed to translate all comments in your code in order to blame someone else.
</p>

<p align="center">
  :warning: Blamer is still under development :warning:
</p>

<hr>

# What is Blamer?
Blamer is a tool written in Python that translates all comments in a code file into the desired language. Blamer uses the Google Translate library to translate comments.

For the moment, Blamer only detects comments starting with `//` or multi-line comments surrounded by `/*` and `*/` but it is planned for future versions to add other parameters.

With Blamer you can release your malware into the wild while blaming another country. Why? Because it's cool.

# Requirements
To use Blamer, you'll need additional libraries. You can install them by typing `pip3 install requirements.txt`.

# Usage
You can type `python3 blamer.py -h` in order to get help about how to use Blamer. 

To show you a concrete example of what you can do with Blamer, let's take this initial piece of code:
```
// This is a comment
int var = 0;

/* This is a multiline comment */
for(int i = 0; i < 10; ++i){
    var += i;
}

/*
What about this comment ?
*/

/*
    What about that one
*/
```

After running `python3 blamer.py -i someFile.cpp -o myResult.cpp -d ru` all comments will be translated to russian and the result is:

```
// Это комментарий
int var = 0;

/ * Это многострочный комментарий * /
for(int i = 0; i < 10; ++i){
    var += i;
}

/ *
Что насчет этого комментария?
* /

/ *
    Как насчет того
* /
```
