from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class GLua(Linter):
    cmd = 'glualint ${file} ${args}'
    regex = r'.+\.lua: \[?(?P<error>Error)?(?P<warning>Warning)\] line (?P<line>\d+), column (?P<col>\d+) - line \d+, column \d+: (?P<message>.+)'
    multiline = True
    defaults = {
        'selector': 'source.lua'
    }
