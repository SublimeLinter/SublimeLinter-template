SublimeLinter-contrib-groovyc
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-groovyc.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-groovyc)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [groovyc](http://www.groovy-lang.org/download.html). It will be used with files that have the “.groovy” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `groovyc` is installed on your system.

In order for `groovyc` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

- `GROOVY_HOME` environment variable has to be set to main groovy folder (inside this folder you can find directories like `bin`, `lib` and `conf`)

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-groovyc settings:

|Setting|Description    |
|:------|:--------------|
|classpath    |directories to add to classpath (dependencies), project folder is added automatically|
|sourcepath    |directories to add as source path|

# Example SublimeLinter settings

## Global Settings
```json
{
    "linters":
    {
        "groovy":{
            "env": {
                "GROOVY_HOME": "C:\\groovy\\apache-groovy-binary-2.6.0-alpha-3\\groovy-2.6.0-alpha-3"
            }
        }
    },
    "paths":
    {
        "linux":
        [
        ],
        "osx":
        [
        ],
        "windows":
        [
            "C:\\groovy\\apache-groovy-binary-2.6.0-alpha-3\\groovy-2.6.0-alpha-3\\bin"
        ]
    }
}
```

## Project settings

```
"SublimeLinter": {
        "linters": {
            "groovy": {
                "classpath": "C:\\code\\project1\\src"
            }
        }
    }
```