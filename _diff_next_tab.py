import sublime, sublime_plugin
import subprocess
class DiffCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		cur = num = 0
		# Получим массив всех view
		views = sublime.active_window().views()
		# Пройдемся по всем view в поисках активного, сравнивая по id
		for view in views:
			if view.id() == sublime.active_window().active_view().id():
				# Если id совпало, то запомним номер активного view
				cur = num
			num += 1
		# Проверим не является ли активный view последним
		if num-1 != cur:
			# Запустим программу meld с параметрами
			subprocess.Popen([
				'meld',
				views[cur].file_name(),
				views[cur+1].file_name()
			])
