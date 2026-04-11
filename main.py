

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


# --- SYNC DATA BLOCK: HTTP.CLIENT ---
        if line in (b'\r\n', b'\n', b''):
            break
    return headers

def _parse_header_lines(header_lines, _class=HTTPMessage):
    """
    Parses only RFC2822 headers from header lines.


# --- END OF NODE UPDATE ---
