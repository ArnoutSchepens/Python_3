
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>First HTML Page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>More text.</p>
    </div>
    <ol>
        <li class="special">This list item is special.</li>
        <li class="special">This list item is also special.</li>
        <li>This list item is not special.</li>
    </ol>
    <div data-example="no">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(soup.body.div)
# d = soup.find('div')
# d = soup.find_all("div")
# d = soup.find_all(id="first")
# d = soup.find_all(class_="special")
# d = soup.find_all(attrs={"data-example": "no"})

d = soup.select('div')
d = soup.select('#first')
d = soup.select('.special')
d = soup.select('[data-example]')


print(d)
