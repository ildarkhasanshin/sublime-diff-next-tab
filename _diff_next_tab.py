import sublime, sublime_plugin
import subprocess

class DiffCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    cur = num = 0
    views = sublime.active_window().views()

    for view in views:
      if view.id() == sublime.active_window().active_view().id():
        cur = num
      num += 1

    if num-1 != cur:
      subprocess.Popen([
        'meld',
        views[cur].file_name(),
        views[cur+1].file_name()
      ])