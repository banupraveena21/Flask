# Fun Fact Generator by Animal
'''
Requirements:
• /fact/<animal> returns a fun fact (from dictionary) for that animal.
• /fact/list lists all available animals.
• Return response in colorful HTML with <ul> and <li>.
'''


from flask import Flask

app = Flask(__name__)

fun_facts = {
    "dog": "Dogs have an extraordinary sense of smell, about 40 times better than humans!",
    "cat": "Cats can rotate their ears 180 degrees thanks to 32 muscles in each ear.",
    "elephant": "Elephants are the only mammals that can't jump.",
    "dolphin": "Dolphins have names for each other and respond to them.",
    "owl": "Owls can rotate their heads up to 270 degrees."
}

@app.route("/fact/list")
def list_animals():
    animals = fun_facts.keys()
    animal_list = "".join(f"<li>{animal.capitalize()}</li>" for animal in animals)

    return f"""
    <h2 style="color:darkgreen;">Available Animals for Fun Facts</h2>
    <ul style="font-size:18px; color:#555;">
        {animal_list}
    </ul>
    """

@app.route("/fact/<animal>")
def animal_fact(animal):
    fact = fun_facts.get(animal.lower())
    if fact:
        return f"""
        <h2 style="color:navy;">Fun Fact About {animal.capitalize()}</h2>
        <p style="font-size:18px; color:#333;">{fact}</p>
        """
    else:
        return f"""
        <h2 style="color:red;">Sorry!</h2>
        <p>We don't have a fun fact for <strong>{animal}</strong>.</p>
        <p>Check the available animals at <a href="/fact/list">/fact/list</a></p>
        """

if __name__ == "__main__":
    app.run(debug=True)