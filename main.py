from random import choice
from pyscript.web import page
from pyscript import when

characters = ['an apple', 'a cat', 'a dragon', 'a fairy', 'a firefighter', 'me', 'a monarch', 'a mushroom', 'a pizza', 'a robot', 'a scientist', 'a unicorn']
locations = ['a boat', 'a cave', 'a computer', 'a factory', 'the future', 'outer space', 'a parallel universe', 'the past', 'a science centre', 'a shop', 'a thunder storm', 'the woods']
styles = ['an adventurous', 'a confusing', 'a dramatic', 'an exciting', 'a fantastical', 'a funny', 'a happy', 'a mysterious', 'a predictable', 'a romantic', 'a scary', 'a strange']

@when("click", "#run")
def story():
    input_character = page.find("#character")[0]
    character = input_character.value
    if not character:
        character = choice(characters)
        
    input_location = page.find("#location")[0]
    location = input_location.value
    if not location:
        location = choice(locations)
    
    input_style = page.find("#style")[0]
    style = input_style.value
    if not style:
        style = choice(styles)
    
    output_div = page.find("#output")[0]
    output_div.innerText = ("This story is about " + character + " in " + location + "." +"\n" + "It is " + style + " story."+ "\n" + "\n")
