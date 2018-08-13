import os
import platform
import tempfile

from SublimeLinter.lint import Linter

if platform.system() == "Windows":
    GROOVY_BINARY = 'groovyc.bat'
    CLASSPATH_DIVIDER = ';'
else:
    GROOVY_BINARY = "groovyc"
    CLASSPATH_DIVIDER = ':'

class Groovy(Linter):

    tempfile_suffix = "-"

    regex = r'''(?sx)(.*?:\ # Filepath part
                \d+:\ # Line part, we ignore it as we have it later
                (?P<message>.*?)\s* # Error message till @
                @\ line\ (?P<line>\d+),\ column\ (?P<col>\d+)\. # line and column, ends with dot
                ''' \
                '{}'.format(os.linesep) +\
                r'''\s*(?P<code>.*?)\n # Second line - will be whole code snippet of error, it has to ends with unix newline
                ''' \
                r'|.*) # The last resort match - if we do not match error, match anything to silence info from SL'

    multiline = True

    defaults = {
        'classpath': None,
        'sourcepath': None,
        'selector': 'source.groovy',
    }

    on_stderr = None

    def cmd(self):
        cmd = (GROOVY_BINARY,)
        settings = self.get_view_settings()
        # pylint: disable=attribute-defined-outside-init
        self._tempdir = tempfile.TemporaryDirectory(prefix="sublimelinter-contrib-groovyc-target-")

        classpaths = []
        classpaths.append(settings.get('classpath') or '')
        classpaths.append(self._tempdir.name)

        classpath_str = '"{}'.format(CLASSPATH_DIVIDER) + '{}"'.format(CLASSPATH_DIVIDER.join(classpaths))
        cmd += ('-classpath', classpath_str)

        for opt in ('sourcepath',):
            value = settings.get(opt)
            if value is not None:
                cmd += ('--{}'.format(opt), '"{}"'.format(value),)

        cmd += ('-d', '"{}"'.format(self._tempdir.name))
        return cmd

    def run(self, cmd, code=None):
        with self._tempdir:
            return super().run(cmd, code)

    def split_match(self, match):
        match, line, col, error, warning, message, near = super().split_match(match)

        if line is None:
            return match, 0, 0, None, None, None, None
        return match, line, col, error, warning, message, near
