import time

from anki.hooks import wrap
from anki.sound import playFromText
from aqt.reviewer import Reviewer
from aqt import mw

def myShowAnswer(self):
    config = mw.addonManager.getConfig(__name__)

    if config['play_question_audio']:
	    playFromText(self.card.q())

    if config['play_answer_audio']:
	    playFromText(self.card.a())

Reviewer._showAnswer = wrap(Reviewer._showAnswer, myShowAnswer)

