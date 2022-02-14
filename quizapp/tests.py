from quizapp import models

import json
import pytest
import os


# * This is in JSON format
TEST_QUIZZES = {
    "quizzes": {
        "Basic Programming Quiz": {
            "title": "Basic Programming Quiz",
            "questions": [
                {
                    "question": "What is an algorithm?",
                    "option1": "A series of instruction achieved to perform an objective",
                    "option2": "A fruit",
                    "option3": "A computer component",
                    "option4": "A piece of software",
                    "rightAnswer": "A series of instruction achieved to perform an objective",
                    "bonus": False,
                },
                {
                    "question": "What is a variable?",
                    "option1": "Something that changes",
                    "option2": "Something that does not changes",
                    "option3": "A computer component",
                    "option4": "An identifier to store a value in a computer program",
                    "rightAnswer": "An identifier to store a value in a computer program",
                    "bonus": False,
                },
                {
                    "question": "What is the most common reserved word for a conditional sequence?",
                    "option1": "An if",
                    "option2": "A for",
                    "option3": "A loop",
                    "option4": "A while",
                    "rightAnswer": "An if",
                    "bonus": False,
                },
                {
                    "question": "What is a loop?",
                    "option1": "An algorithm that changes over time",
                    "option2": "An algorithm that will repeat itself until a condition is met",
                    "option3": "A software concept",
                    "option4": "A software that will repeat itsel until a condition is met",
                    "rightAnswer": "An algorithm that will repeat itself until a condition is met",
                    "bonus": False,
                },
                {
                    "question": "How it is called a callable identified routine",
                    "option1": "An object",
                    "option2": "A class",
                    "option3": "A function",
                    "option4": "A module",
                    "rightAnswer": "A function",
                    "bonus": False,
                },
                {
                    "question": "Which one of these are programming languages?",
                    "option1": "Python, Nebraska, Lugano",
                    "option2": "C++, C, Assembly",
                    "option3": "HTML, CSS, Python",
                    "option4": "Python, 313, ABC",
                    "rightAnswer": "C++, C, Assembly",
                    "bonus": True,
                },
            ]
        },
        "Math quiz": {
            "title": "Math quiz",
            "questions": [
                {
                    "question": "What is the result of 2+2?",
                    "option1": "4",
                    "option2": "5",
                    "option3": "That is an invalid operation",
                    "option4": "2",
                    "rightAnswer": "4",
                    "bonus": False,
                },
                {
                    "question": "The divisor and dividend are",
                    "option1": "A divisor is somethings to split the equation, and the dividend is half of that number",
                    "option2": "The divisor is the number by which the dividend will be divided",
                    "option3": "They are mathematical functions",
                    "option4": "Two numbers that will be summed into a bigger number",
                    "rightAnswer": "The divisor is the number by which the dividend will be divided",
                    "bonus": False,
                },
                {
                    "question": "What is an equation?",
                    "option1": "A computer virus",
                    "option2": "An arithmetic operation",
                    "option3": "A statement that asserts the equality between two (or more) expressions",
                    "option4": "A statement to transform an arithmetic operation",
                    "rightAnswer": "A statement that asserts the equality between two (or more) expressions",
                    "bonus": False,
                },
                {
                    "question": "What are the natural numbers?",
                    "option1": "Hippie numbers",
                    "option2": "Those used for counting and ordering",
                    "option3": "Those that have a fractional part",
                    "option4": "A number that is found in nature",
                    "rightAnswer": "Those used for counting and ordering",
                    "bonus": False,
                },
                {
                    "question": "What is a rational number",
                    "option1": "A really smart number",
                    "option2": "A philosophic number",
                    "option3": "A fractional number or number with comma",
                    "option4": "A number used in a geometric expression",
                    "rightAnswer": "A fractional number or number with comma",
                    "bonus": False,
                },
                {
                    "question": "What is the opposite of a number?",
                    "option1": "The number with its sign inverted",
                    "option2": "The distance from that number to zero",
                    "option3": "The distance from that number to 216",
                    "option4": "The number inverted (i.e 32 and its opposite, 23)",
                    "rightAnswer": "The number with its sign inverted",
                    "bonus": False,
                },
                {
                    "question": "What is the absolute value of a number?",
                    "option1": "The distance from that number to zero",
                    "option2": "The distance from that number to its opposite",
                    "option3": "The distance from that number to \"a million\", hence the therm Absolute",
                    "option4": "A very confident number",
                    "rightAnswer": "The distance from that number to zero",
                    "bonus": False,
                },
                {
                    "question": "What is geometry?",
                    "option1": "Just shapez",
                    "option2": "The mathematics of shapes",
                    "option3": "The mathematics of the properties, measurement, and relationships of points, lines, angles, surfaces, and solids",
                    "option4": "A geologist doing telemetry",
                    "rightAnswer": "The mathematics of the properties, measurement, and relationships of points, lines, angles, surfaces, and solids",
                    "bonus": True,
                },
                
            ]
        }
    }
}

@pytest.mark.django_db
def test_quiz_create_from_json():
    file = "JSON_TEST_FILE.JSON"
    with open(file, "w") as fp:
        json.dump(TEST_QUIZZES, fp)

    quizzes = models.quizFromJson(file)

    # * Test Python object instance
    quiz_0 = TEST_QUIZZES["quizzes"]["Basic Programming Quiz"]
    quiz_1 = TEST_QUIZZES["quizzes"]["Math quiz"]

    # * Database Model Instance
    Quiz0 = quizzes[0]
    Quiz1 = quizzes[1]

    assert Quiz0.title == quiz_0["title"]
    assert Quiz1.title == quiz_1["title"]

    # * Access to the list without having troubles, and made all of this re-usable
    for question in quiz_0["questions"]:
        Question = models.Question.objects.get(question=question["question"])
        if Question:
            assert Question.option1 == question["option1"]
            assert Question.option2 == question["option2"]
            assert Question.option3 == question["option3"]
            assert Question.option4 == question["option4"]
            assert Question.rightAnswer == question["rightAnswer"]
            assert Question.bonus == question["bonus"]
        else:
            raise AssertionError(f'The question {question["question"]} do not exist')
    
    for question in quiz_1["questions"]:
        Question = models.Question.objects.get(question=question["question"])
        if Question:
            assert Question.option1 == question["option1"]
            assert Question.option2 == question["option2"]
            assert Question.option3 == question["option3"]
            assert Question.option4 == question["option4"]
            assert Question.rightAnswer == question["rightAnswer"]
            assert Question.bonus == question["bonus"]
        else:
            raise AssertionError(f'The question {question["question"]} do not exist')
    os.remove(file)


