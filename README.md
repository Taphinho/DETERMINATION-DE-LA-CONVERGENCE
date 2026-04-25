# 📐 Détermination de la Convergence

Un outil en ligne de commande Python pour analyser la **convergence simple** et la **convergence uniforme** d'une suite de fonctions $f_n(x)$ sur un intervalle donné.

---

## 📋 Description

Ce programme permet, à partir d'une fonction $f_n(x)$ saisie par l'utilisateur, de :

1. Calculer la **fonction limite** $f(x) = \lim_{n \to \infty} f_n(x)$
2. Déterminer si la suite est **simplement convergente** sur l'intervalle spécifié
3. Déterminer si la suite est **uniformément convergente** en analysant le comportement de $\sup_{x \in [a,b]} |f_n(x) - f(x)|$ quand $n \to \infty$

---

## 🧮 Concepts mathématiques

### Convergence simple
Une suite de fonctions $(f_n)$ converge **simplement** vers $f$ sur $[a, b]$ si :

$$\forall x \in [a, b], \quad \lim_{n \to \infty} f_n(x) = f(x)$$

### Convergence uniforme
Une suite de fonctions $(f_n)$ converge **uniformément** vers $f$ sur $[a, b]$ si :

$$\lim_{n \to \infty} \sup_{x \in [a, b]} |f_n(x) - f(x)| = 0$$

---

## ⚙️ Prérequis

- Python 3.x
- [NumPy](https://numpy.org/)
- [SymPy](https://www.sympy.org/)

Installation des dépendances :

```bash
pip install numpy sympy
```

---

## 🚀 Utilisation

```bash
python Dtm_convergence.py
```

Le programme vous demandera ensuite de saisir :

1. **La fonction** $f_n(x)$ — en utilisant les variables `x` et `n`
2. **La borne inférieure** de l'intervalle (entier ou `-oo` pour $-\infty$)
3. **La borne supérieure** de l'intervalle (entier ou `+oo` pour $+\infty$)

### Exemple d'utilisation

```
ENTREZ UNE FONCTION fn(x) = x/n
ENTREZ LA BORNE INFERIEURE DE LA DF: 0
ENTREZ LA BORNE SUPERIEURE DE LA DF: 1
```

---

## ✍️ Opérateurs supportés

| Opérateur / Fonction | Description             |
|----------------------|-------------------------|
| `+`                  | Addition                |
| `-`                  | Soustraction            |
| `*`                  | Multiplication          |
| `/`                  | Division                |
| `**`                 | Puissance               |
| `sin()`              | Sinus                   |
| `cos()`              | Cosinus                 |
| `tan()`              | Tangente                |
| `exp()`              | Exponentielle           |
| `ln()`               | Logarithme naturel      |
| `sqrt()`             | Racine carrée           |
| `abs()`              | Valeur absolue          |

---

## 📂 Structure du projet

```
DETERMINATION-DE-LA-CONVERGENCE/
└── Dtm_convergence.py   # Script principal
```

---

## ⚠️ Limites connues

- L'analyse numérique du supremum est effectuée par pas de `0.1` sur l'intervalle, ce qui peut manquer des extrema très localisés.
- En cas de borne infinie (`-oo` ou `+oo`), l'intervalle est remplacé par $[-5, 5]$ pour le calcul numérique.
- Le programme évalue le supremum en $n = 100$ pour l'approximation numérique, ce qui peut être insuffisant pour certaines suites à convergence très lente.

---

## 👤 Auteur

**Taphinho** — [GitHub](https://github.com/Taphinho)

---


Petit programme fait après un cours de maths pour déterminer la convergence des séries de fonctions.
