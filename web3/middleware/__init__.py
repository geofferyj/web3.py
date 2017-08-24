from __future__ import absolute_import
import functools

from .formatting import (  # noqa: F401
    construct_formatting_middleware,
)
from .pythonic import (  # noqa: F401
    pythonic_middleware,
)
from .attrdict import (  # noqa: F401
    attrdict_middlware,
)


def combine_middlewares(middlewares, web3, provider_request_fn):
    """
    Returns a callable function which will call the provider.provider_request
    function wrapped with all of the middlewares.
    """
    return functools.reduce(
        lambda request_fn, middleware: middleware(request_fn, web3),
        reversed(middlewares),
        provider_request_fn,
    )
