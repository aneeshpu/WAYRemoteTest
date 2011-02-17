from latitude import OAuth
import unittest

class OAuthTest(unittest.TestCase):
  def test_how_to(self):
    print "inside test how to"
    oauth = OAuth.OAuthWay(None)
    oauth.authorize()

if __name__ == "__main__":
  unittest.main()
    
