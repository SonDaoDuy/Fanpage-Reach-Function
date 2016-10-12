import codecs
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.data = []

  def handle_starttag(self, tag, attributes):
    if tag != 'div':
      return
    if self.recording:
      self.recording += 1
      return
    for name, value in attributes:
      if name == 'class' and value == '_5kn2':
        break
    else:
      return
    self.recording = 1

  def handle_endtag(self, tag):
    if tag == 'div' and self.recording:
      self.recording -= 1

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)

f = codecs.open("data.html",'r')
target = codecs.open("getdata.txt",'w')
data = f.read()
f.close()
parser = MyHTMLParser()
parser.feed(data)
print parser.data
i = 0
for number in parser.data:
    target.write(number)
    i = i + 1
    if(i >=4):
        target.write('\n')
        i = 0
    else:
      target.write(' ')
target.close()
#tags = parser.handle_starttag('div',[('class','_5kn3 ellipsis')])

# for tag in tags:
#     list.append(parser.get_starttag_text())

# print list