def display_message():
    """Simple function program"""
    print("I am learning about functions in python")
display_message()


def favourite_book(title):
    """passing one parameter"""
    print(f"One of my favourite books is {title.title()}")
    
favourite_book("splinter cell: checkmate")


def make_shirt(size, message):
    """Printing out shirts with messages"""
    print(f"The shirt of size {size.title()} has the message {message.title()}")
    
make_shirt('large', 'i love python')


def make_shirts(message, size='large'):
    """one parameter is default"""
    print(f"The {size.title()} sized shirt has the message {message.title()}")

make_shirts('i love python')

def describe_city(city, country):
    """printing out city and country"""
    print(f"{city.title()} is in {country.title()}")

describe_city('reykjavik', 'iceland')
describe_city('nairobi', 'kenya')
describe_city('london', 'united kingdom')

def city_country(city, country= 'kenya'):
    """printing out city and country again"""
    print(f"{city.title()}, {country.title()}")

print(city_country('nairobi', 'kenya'))
print(city_country('nakuru', 'kenya'))
print(city_country('paris', 'france'))


def make_album(artist_name, album_title, tracks=None):
    """returning album dictionary"""
    album_name = {'artist': artist_name, 'album': album_title, 'tracks': tracks}
    return album_name

while True:
    print("\nEnter album information: ")
    print("Enter 'q' to quit")
    
    artist = input("Artist name: ")
    if artist == 'q':
        break
    album = input("Album name: ")
    if album == 'q':
        break
    track = input("Enter tracks: ")
    if track == 'q':
        break
    album_name = make_album(artist, album, track)
    print(album_name)
print(make_album('kendrick lamar', 'gnx'))
print(make_album('the off season', 'j.cole', 13))



def show_magicians():
    """display a list of magicians"""
    for name in names:
        print(f"{name.title()}")
    
names = ['dynamo', 'chirs angel', 'mikey']
show_magicians()

def make_great():
    """adding the name Great to magicians names"""
    for name in names:
        print(f"Great{name.title()}")
        
names = ['dynamo', 'chirs angel', 'mikey']
make_great()

def sandwich_ingredients(*args):
    """priniting sandwich ingredients"""
    print("\nThese are sandwich ingredients")
    for arg in args:
        print(F"- {arg}")
        
    sandwich_ingredients()
    sandwich_ingredients('Sliced white', 'whole wheat', 'rye', 'multigrain bread')
    
