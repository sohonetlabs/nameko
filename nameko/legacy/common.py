import arrow
import uuid


UIDGEN = lambda: uuid.uuid4().hex
UTCNOW = lambda: arrow.utcnow().datetime
