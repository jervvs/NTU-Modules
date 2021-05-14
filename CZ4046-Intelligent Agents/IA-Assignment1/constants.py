# CONSTANTS USED
## STATES - GRID ENVRIONMENT
GRID = [
    ['G', 'W', 'G', ' ', ' ', 'G'],
    [' ', 'O', ' ', 'G', 'W', 'O'],
    [' ', ' ', 'O', ' ', 'G', ' '],
    [' ', ' ', ' ', 'O', ' ', 'G'],
    [' ', 'W', 'W', 'W', 'O', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
]

## REWARD FUNCTION
REWARD_MAP = {
    ' ': -0.04,  # white square
    'G': 1.0,  # green square
    'O': -1.0  # orange square
}

## DISCOUNT
DISCOUNT = 0.99

## VALUE ITERATION CONSTANT(S)
EPSILON = 1 # maximum error allowed in the utility of any state

## POLICY ITERATION CONSTANT(S)
K = 5


