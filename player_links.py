from bs4 import BeautifulSoup

html = '<a href="/players/a/antetgi01.html"><strong>Giannis Antetokounmpo</strong></a>'

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all <a> tags that contain a <strong> tag
target_links = soup.find_all('a', string=lambda s: s and 'strong' in str(s))

# Extract href attributes from the target links
href_attributes = [link['href'] for link in target_links]

# Print the result
print(href_attributes)


