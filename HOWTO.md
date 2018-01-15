Creating a Linter Plugin
========================

. Fork this repo to bootstrap your new linter.
. Clone it into Packages.
. Change a linter.py.
. Update the README and replace `__linter__` placeholders.
. Update messages/install.txt and replace `__linter__` placeholders.
. Open a PR in our [package_control repo](https://github.com/SublimeLinter/package_control_channel) to make it available to others.

Additional documentation can be found at [sublimelinter.com](http://sublimelinter.com).


Updating class attributes
--------------------------
Template linter plugins are created with almost all of the Linter class attributes filled in with the default values. To make your new linter plugin functional, at the very least you need to do the following:

- Change the `syntax` attribute to indicate the syntax (or syntaxes) that the linter lints.

- Change the `cmd` attribute to include the executable and arguments you want to include on every run. Or if you are going to implement a `cmd <cmd-method>` method, set the attribute to `None` and set the `executable` attribute to the name of the linter executable.

- Change the `regex` attribute to correctly capture the error output from the linter.

- Change the `multiline` attribute to `True` if the regex parses multiline error messages.

- Determine the minimum/maximum versions of the linter executable that will work with your plugin and change the `version_args`, `version_re` and `version_requirement` attributes accordingly.

- If the linter executable does not accept input via `stdin`, set the `tempfile_suffix` attribute to the filename suffix of the temp files that will be created.

These are the minimum requirements to make a linter plugin functional. However, depending on the features of the linter executable, you may need to configure other class attributes.

- If the linter outputs errors only on `stderr` or `stdout`, set `error_stream` to `util.STREAM_STDERR` or `util.STREAM_STDOUT` respectively.

- If you wish to support embedded syntaxes, set the `selectors` attribute accordingly.

- If the linter subclasses from `PythonLinter`, remove the `module` attribute if you do not plan to use the linter’s python API. If you do, you will need to implement the `check` method.

You should remove attributes that you do not change, as their values will be provided by the superclass.
