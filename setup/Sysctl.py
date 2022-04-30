from . import FileEntity


class Sysctl:

    @staticmethod
    def rewrite_for_bridge() -> None:
        target = FileEntity.FileEntity()
        target.path = '/etc/sysctl.conf'
        target.content_replace_regexp('templates/etc/sysctl.conf')
        return None

    def run(self) -> None:
        self.rewrite_for_bridge()
        return None
