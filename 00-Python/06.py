"""
A module for building quiz applications. It provides funtionality for storing questions and
accessing them in a randomly shuffled manner.
"""

import string
from typing import List, Tuple
from random import shuffle

class Question:
    """
    A class for storing a single question and its answers.
    
    Attributes:
    str question_text: The text of the question
    list(str) answers: A list of possible answers
    """
    def __init__(self, question_text: str, answers: List[str], correct_answers: List[int]) -> None:
        """
        Creates a new question object.
        
        :param question_text: The question itself, that will be asked
        :param answers: A list of possible answers, that should be displayed
        :param correct_answers: A list of indices, that indicate correct anwers in the `answers`
        list. Must contain at least one element.
        """
        self.question_text = question_text
        self.answers = answers
        self._correct_answers = tuple(correct_answers)

    def shuffle(self) -> None:
        """
        Randomizes the order of the question's possible answers
        """
        shuffle_indices = list(range(len(self.answers)))
        shuffle(shuffle_indices)
        correct_answers = []
        shuffled_answers = ['']*len(self.answers)
        for original_index, new_index in enumerate(shuffle_indices):
            shuffled_answers[new_index] = self.answers[original_index]
            if original_index in self._correct_answers:
                correct_answers.append(new_index)
        self.answers = shuffled_answers
        self._correct_answers = tuple(sorted(correct_answers))

    def answer(self, selected_answer: List[int]) -> Tuple[bool, List[int]]:
        """
        Returns a tuple containing a boolean value whether the selected answers are the correct ones
        or not, as well as a list containing the the correct answer indices.
        
        :param selected_answer: A list of indices, that correspond to answers of the Question's
        answer attribute.
        :returns: Tuple of bool and a List of indices
        """
        return (tuple(sorted(selected_answer)) == self._correct_answers, self._correct_answers)

class QuizMaster:
    """
    A class for storing multiple questions and accessing them in a randomly shuffled order.
    Quizmaster objects collect all questions and pick new questions. Selected questions are returned as a Question-object
    """
    def __init__(self) -> None:
        """
        Creates a new quizmaster object.
        """
        self._questions = []
        self._question_index = -1

    def add_question(self, question_text: str, answers: List[str], correct_answers: List[int]) -> None:
        """
        Adds a new question to the quiz master question collection.
        
        :param str question_text: The question itself, that will be asked
        :param list(str) answers: A list of possible answers, that should be displayed
        :param list(int) correct_answers: A list of indices, that indicate correct anwers in the `answers`
        list. Must contain at least one element.
        """
        self._questions.append(Question(question_text, answers, correct_answers))
        shuffle(self._questions)
        self._question_index = 0

    def pick_question(self) -> Question:
        """
        Returns a random Question object from the collected questions, that has already been
        shuffled.
        
        :returns: the selected Question object
        :raises IndexError: if no questions have been added yet
        """
        if self._question_index < 0:
            raise IndexError("No questions available")
        return_question = self._questions[self._question_index]
        return_question.shuffle()
        self._question_index += 1
        if self._question_index >= len(self._questions):
            shuffle(self._questions)
            self._question_index = 0
        return return_question

def index_to_letter(index: int) -> str:
    """
    Returns a letter from a-z corresponding to the given index, e.g. 0 -> a, 1 -> b and so on.
    
    :param index: The index that shall be converted to a letter.
    :returns: letter from a-z
    :raises ValueError: if the given index is not in the range of 0-25
    """
    if (not isinstance(index, int)) or index not in range(25):
        raise ValueError("index not in range 0-25")
    return chr(index+97)

def letter_to_index(letter: str) -> int:
    """
    Returns an index from 0-25 corresponding to the given letter, e.g. a -> 0, b -> 1 and so on.
    
    :param letter: The letter that shall be converted to an index.
    :returns: index from 0-25
    :raises ValueError: if the given letter is not in the range of a-z
    """
    if (not isinstance(letter, str)) or len(letter) != 1 or letter not in string.ascii_lowercase:
        raise ValueError("letter not in range a-z")
    return ord(letter)-97

