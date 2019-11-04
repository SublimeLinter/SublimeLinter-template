Creating a Linter Plugin
========================

- Click "use this template" to bootstrap your new linter.
- Clone it into Packages.
- Change a linter.py.
- Update the README and replace `__linter__` placeholders.
- Update messages/install.txt and replace `__linter__` placeholders.
- Open a PR in our [package_control repo](https://github.com/SublimeLinter/package_control_channel) to make it available to others.

Additional documentation can be found at [sublimelinter.com](http://sublimelinter.com).


Updating class attributes
--------------------------
Template linter plugins are created with almost all of the Linter class attributes filled in with the default values. To make your new linter plugin functional, at the very least you need to do the following:

- Change the default `'selector'` to include the scopes you want the linter to lint.

- Change the `cmd` attribute to include the executable and arguments you want to include on *every* run. Usually this should be a tuple like `('linter', '-fooarg', '-etc', '-')`. You can also make `cmd` a method (or callable in python speak) which returns such a tuple.

- Change the `regex` attribute to correctly capture the error output from the linter.

- Change the `multiline` attribute to `True` if the regex parses multiline error messages.

Other, optional, attributes include:

- If the linter executable does not accept input via `stdin`, set the `tempfile_suffix` attribute to the filename suffix of the temp files that will be created.

- If the linter outputs errors only on `stderr` or `stdout`, set `error_stream` to `util.STREAM_STDERR` or `util.STREAM_STDOUT` respectively.

You should remove attributes that you do not change, as their values will be provided by the superclass. More information can be found in the [docs](https://github.com/SublimeLinter/SublimeLinter/blob/master/docs/linter_attributes.rst).
