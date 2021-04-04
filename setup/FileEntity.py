import re


class FileEntity:

    def __init__(self):
        self.f_content = []
        self.f_path = ''
        self.f_regexp_replace_file_pattern_indicator = 'pattern:'
        self.f_regexp_replace_file_replacement_indicator = 'replacement:'

    @property
    def path(self) -> str:
        return self.f_path

    @property
    def content(self) -> list:
        return self.f_content

    @property
    def regexp_replace_file_pattern_indicator(self) -> str:
        return self.f_regexp_replace_file_pattern_indicator

    @property
    def regexp_replace_file_replacement_indicator(self) -> str:
        return self.f_regexp_replace_file_replacement_indicator

    @path.setter
    def path(self, arg: str):
        self.f_path = arg

    @content.setter
    def content(self, arg: list):
        self.f_content = arg

    @regexp_replace_file_pattern_indicator.setter
    def regexp_replace_file_pattern_indicator(self, arg: str):
        self.f_regexp_replace_file_pattern_indicator = arg

    @regexp_replace_file_replacement_indicator.setter
    def regexp_replace_file_replacement_indicator(self, arg: str):
        self.f_regexp_replace_file_replacement_indicator = arg

    def read(self) -> None:
        self.content = []
        with open(self.path, 'r') as f:
            lines = f.read().split('\n')
            for line in lines:
                self.content.append(line)
        return None

    def write(self) -> None:
        with open(self.path, 'w') as f:
            for line in self.content:
                f.write(line)
                f.write('\n')
        return None

    def rewrite(self, content: list) -> None:
        fe = FileEntity()
        fe.path = self.path
        fe.content = content
        fe.write()
        return None

    def append(self, content: list) -> None:
        fe = FileEntity()
        fe.path = self.path
        fe.read()
        fe.content.extend(content)
        fe.write()
        return None

    def replace_regexp(self, pattern: str, replacement: str) -> None:
        fe = FileEntity()
        fe.path = self.path
        fe.read()
        l_p = re.compile(pattern)
        new_content = []
        for line in fe.content:
            l_m = l_p.match(line)
            if l_m is not None:
                new_content.append(replacement)
            else:
                new_content.append(line)
        fe.content = new_content
        fe.write()
        return None

    def content_replace(self, pattern: str, replacement: str) -> None:
        self.content = list(map(
            lambda line:
            line.replace(pattern, replacement),
            self.content
        ))
        return None

    def content_replace_regexp(self, pattern_file_path: str) -> None:
        patterns = FileEntity()
        patterns.path = pattern_file_path
        patterns.read()
        pattern_from = len(self.regexp_replace_file_pattern_indicator)
        for item in patterns.content:
            pattern_to = item.find(self.regexp_replace_file_replacement_indicator)
            replacement_from = \
                item.find(self.regexp_replace_file_replacement_indicator) + \
                len(self.regexp_replace_file_replacement_indicator)
            pattern = item[pattern_from:pattern_to]
            replacement = item[replacement_from:]
            self.replace_regexp(pattern, replacement)
        return None
