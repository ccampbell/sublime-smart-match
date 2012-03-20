#!/usr/bin/env python

# Copyright 2012 Craig Campbell
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sublime, sublime_plugin

class SmartMatchCommand(sublime_plugin.TextCommand):
    def run(self, edit, character):
        for region in self.view.sel():
            if self.allowReplacement(region, character):
                self.replaceRegionWithString(edit, region, character)
                continue

            self.moveCursorForward(edit, region, character)

    def allowReplacement(self, region, character):
        if region.size() > 1:
            return True

        start_char = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        line = self.view.line(region)

        full_line_text = self.view.substr(line).strip()
        text_before_insertion = self.view.substr(sublime.Region(line.a, region.a)).strip()
        text_after_insertion = self.view.substr(sublime.Region(region.b, line.b)).strip()

        open_count_before = text_before_insertion.count(start_char[character])

        if open_count_before == 0:
            return True

        close_count_before = text_before_insertion.count(character)

        close_count = full_line_text.count(character)

        if open_count_before <= close_count and close_count_before != open_count_before and len(text_after_insertion) and text_after_insertion[0] == character:
            return False

        return True

    def moveCursorForward(self, edit, region, character):
        new_region = sublime.Region(region.a, region.a + 1)
        self.replaceRegionWithString(edit, new_region, character)

    def replaceRegionWithString(self, edit, region, character):
        self.view.erase(edit, region)
        self.view.run_command('insert',  {"characters": character})
