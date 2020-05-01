import argparse
# Getting the parameters
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='HyperFlex API Monitoring Demo.')
    parser.add_argument('--hxip',
                        help='HyperFlex ip',
                        )
    parser.add_argument('--hxpasswd',
                        help='HyperFlex Cluster Password',
                        )
    parser.add_argument('--hxuser',
                        help='hx user name',
                        )
    parser.add_argument('--hxtoken',
                        help='HX API Token',
                        )

    return parser.parse_args(args)

