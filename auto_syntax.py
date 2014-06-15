import sublime, sublime_plugin, re

class AutoSyntax(sublime_plugin.TextCommand):
    def run(self, edit):
        s = self.read_first_line()
        lang = self.test_mode(s)
        if lang:
            self.set_syntax(lang)
        else: 
            lang = self.test_vim(s)
            if lang:
                self.set_syntax(lang)


    def read_first_line(self):
        v = self.view
        return v.substr(v.line(0))

    def test_syntax(self, r, s):
        m = re.search(r, s)
        if m:
            return m.group(1)
        else:
            return None

    def test_mode(self, s):
        r = '^\# \-\*\- mode\: (.*) \-\*\-$'
        return self.test_syntax(r, s)

    def test_vim(self, s):
        r = '^\# vi\: set ft\=(.*) \:$'
        return self.test_syntax(r, s)

    def set_syntax(self, lang):
        name = lang.capitalize()
        path = "Packages/" + name + "/" + name + ".tmLanguage"
        try:
            self.view.set_syntax_file(path)
        except:
            print("Cannot find syntax file for: " + lang)
            print("Tried: " + path)


class SyntaxListener(sublime_plugin.EventListener):
    def on_load_async(self, view):
        view.run_command("auto_syntax")
