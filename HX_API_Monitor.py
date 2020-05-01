'''
HX API Monitoring
'''

import hx_api
import hx_args
import sys
import getpass

################################# L O C A L   F U N C T I O N S ##########################


################## M A I N ###################
args = hx_args.check_arg(sys.argv[1:])
hxiparg = args.hxip
hxuserarg = args.hxuser
hxpasswdarg = args.hxpasswd
hxtokenarg = args.hxtoken

if args.hxip == None:
    hxip = input("HyperFlex IP Address: ")

if args.hxuser == None:
    hxuser = input("HyperFlex UserName: ")

if args.hxpasswd == None:
    hxpasswd = getpass.getpass("Please enter the HyperFLex Password: ")

hx = hx_api.HX_API(hxiparg,hxuserarg,hxpasswdarg,hxtokenarg)

if args.hxtoken == None:
    # Get the Token.
    hx.get_hxtoken()
else:
    print ('Verify Token!')

cluster_uuid = hx.get_cuuid()
print ('Cluster uuid: ',cluster_uuid)

