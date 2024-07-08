import hashlib

def assert_equals(actual, expect):
  """
  Assert that actual == expect. If not, print the values and raise an AssertionError.

  Parameters:
  - actual (any): The actual value.
  - expect (any): The expected value.

  Raises:
  AssertionError: If actual != expect
  """

  if actual is None:
    actual = '<NONE>'
  if expect is None:
    expect = '<NONE>'

  if isinstance(actual, bytes):
    actual = actual.hex()
  if isinstance(expect, bytes):
    expect = expect.hex()

  if not isinstance(actual, str):
    actual = str(actual)

  if actual != expect:
    print(f"""
actual: {actual}
expect: {expect}
""")
    raise AssertionError("actual != expect")

def now():
  'Return the current date and time.'
  import datetime
  return datetime.datetime.now()

def seconds_since(dt):
  'Return the number of seconds since dt and now.'
  import datetime
  return (now() - dt).total_seconds()

def seconds_since_bytes(dt):
  'Return the number of seconds since dt and now as a 4-byte little-endian unsigned integer.'
  return int(seconds_since(dt)).to_bytes(4, 'little')

def hash(x):
  'Return the 512-bite Whirlpool hash of x'
  if isinstance(x, str):
    b = bytes(x, 'utf-8')
  else:
    b = x
  hasher = hashlib.sha512()
  hasher.update(b)
  return hasher.digest()


def ToUUINT(x):
  if not isinstance(x, int):
    raise ValueError("x must be an integer")
  if x < 0:
    raise ValueError("x must not be negative")

  if x < 0xFC:
    # A byte less than 0xFC
    return bytearray([x])

  if x <= 0xFFFF:
    # 0xFC + 2 bytes
    return bytearray([0xFC]) + x.to_bytes(2, 'little')

  if x <= 0xFFFFFFFF:
    # 0xFD + 4 bytes
    return bytearray([0xFD]) + x.to_bytes(4, 'little')

  if x <= 0xFFFFFFFFFFFFFFFF:
    # 0xFE + 8 bytes
    return bytearray([0xFE]) + x.to_bytes(8, 'little')

  # 0xFF
  raise NotImplementedError("x is too large")


def FromUUINT(bytes):
  if len(bytes) < 1:
    raise ValueError("bytes must not be empty")

  if bytes[0] < 0xFC:
    return bytes[0]

  if bytes[0] == 0xFC:
    return int.from_bytes(bytes[1:3], 'little')

  if bytes[0] == 0xFD:
    return int.from_bytes(bytes[1:5], 'little')

  if bytes[0] == 0xFE:
    return int.from_bytes(bytes[1:9], 'little')

  if bytes[0] == 0xFF:
    raise NotImplementedError("x is too large")

  raise ValueError("Invalid prefix")