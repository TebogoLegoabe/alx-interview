#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
  """
  Checks if a list of integers represents a valid UTF-8 encoding.

  Args:
      data: A list of integers representing bytes in the data set.

  Returns:
      True if the data is valid UTF-8, False otherwise.
  """
  lead_bytes = 0
  for byte in data:
    byte &= 0xFF

    if lead_bytes > 0:
      if 0x80 <= byte <= 0xBF:
        lead_bytes -= 1
      else:
        return False
    else:
      if 0xC0 <= byte <= 0xDF:
        lead_bytes = 1
      elif 0xE0 <= byte <= 0xEF:
        lead_bytes = 2
      elif 0xF0 <= byte <= 0xF7:
        lead_bytes = 3
      else:
        if byte < 0x80:
          lead_bytes = 0
        else:
          return False

  return lead_bytes == 0
