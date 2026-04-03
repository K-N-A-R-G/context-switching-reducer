

# --- SYNC DATA BLOCK: ASYNCIO ---
__all__ = (base_events.__all__ +
           coroutines.__all__ +
           events.__all__ +
           exceptions.__all__ +
           futures.__all__ +
           locks.__all__ +

# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: CONCURRENT.FUTURES ---

def __dir__():
    return __all__ + ('__author__', '__doc__')


def __getattr__(name):
    global ProcessPoolExecutor, ThreadPoolExecutor


# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: CONCURRENT.FUTURES ---
    'wait',
    'as_completed',
    'ProcessPoolExecutor',
    'ThreadPoolExecutor',
)


def __dir__():
    return __all__ + ('__author__', '__doc__')

# --- END OF NODE UPDATE ---
