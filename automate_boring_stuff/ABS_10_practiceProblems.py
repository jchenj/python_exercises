#AWS_10_practiceProblems
"""1. Write an assert statement that triggers an AssertionError
if the variable spam is an integer less than 10."""

assert spam >= 10, "The spam variable is less than 10!"

# Learning: Make sure to understand the task correctly & fully.

"""2. Write an assert statement that triggers an AssertionError if the variables
eggs and bacon contain strings that are the same as each other, even if their
cases are different (that is, 'hello' and 'hello' are considered the same, and
'goodbye' and 'GOODbye' are also considered the same)."""

assert eggs.lower() != bacon.lower(), "The eggs and bacon variables are the same!"
"""Learning: In string to display when condition false, call attention to error,
rather than restrate condition."""

"""3. Write an assert statement that always triggers an AssertionError."""
assert spam != spam, "Spam is equal to spam!"
"""Learning: Answer from book: assert False, "This assertion always triggers."""

"""4. What are the two lines that your program must have in order to be able to
call logging.debug()?"""

