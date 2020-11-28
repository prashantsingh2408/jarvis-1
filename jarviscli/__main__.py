import argparse
import sys

import main

if __name__ == '__main__':
    main.assert_python_version()

    parser = argparse.ArgumentParser('Generate metadata json file')
    parser.add_argument('--with-server', dest='enable_server', action='store_true')
    parser.add_argument('--with-gui', dest='enable_gui', action='store_true')
    parser.add_argument('--with-voice', dest='enable_voice', action='store_true')
    parser.add_argument('--without-voice', dest='disable_voice', action='store_true')
    parser.add_argument('--with-speech-recognition', dest='enable_speech_recognition',
                        action='store_true')
    parser.add_argument('--without-cli', dest='enable_cli',
                        action='store_false')
    parser.add_argument('CMD', type=str, nargs='*')
    args = parser.parse_args()
    sys.argv = sys.argv[0]

    jarvis = main.build_jarvis()
    main.start(args, jarvis)
