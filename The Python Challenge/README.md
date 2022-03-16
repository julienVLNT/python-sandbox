Mes solutions aux problèmes de [The Python Challenge](http://www.pythonchallenge.com/). Les codes sont numérotés par problème.

| **Problème** | **URL**                                                | **Résolu ?** |
|--------------|--------------------------------------------------------|--------------|
| 0            | [clic](http://www.pythonchallenge.com/pc/def/0.html)   | ✓ 16/03/2002 |
| 1            | [clic](http://www.pythonchallenge.com/pc/def/map.html) |

---

# Résultats <!-- omit in toc -->

- [Problème 0 : "Warmup"](#problème-0--warmup)
- [Problème 1](#problème-1)

## Problème 0 : "Warmup"

Il suffit de modifier l'URL de la page : changer $0$ pour le résultat de $2^{38}$. L'URL est donc

```
http://www.pythonchallenge.com/pc/def/274877906944.html
```

## Problème 1

On voit trois associations de lettres. Chaque fois, le décalage entre les deux vaut +2. On devine qu'il va falloir appliquer ce décalage à chaque caractère du texte écrit en mauve.
On déclare la variable `crypte` contenant la chaîne de caractère à traduire.

```python
>>> crypte = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
```

Essayons

```python
>>> clef  = lambda c : chr(ord(c)+2)
>>> clair = ''.join([clef(car) for car in crypte])
```

On obtient

```python
>>> clair
'i"hope"you"didnt"tr{nsl{te"it"|y"h{nd0"th{ts"wh{t"computers"{re"for0"doing"it"in"|y"h{nd"is"inefficient"{nd"th{t)s"why"this"text"is"so"long0"using"string0m{ketr{ns*+"is"recommended0"now"{pply"on"the"url0'
```

Ce n'est pas diablement efficace.