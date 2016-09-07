<h1 align="center">Pygwizo</h1>
<br>
![home](https://github.com/kampsy/pygwizo/blob/master/img/pygwizo.png)

pygwizo |pronounced as [py guizo]| is a Python 3 implementation of the
Porter Stemmer algorithm (An algorithm for suffix stripping M.F.Porter 1980 see:
(http://tartarus.org/martin/PorterStemmer/def.txt).
pygwizo is very extensible and comes with cool features.

Pygwizo is an awesome tool for projects involving:
1) Machine Learning algorithms, specifically Natural language processing (NLP).
2) Inverted indices for Information Retrieval Systems eg Search Engines.

The string that the Ingest() function takes is case insensitive

## Installation

Just download pygwizo.py and put it in your project directory.


# Usage

## DeepStem:

The ingested word goes through every step in the algorithm.
```Python
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    print(val.deep_stem())
```
```shell
$ ./main.py

Stem: able
```

## shallow_stem

The word Goes through each step in accending order just like DeepStem. But The
difference is that it return when the original word is changed.
```python
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    print(val.shallow_stem())
```

```shell
$ ./main.py

Stem: abiliti
```

## shallow_stemmed

Works exactly like ShallowStem. The difference is that it returns
the Step that was used instead of the stem.
```python
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    print(val.shallow_stemmed())
```
```shell
$ ./main.py

Steps used: step_1a()
```

## vowcon and Measure

```python
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo

  if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    # vowcon
    print("{0} has Pattern {1}".format(val.word, val.vowcon))

    # Measure value [v]vc{m}[c]
    print("{0} has Measure value {1}".format(val.word, val.measure))
```
```shell
$ ./main.py

abilities has Pattern vcvcvcvvc
abilities has Measure value 4
```


## Access Any step Directly

pygwizo is so extensible that it allows you to use its core components.
you can explicitly specify which Step to use on an ingested string.
```python
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
```
```shell
$ ./main.py

trouble
vietnamize
electric
```

## File Stem Performance.

pygwizo stemmed the file input.txt containing 23531 words in 10.5375394821167s
on an AMD C655 Laptop.
```python
  #!/usr/bin/env python3
  # -*- coding:utf-8 -*-

  import pygwizo
  import time

  if __name__ == "__main__":
      array = open("input.txt").read().splitlines()
      start_time = time.time()
      for word in array:
          val = pygwizo.Ingest(word)
          deep = val.deep_stem()
          with open("stem.txt", "a") as file:
              stem = deep + "\n"
              file.writelines(stem)
              print(word, " ---> ", deep)

      print("============================")
      print("Done After: %ss" % (time.time() - start_time))
      print("============================")
```
```shell
$ ./main.py

Done After: 10.5375394821167s
```

## License
BSD style - see license file.

## Developer
kampamba chanda (a.k.a kampsy).
twitter: @kampsy
google+: google.com/+kampambachanda
email: kampsycode@gmail.com
