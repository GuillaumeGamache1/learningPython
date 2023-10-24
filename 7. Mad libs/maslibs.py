import random

storyStructure = {
    'adjective': 'Please enter an adjective: ',
    'verb': 'Please enter a verb: ',
    'noun': 'Please enter a noun: '
}

libs = [
            "Once upon a time, a {adjective} {noun} was walking through the forest and he/she {verb} in the presence of mother nature.",
            "For as long as he can remember Henry the {adjective} dwarf always wanted to {verb} a {noun}",
            "His name was {noun}, and was always {adjective} with animals, he would often {verb} in their presence"
]

def gather_answers(answer_type):
    user_answer = input(storyStructure[answer_type])
    return user_answer


def makeStory(adjective, verb, noun):
    template = random.choice(libs)
    story = template.format(adjective=adjective, noun=noun, verb=verb)
    print(story)

def main():
    adjective = gather_answers('adjective')
    verb = gather_answers('verb')
    noun = gather_answers('noun')
    makeStory(adjective, verb, noun)

main()

 