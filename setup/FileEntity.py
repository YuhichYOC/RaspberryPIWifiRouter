import re


class FileEntity:

    def __init__(self):
        self.f_content = []
        self.f_path = ''

    @property
    def path(self) -> str:
        return self.f_path

    @property
    def content(self) -> list:
        return self.f_content

    @path.setter
    def path(self, arg: str):
        self.f_path = arg

    @content.setter
    def content(self, arg: list):
        self.f_content = arg

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
