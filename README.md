pygwizo
=======
<code>The stemmer with a magic touch </code>
<br>
<img src="https://github.com/kampsy/pygwizo/blob/master/img/pygwizo.png" height="200px" width="200px">
<br>
<hr>

pygwizo |pronounced as [pyguizo]| is the Next generation Native Python 3 implementation of the
Porter Stemmer algorithm (An algorithm for suffix stripping M.F.Porter 1980 see:
(http://tartarus.org/martin/PorterStemmer/def.txt).
pygwizo is different from other Python implementation because It is extensible and it
comes with cool features. It is designed to be extensible, so that developers can easily create
new experiences.(see examples below).

pygwizo is an awesome tool for projects involving:
1) Machine Learning algorithms, specifically Natural language processing (NLP).
2) Inverted indices for Information Retrieval Systems eg Search Engines.


Note: I made a few modification to pygwizo for it to pass the unittest. The original algorithm
at http://tartarus.org/martin/PorterStemmer/def.txt) has a few issues(opinion!).

The string that the Ingest() function takes is case insensitive

Installation
------------
<pre>
  just download pygwizo.py and put it in your project directory.
</pre>

[[[[[ Examples ]]]]]

deep_stem, shallow_stem, shallow_stemmed
====================================================
deep_stem: The ingested word goes through every step in the algorithm.
<pre>
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    print(val.deep_stem())

  Results
  ---------------------
  Steps used: step_1a() then step_2()
  Stem: able
</pre>

shallow_stem: The word Goes through each step, from top to bottom like in
deep_stem. The difference is that it bells out the moment a step Stems the
ingested word.
<pre>
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    print(val.shallow_stem())

  Results
  ---------------------
  Steps used: step_1a()
  Stem: abiliti
</pre>

shallow_stemmed: Works exactly like shallow_stem. The difference is that it returns
the step that was used instead of the stem.
<pre>
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    print(val.shallow_stemmed())

  Results
  ---------------------
  Steps used: step_1a()
</pre>

vowcon and Measure
====================================================
<pre>
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    # vowcon
    print("{0} has Pattern {1}".format(val.word, val.vowcon))

    # Measure value [v]vc{m}[c]
    print("{0} has Measure value {1}".format(val.word, val.measure))

  Results
  ---------------------
  abilities has Pattern vcvcvcvvc
  abilities has Measure value 4
</pre>

Access Any step Directly
====================================================
pygwizo is so extensible that it allows you to use its core components.
you can explicitly specify which step to use on an ingested string.
<pre>
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  if __name__ == "__main__":
    val = pygwizo.Ingest("troubled")
    # Stem only with Step_1b
    print(val.step_1b())

    val.word = "vietnamization"
    # Stem only with Step_2
    print(val.step_2())

    val.word = "electriciti"
    # Stem only with Step_3
    print(val.step_3())

  Results
  ---------------------
  trouble
  vietnamize
  electric
</pre>

File Stem Performance.
====================================================
pygwizo stemmed a file input.txt containing 23531 in
on my computer.
<pre>
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  array = open("input.txt").read().splitlines()
  for word in array:
    val = pygwizo.Ingest(word)
    deep = val.deep_stem()
    with open("stem.txt", "a") as file:
      stem = deep + "\n"
      file.writelines(stem)
      print(word, " ---> ", deep)

  Results
  ---------------------
  Done After: 11s
</pre>

License
==========
BSD style - see license file.

Developer
===============
kampamba chanda (a.k.a kampsy).
twitter @kampsy
google+ google.com/+kampambachanda
email: kampsycode@gmail.com
