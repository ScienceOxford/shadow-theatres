from random import choice

characters = ['an apple', 'a cat', 'a dragon', 'a fairy', 'a firefighter', 'me', 'a monarch', 'a mushroom', 'a pizza', 'a robot', 'a scientist', 'a unicorn']
locations = ['a boat', 'a cave', 'a computer', 'a factory', 'the future', 'outer space', 'a parallel universe', 'the past', 'a science centre', 'a shop', 'a thunder storm', 'the woods']
styles = ['an adventurous', 'a confusing', 'a dramatic', 'an exciting', 'a fantastical', 'a funny', 'a happy', 'a mysterious', 'a predictable', 'a romantic', 'a scary', 'a strange']

def story():
    input_character = Element("character")
    character = input_character.element.value
    if not character:
        character = choice(characters)
        
    input_location = Element("location")
    location = input_location.element.value
    if not location:
        location = choice(locations)
    
    input_style = Element("style")
    style = input_style.element.value
    if not style:
        style = choice(styles)
    
    output_div = Element("output")
    output_div.element.innerText = ("This story is about " + character + " in " + location + "." +"\n" + "It is " + style + " story."+ "\n" + "\n")
