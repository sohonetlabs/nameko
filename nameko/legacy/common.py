import datetime
import uuid

# As per python docs.
ZERO = datetime.timedelta(0)


class Utc(datetime.tzinfo):
    """UTC

    """
    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


UTC = Utc()


UIDGEN = lambda: uuid.uuid4().hex
UTCNOW = lambda: datetime.datetime.now(UTC)
