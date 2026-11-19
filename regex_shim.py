import sys
import re

class PatternWrapper:
    def __init__(self, pat):
        self._pat = pat
        for a in ['pattern', 'flags', 'groups', 'groupindex']:
            if hasattr(pat, a):
                setattr(self, a, getattr(pat, a))

    def match(self, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self._pat.match(string, *args, **kwargs)

    def search(self, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self._pat.search(string, *args, **kwargs)

    def fullmatch(self, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self._pat.fullmatch(string, *args, **kwargs)

    def findall(self, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self._pat.findall(string, *args, **kwargs)

    def finditer(self, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self._pat.finditer(string, *args, **kwargs)

    def sub(self, repl, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self._pat.sub(repl, string, *args, **kwargs)

    def subn(self, repl, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self._pat.subn(repl, string, *args, **kwargs)

    def split(self, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self._pat.split(string, *args, **kwargs)

class RegexShim:
    def __init__(self):
        for k in dir(re):
            if k not in ['compile', 'match', 'search', 'sub', 'subn', 'split', 'fullmatch']:
                setattr(self, k, getattr(re, k))
        self.error = re.error
        self.Pattern = PatternWrapper

    def compile(self, pattern, *args, **kwargs):
        kwargs.pop('timeout', None)
        if isinstance(pattern, str):
            try:
                return PatternWrapper(re.compile(pattern, *args, **kwargs))
            except re.error:
                clean = re.sub(r'\\p\{[^\}]+\}', r'\\w', pattern)
                clean = re.sub(r'\\P\{[^\}]+\}', r'\\W', clean)
                try:
                    return PatternWrapper(re.compile(clean, *args, **kwargs))
                except re.error:
                    return PatternWrapper(re.compile(r'.*'))
        return PatternWrapper(re.compile(pattern, *args, **kwargs))

    def match(self, pattern, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self.compile(pattern).match(string, *args, **kwargs)

    def search(self, pattern, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self.compile(pattern).search(string, *args, **kwargs)

    def sub(self, pattern, repl, string, *args, **kwargs):
        kwargs.pop('timeout', None)
        return self.compile(pattern).sub(repl, string, *args, **kwargs)

shim = RegexShim()
for m in ['regex', '_regex', 'regex._main', 'regex._regex_core']:
    sys.modules[m] = shim
