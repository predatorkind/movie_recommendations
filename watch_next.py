import spacy


def find_recommendation(description):
    """
    finds a movie recommendation in 'movies' list based on passed in description
    :param description: description of an input movie
    :return: recommended movie from the 'movies' list
    """
    # create a spacy program and a model of the input sentence
    nlp = spacy.load('en_core_web_md')
    model_description = nlp(description)

    # loop through movie list and find one with the highest similarity to the one in model_description
    highest_similarity = 0
    recommended_movie = ""
    for movie in movies:
        similarity = nlp(movie).similarity(model_description)
        print(movie[:7] + " - ", similarity)
        if similarity > highest_similarity:
            highest_similarity = similarity
            recommended_movie = movie

    return recommended_movie


def read_movies(file):
    """
    read movie list with descriptions from file
    :param file: input file with movie descriptions
    :return: list of movie descriptions
    """
    # read in movie list from file
    movies = []
    try:
        with open(file, "r") as f:
            for movie in f.readlines():
                movie = movie.replace("\n", "")
                movies.append(movie)
    except FileNotFoundError:
        print(f"{file} not found. Terminating program.")
        exit()

    return movies


# ========================================
# read in movie list
movies = read_movies("movies.txt")

# declare a variable with input movie description
planet_hulk = "Will he save their world or destroy it? when the Hulk becomes too dangerous for the Earth," \
              "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live" \
              "in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as" \
              "as a gladiator."

# display movie recommendation
print(f"\nYour recommendation:\n{find_recommendation(planet_hulk)}")


# word1 = nlp("cat")
# word2 = nlp("monkey")
# word3 = nlp("banana")
#
# print(word1.similarity(word2))
# print(word3.similarity(word2))
# print(word3.similarity(word1))
# print("")
#
#
# # tokens = nlp("cat apple monkey banana")
#
# # unknown words do not have a valid word vector and do not produce a meaningful result
# tokens = nlp("python java kotlin")
#
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))
#
# sentence_to_compare = "Why is my cat on the car"
#
# sentences = ["Where did my dog go",
#              "Hello, there is my car",
#              "I've lost my car in my car",
#              "I'd like my boat back",
#              "I will name my dog Diana"]
#
# model_sentence = nlp(sentence_to_compare)
#
# print(f"\n{sentence_to_compare}")
# for sentence in sentences:
#     similarity = nlp(sentence).similarity(model_sentence)
#     print(sentence + " - ", similarity)
