import os

import toolcli

from .. import config_data
from .. import config_read
from .. import config_values


def setup_data_root() -> tuple[str, bool]:

    print()
    print()
    print('## Data Root Directory')

    input_kwargs: toolcli.InputFilenameOrDirectoryKwargs = {
        'prompt': 'Where should ctc store data? (specify a directory path)\n> ',
        'create_directory': 'prompt_and_require',
    }

    # data_root
    if not config_read.config_path_exists or not config_read.config_is_valid():
        print()
        new_data_root = toolcli.input_filename_or_directory(**input_kwargs)
        create_new_config = True

    else:
        old_data_root = config_values.get_data_root_directory()
        print()
        print('Data directory currently set to:', old_data_root)

        if not isinstance(old_data_root, str):
            print()
            print('This value is invalid')
            print()
            new_data_root = toolcli.input_filename_or_directory(**input_kwargs)
            create_new_config = True

        elif os.path.abspath(old_data_root) != old_data_root:
            print()
            print('This path should be an absolute path')
            print()
            print('Absolute path:', os.path.abspath(old_data_root))
            print()
            if toolcli.input_yes_or_no('Use this path for data directory?'):
                new_data_root = old_data_root
                create_new_config = False
            else:
                print()
                new_data_root = toolcli.input_filename_or_directory(
                    **input_kwargs
                )
                create_new_config = True

        else:
            print()
            if toolcli.input_yes_or_no('Keep storing data in this directory?'):
                new_data_root = old_data_root
                create_new_config = False
            else:
                new_data_root = toolcli.input_filename_or_directory(
                    **input_kwargs
                )
                create_new_config = True

    # initialize directory data
    if config_data.is_data_root_initialized(new_data_root):
        print()
        print('Data directory is already initialized')
    else:
        initialized = config_data.initialize_data_root(new_data_root)
        if not initialized:
            return setup_data_root()

    return new_data_root, create_new_config

