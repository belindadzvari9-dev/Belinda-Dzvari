#2. Event Dispatcher Using the Observer Pattern
class EventDispatcher:
    def __init__(self):
        # Stores event names and their callback functions.
        self.subscribers = {}

    def subscribe(self, event_type, callback):
        # Create an empty list for a new event.
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []

        # Add the callback to the event list.
        self.subscribers[event_type].append(callback)

    def unsubscribe(self, event_type, callback):
        # Remove the callback if it exists.
        if event_type in self.subscribers:
            if callback in self.subscribers[event_type]:
                self.subscribers[event_type].remove(callback)

    def dispatch(self, event_type, *args, **kwargs):
        # Do nothing if nobody subscribed to this event.
        if event_type not in self.subscribers:
            return

        # Run callbacks in the order they were added.
        for callback in self.subscribers[event_type]:
            try:
                callback(*args, **kwargs)
            except Exception as error:
                # An error in one callback must not stop the next one.
                print("Error:", error)


# Example callback functions
def send_email(name):
    print("Email sent to", name)

def save_log(name):
    print("Log saved for", name)

# Create dispatcher and register callbacks
dispatcher = EventDispatcher()
dispatcher.subscribe("user_registered", send_email)
dispatcher.subscribe("user_registered", save_log)

# Trigger the event
dispatcher.dispatch("user_registered", "Alice")
#Expected output:
#Email sent to Alice
#Log saved for Alice
