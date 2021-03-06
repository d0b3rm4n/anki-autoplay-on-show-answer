from aqt import gui_hooks
from aqt import mw
from aqt.sound import av_player

def auto_play_all(card):
    config = mw.addonManager.getConfig(__name__)
    tags = []

    left = int(card.left / 1000)
    if config['play_question_audio']:
        tags += card.question_av_tags()

    if config['play_answer_audio']:
        if card.queue >= 2 or (card.queue == 1 and left == 1):
            tags += card.answer_av_tags()

    if tags:
        av_player.play_tags(tags)

gui_hooks.reviewer_did_show_answer.append(auto_play_all)
