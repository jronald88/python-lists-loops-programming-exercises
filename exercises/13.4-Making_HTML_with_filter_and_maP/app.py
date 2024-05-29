all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def general_li(colour):    
	return f"<li>{colour['label']}</li>" #returns the label inisde the string <li> etc.


def filter_colours(data):
	return data["sexy"]

sexy_colours = list(filter(filter_colours, all_colors))
#print(sexy_colours)
sexy_colours_HTML = list(map(general_li,sexy_colours))
print(sexy_colours_HTML)
