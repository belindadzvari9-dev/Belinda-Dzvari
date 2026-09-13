#Bug 1 — UnboundLocalError
#Because calls is assigned inside wrapper:
#calls = [t for t in calls if now - t < period]
#Python therefore treats calls as a local variable throughout wrapper.
# The right-hand side tries to read that local variable before it has been assigned, raising UnboundLocalError.

#Adding nonlocal calls would fix that specific scoping issue.

#Bug 2 — instances share one rate-limit state
#A decorator is applied once, at class-definition time.
# A single closure-level calls list would therefore be shared by every instance of that class.
# To give each instance its own limit, keep timestamp queues in a mapping keyed by the instance (ideally a WeakKeyDictionary, to avoid retaining discarded instances).

# Corrected, thread-safe decorator
import time
import threading
import weakref
from collections import deque
from functools import wraps

# iii. Corrected code
import time
from functools import wraps

def rate_limit(max_calls, period, per_instance=False):
    def decorator(func):
        calls = {}  # Stores call times

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use one shared limit by default.
            key = "shared"

            # For class methods, give each object its own limit.
            if per_instance and args:
                key = id(args[0])

            if key not in calls:
                calls[key] = []

            now = time.time()

            # Keep only calls made inside the time period.
            calls[key] = [t for t in calls[key] if now - t < period]

            if len(calls[key]) >= max_calls:
                raise Exception("Rate limit exceeded")

            calls[key].append(now)
            return func(*args, **kwargs)

        return wrapper
    return decorator


@rate_limit(max_calls:=3, period:=10)
def fetch_user_data(user_id):
    return f"Data for {user_id}"

print(fetch_user_data(1))
for a in [1,2,3]:
    print(a)
@rate_limit(max_calls:=3, period:=10)
class UserService:
    @rate_limit(max_call:=3, period:=10, per_instance:=True)
    def fetch_data(self):
        return "User data"







