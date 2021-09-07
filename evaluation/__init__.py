from .bleu import Bleu
from .meteor import Meteor
from .rouge import Rouge
from .origin_cider import Cider
from .tokenizer import PTBTokenizer
from .spice.spice import Spice

def compute_scores(gts, gen,spice=False):
    if spice:
        metrics = (Bleu(), Meteor(), Rouge(), Cider(), Spice())
    else:
        metrics = (Bleu(), Meteor(), Rouge(), Cider())
    all_score = {}
    all_scores = {}
    for metric in metrics:
        score, scores = metric.compute_score(gts, gen)
        all_score[str(metric)] = score
        all_scores[str(metric)] = scores

    return all_score, all_scores
