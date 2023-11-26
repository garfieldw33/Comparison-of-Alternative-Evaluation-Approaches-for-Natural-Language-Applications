# Comparison-of-Alternative-Evaluation-Approaches-for-Natural-Language-Applications

## Datasets:

* (1) en.combined: original reference
* (1.2) en.shuffle4G.combined: 4-grams reordered in sentences [unreadable texts]
* (1.3) synonyms _translations.txt: Use synonyms to process translation results

* (2) zh.combined: original Chinese texts

* (3) googletrans.combined: translation generated from (2) by Google [good translation]
* (3.1) googletrans_shuffled.txt: words randomly reordered in sentences. [unreadable texts]
* (3.2) googletrans.shuffle4G.combined: 4-grams reordered in sentences. [unreadable texts]

## Experiments:
a)	Original standard English texts vs. Original translated English texts. The evaluation methods are expected to gen-erate a relatively high score on this pair to acknowledge a good translation.

b)	Original standard English texts vs. Shuffled translated English texts. The evaluation methods are expected to re-turn a low score on this pair to represent the loss of meaning in sentences.

c)	Original standard English texts vs. 4-gram reordered translated English texts. The result shall be similar to the last pair but the score could be a little higher.

d)	Original translated English texts vs. 4-gram reordered translated English texts. The evaluation methods are expected to report a relatively low score on this pair to represent the loss of meaning in sen-tences.

e)	Original standard English texts vs. 4-gram reordered standard English texts. The result shall be similar to the result in experiments in d).

f)	Original standard English texts vs. Standard English texts with synonyms replaced. A good evaluation method is expected to provide a high rating similar to the original dataset.

## Evaluation approaches tested:
* BLEU
* BARTScore
* BERTScore
* COMET

  
