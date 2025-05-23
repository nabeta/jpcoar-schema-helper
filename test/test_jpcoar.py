import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import jpcoar
import pytest

def test_resource_type_uri():
  assert jpcoar.resource_type_uri("test") == None
  assert jpcoar.resource_type_uri("article") == "http://purl.org/coar/resource_type/c_6501"
