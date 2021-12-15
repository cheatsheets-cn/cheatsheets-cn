#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class CSTableProcessor(Preprocessor):
    def run(self, lines):
        new_lines = []

        flag_start = False
        flag_child_start = False
        flag_brief_start = False

        for line in lines:
            if line.strip() == ">cstable":
                line = line.replace(">cstable", '<table class="cs-table">')
                flag_start = True
            elif line.strip() == "<cstable":
                line = line.replace("<cstable", "</table>")
                flag_start = False
            elif flag_start:
                line = re.sub(">\| +", "<tr><td><pre>", line)
                line = re.sub(" +\|\| +", "</pre></td><td><pre>", line)
                line = re.sub(" +\|<", "</pre></td></tr>", line)

            new_lines.append(line)
        return new_lines


class CSTableExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.add("cstable", CSTableProcessor(), "_begin")


def makeExtension(**kwargs):
    return CSTableExtension(**kwargs)
