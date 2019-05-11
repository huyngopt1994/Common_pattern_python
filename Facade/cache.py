from datetime import timedelta, datetime
import pickle


class Cache(object):
    """Build Caching layer to store information to disk storage with expiration time is 3 hour."""

    def __init__(self, filename):
        self.filename = filename

    def save(self, obj):
        with open(self.filename, 'w') as f:
            dct = {
                'obj': obj,
                'expired': datetime.utcnow() + timedelta(hours=3)
            }
            pickle.dump(dct, f)

    def load(self):
        try:
            with open(self.filename) as f:
                result = pickle.load(f)
                if result['expired'] > datetime.utcnow():
                    return result['obj']
        except IOError:
            pass
