<p align="center">
  <img width="287" height="258" src="ressources/BLAMER.png">
</p>

<p align="center">
  Blamer is an obfuscation code tool designed to translate all comments in your code. This is very useful if you want to deploy your malicious scripts into the wild and blame another country for it.
</p>

<hr>


# What is Blamer?
Blamer is a tool written in Python that translates all comments in a code file into the desired language. Blamer uses the Google Translate library to translate comments.

With Blamer you can release your malicious scripts or piece of code into the wild and let another country be blamed for it. Why? Because it's cool.


# Roadmap
* Because I am very efficient, the roadmap is finished and I need to find new features to add or improve.


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

After running `python3 blamer.py -i someFile.cpp -l ru` all comments will be translated to russian and the result is:

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

You can find a list of all supported languages there: https://github.com/TheTeasel/Blamer/wiki/Supported-languages


# Configuration
## Add more languages
Blamer is shipped with a configuration file to help during comment extraction. This file contains the regex that will be used to extract comments for specified files extensions. By default, Blamer is expecting multi-line comments to start with `/*` and to end with `*/` and single-line comments to start with `//`. There is, however, another configuration for Python files to use `'''` for multi-line comments and `#` for single-line comments.

This is a preview of the default configuration:
```yaml
# This is the list of regex to extract comments in different languages

# The default config is defined like:
# Multi-line comments are located between /* and */
# Single-line comments start with //
default:  '(^)?[^\S\n]*\/(?:\*(.*?)\*\/[^\S\n]*|\/[^\n]*)($)?'

# The python config is defined like:
# Multi-line comments are located between """ and """
# Single-line comments start with #
.py:      '(^)?[^\S\n]*[#\"](?:\"\"(.*?)\"\"\"[^\S\n]*|[^\n]*)($)?'
```

To add a new file type to the configuration, you can add it to the file by giving it's extension as the key (as shown above with `.py`).


## Anonymize
In the `bash_tools` directory you will find two scripts to help you anonymize your traffic.

`anonymize.sh`: Verify if the torsock package is installed and then start it.

`de-anonymize.sh`: Stop the torsock module.

<hr>

<p align="center"> Made with ♥️ by Teasel</p>
