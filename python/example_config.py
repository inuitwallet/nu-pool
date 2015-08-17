import os

# pool configuration
_port = 3333
# daily interest rates
_interest = {
    'bittrex': {
        'btc': {
            'bid': {
                'rate': 0.001,
                'target': 500.0
            },
            'ask': {
                'rate': 0.001,
                'target': 500.0
            }
        }
    }
}

_nuconfig = '%s/.nu/nu.conf' % os.getenv("HOME")  # path to nu.conf
_tolerance = 0.0085  # price tolerance
_sampling = 6  # number of requests validated per minute
_autopayout = False  # try to send payouts automatically
_minpayout = 0.1  # minimum balance to trigger payout
_grantaddress = ""  # custodian grant address
_master = ""
_slaves = []
