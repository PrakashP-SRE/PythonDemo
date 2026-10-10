# int: no decimal point, can be positive or negative
max_tokens  : int = 1024   # max LLM response length
max_retries : int = 3      # retry on failure
customer_id : int = 1001   # from customers.csv

print(type(max_tokens))    #
print(10 + 3)              # 13
print(10 // 3)             # 3  — floor division (drops remainder)
print(10 % 3)              # 1  — modulo (remainder only)

# float: has a decimal point
temperature : float = 0.2    # 0.0 = deterministic, 1.0 = creative
similarity  : float = 0.85   # RAG retrieval cutoff
price       : float = 205.21 # from products.csv

print(type(temperature))   # <class 'float'>
print(10 / 3)              # 3.333... — division always returns float

# str: any characters in single or double quotes — both identical
model_name    : str = "gpt-4o"
customer_name : str = "Danielle Johnson"
order_id      : str = "ORD-3042"

print(type(model_name))    # <class 'str'>
print(len(customer_name))  # 16 — number of characters

# bool: exactly two values — must be capitalised
stream_response : bool = True
is_verified     : bool = False

print(10 > 5)              # True  — comparisons return bool
print(3 == 7)              # False
print(type(True))          # <class 'bool'>

# None: represents 'not set yet' — check with  is None
api_key          = None   # loaded from .env later
pending_response = None   # LLM hasn't replied yet

print(pending_response is None)  # True  — correct way to check
print(type(None))                # <class 'NoneType'>

a = 10
print(id(a))   # id() shows the actual memory address Python chose
print(a)       # reads that address, prints 10

b = a          # b now points to the SAME address as a
print(id(a) == id(b))  # True — same object in memory

a = 10           # right side: 10. Stored as int.
b = a + 5        # right side: 10+5=15. Stored in b.
c = b * 2        # right side: 15*2=30. Stored in c.

# You can reassign any name to a different type
a = "hello"      # a now points to a str — Python allows this
print(a, type(a))

# str()
print(str(1024))       # '1024'
print(str(True))       # 'True'

# int() — truncates, does NOT round
print(int('1024'))     # 1024
print(int(3.9))        # 3  ← truncated, not 4

# float() — essential for env vars
print(float('0.2'))    # 0.2
print(float(10))       # 10.0

# bool() — falsy values
print(bool(0))         # False
print(bool(''))        # False — empty string
print(bool([]))        # False — empty list
print(bool('hello'))   # True  — non-empty

