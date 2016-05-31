from coalib.bearlib.abstractions.Linter import linter
from coalib.settings.Setting import typed_list
from coalib.bears.requirements.PipRequirement import PipRequirement


@linter(executable='bandit',
        output_format='regex',
        output_regex=r'(?P<message>(?P<origin>(?:B\d+[,-]?)+): .*)')
class BanditBear:
    """
    Performs security analysis on Python source code, utilizing the ast module
    from the Python standard library.
    """
    LANGUAGES = {"Python", "Python 2", "Python 3"}
    REQUIREMENTS = {PipRequirement('bandit', '1.1')}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Security'}

    @staticmethod
    def create_arguments(filename, file, config_file,
                         bandit_skipped_tests: typed_list(str)=
                         ("B105", "B106", "B107", "B404", "B603", "B606",
                          "B607")):
        """
        :param bandit_skipped_tests:
            The IDs of the tests bandit shall not perform. You can get
            information about the available builtin codes at
            https://github.com/openstack/bandit#usage.
        """
        args = (filename, '-f', 'json')  # TODO

        if bandit_skipped_tests:
            args += ("-s", ",".join(bandit_skipped_tests))

        return args
