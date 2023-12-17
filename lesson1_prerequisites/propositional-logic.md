# Discrete Mathematics: Propositional Logic

See [Chapter 3.1 Discrete MathematicsAn Open Introduction](https://discrete.openmathbooks.org/dmoi2/sec_propositional.html)

## Propositional Logic

Two troll playing Statego tell you:

1. Troll 1: If we are cousins, then we are both knaves
1. Troll 2: We are cousins or we are both knaves

C = we are cousins

K = we are both knaves

1. C -> K
1. C v K

| C   | K   | C -> K | C v K |
| --- | --- | ------ | ----- |
| T   | T   | T      | T     |
| T   | F   | F      | T     |
| F   | T   | T      | T     |
| F   | F   | T      | F     |

Recall that trolls are either always-truth-telling knights or always-lying knaves.

TTK = Truth telling knights, (C -> K) & C v K
ALK = Always lying knaves, -((C -> K) & C v K)

| (C -> K) | C v K | TTK -> (C -> K) & C v K |
| -------- | ----- | ----------------------- |
| T        | T     | T                       |
| T        | F     | F                       |
| F        | T     | F                       |
| F        | F     | F                       |

| (C -> K) | C v K | ALK -> -((C -> K) & C v K) |
| -------- | ----- | -------------------------- |
| T        | T     | F                          |
| T        | F     | F                          |
| F        | T     | F                          |
| F        | F     | T                          |

(T v L) <-> v (C v K)

| C   | K   | C -> K | C v K | TTK   | ALK |
| --- | --- | ------ | ----- | ----- | --- |
| T   | T   | T      | T     | **T** | F   |
| T   | F   | F      | T     | F     | F   |
| F   | T   | T      | T     | **T** | F   |
| F   | F   | T      | F     | F     | F   |

Could bith trolls be knights? Yes

## Truth Tables

Here's a question about playing monopoly:

If you get more doubles than any other player then you will lose, or if you lose then you must have bought the most properties.

True or False? We will answer this question, and won't need to know anything about Monopoly. Instead we will look at the logical form of the statement.

P = you get more doubles than any other player
Q = you will lose
R = you must have bought many properties

1. P -> Q
1. Q -> R

We need to decide when the statement (P -> Q) v (Q -> R) is true

| P   | Q   | R   | P -> Q | Q -> R | (P -> Q) v (Q -> R) |
| --- | --- | --- | ------ | ------ | ------------------- |
| T   | T   | T   | T      | T      | T                   |
| T   | T   | F   | T      | F      | T                   |
| T   | F   | T   | F      | T      | T                   |
| T   | F   | F   | F      | T      | T                   |
| F   | T   | T   | T      | T      | T                   |
| F   | T   | F   | T      | F      | T                   |
| F   | F   | T   | T      | T      | T                   |
| F   | F   | F   | T      | T      | T                   |

This statement about monopoly is an example of a **tautology**, a statement which is true on the basis of its logical form alone.

### Example 3.1.1

Make a truth table for the statement **¬P ∨ Q**

| P   | Q   | ¬P  | ¬P ∨ Q |
| --- | --- | --- | ------ |
| T   | T   | F   | T      |
| T   | F   | F   | F      |
| F   | T   | T   | T      |
| F   | F   | T   | T      |

## Logical Equivalence

Notice that the final column in the truth table from ¬P ∨ Q is identical to the final column in the truth table for P -> Q

| P   | Q   | P -> Q | ¬P ∨ Q |
| --- | --- | ------ | ------ |
| T   | T   | T      | T      |
| T   | F   | F      | F      |
| F   | T   | T      | T      |
| F   | F   | T      | T      |

This says that no matter what P and Q are, the statements ¬P ∨ Q and p -> Q either both are true or both are false. We therefore say these statements are **logically equivalent**

### Example 3.1.3

Are the statements, "it will not rain or snow" and "it will not rain and it will not snow" logically equivalent?

P = it will rain

¬P = it will not rain

¬Q = it will not snow

1. ¬(P ∨ Q) = it will not rain or snow
1. ¬P ∧ ¬Q = it will not rain and it will not snow

| P   | Q   | ¬P  | ¬Q  | ¬(P ∨ Q) | ¬P ∧ ¬Q |
| --- | --- | --- | --- | -------- | ------- |
| T   | T   | F   | F   | F        | F       |
| T   | F   | F   | T   | F        | F       |
| F   | T   | T   | F   | F        | F       |
| F   | F   | T   | T   | T        | T       |

**ans**: _Yes_, since every row for the two statements are equal, the two statements are logically equivalent

### Example 3.1.4

Prove that the statements ¬(P -> Q) and P ∧ ¬Q are logically equivalents without using truth tables

1. ¬(¬P ∨ Q)
1. ¬¬P ∧ ¬Q
1. P ∧ ¬Q

Notice that the above example illustrates that the negation of an implication is NOT an implications, it is a conjunction

### Example 3.1.5

Are the statements (P ∨ Q) -> R and (P -> R) ∨ (Q -> R) logically equivalent

| P   | Q   | R   | P ∨ Q | P -> R | Q -> R | (P ∨ Q) -> R | (P -> R) v (Q -> R) |
| --- | --- | --- | ----- | ------ | ------ | ------------ | ------------------- |
| T   | T   | T   | T     | T      | T      | T            | T                   |
| T   | T   | F   | T     | F      | F      | F            | F                   |
| T   | F   | T   | T     | T      | T      | T            | T                   |
| T   | F   | F   | T     | F      | T      | F            | T                   |
| F   | T   | T   | T     | T      | T      | T            | T                   |
| F   | T   | F   | T     | T      | F      | F            | T                   |
| F   | F   | T   | F     | T      | T      | T            | T                   |
| F   | F   | F   | F     | T      | T      | T            | T                   |

**ans**: _No_

While we don't have logical equivalnce, it is the case that whenever (P ∨ Q) -> R is true, so is (P -> R) v (Q -> R). his tells us that we can deduce (P -> R) v (Q -> R) from (P ∨ Q) -> R, just not the reverse direction.

## Deductions

If edith eats her vegetables, then she can have a cookie. Edith ate her vegetables. Therefore Edith gets a cookie.

P = 'Edith eats her vegetables'

Q = 'Edith can have a cookie'

p -> Q

P therefore Q

This is an example of a **deduction rule**, an argument form which is always valid. This one in particular is famously called _modus ponens_. Are you convinced that this is a valid rule? Consider the truth tables

| P   | Q   | P -> Q |
| --- | --- | ------ |
| T   | T   | T      |
| T   | F   | F      |
| F   | T   | T      |
| F   | F   | T      |

What matter is that an argument is valid provided the conclusion must be true given the premises are true. The premises in this case are P -> Q and P. P is true in the first two rows, and of those, only the first row has P -> Q true as well. And lo-and-behold, in this one case, Q is also true. So if P -> Q and P are both true, we see that Q must be true as well

### Example 3.1.6

P -> Q

¬P -> Q

therefore Q

is a valid deduction rule

| P   | Q   | ¬P  | P -> Q | ¬P -> Q |
| --- | --- | --- | ------ | ------- |
| T   | T   | F   | T      | T       |
| T   | F   | F   | F      | T       |
| F   | T   | T   | T      | T       |
| F   | F   | T   | T      | F       |

### Example 3.1.7

Decide whether

P -> R

Q -> R

R

therfore P v R

is a valid deduction rule

| P   | Q   | R   | P -> R | Q -> R | P v Q |     |
| --- | --- | --- | ------ | ------ | ----- | --- |
| T   | T   | T   | T      | T      | T     | ✅  |
| T   | T   | F   | F      | F      | T     |     |
| T   | F   | T   | T      | T      | T     | ✅  |
| T   | F   | F   | F      | T      | T     |     |
| F   | T   | T   | T      | T      | T     | ✅  |
| F   | T   | F   | T      | F      | T     |     |
| F   | F   | T   | T      | T      | F     | ⛔️ |
| F   | F   | F   | T      | T      | F     |     |

In the second to last row, all three of premises of the argument are true, but the conclusion is false. Thus this is not a valid deduction rule.

While we have the reuth table in front of use, look at rows 1, 3 and 5. These ar the only rows which all of the statements P -> R, Q -> R, and P v Q are true. It also happens that R is true in these rows as well. This we have discovered a new deduction rule we know is valid:

P -> R

Q -> R

P v Q

therefore R

## Beyond Propositions

Not every statement can be analyzed using logical connectives alone. For example, we might want to work with the statement:

All primes greater than 2 are odd.

To write this statement symbolically, we must use quantifiers. We can translate as follows

∀x((P(x) ∧ x > 2) → O(x))

P(x) = "x is prime"
O(x) = "x is odd"

These are not propositions, since their truth value depends on the input x. Better to think of P and O as denoting properties of the input. The technical term for these is **predicates** and when we study them in logic, we need to use **predicate logic**

Predicate logic extends propositional logic, much like quantum mechanic exends classical mechanics. Our statemend above still uses the (propositional) logical connectives. Everything about equivalence still applies. However, predicate logic allows us to analyze statements at a higher resolution, digging down into the individual propositions P, Q, etc.

A full treatment of predicate logic is beyond the scope of this text. One rason is that there is no systematic procedure for deciding whether two statements in predicate logic are logically equivalent (i.e there is no analogue to truth tables here). Rather, we end with a couple of examples of logical equivalence and deduction, to pique your interest

### Example 3.1.8

Suppose we claim that there is no smallest number. We can translate this into symbols as

¬∃x∀y(x ≤ y)

it is not true that there is a number x such that for all numbers y, x is less or equal to y

the statement above is equivalent to

∀x∃y(y < x)

notice that y < x is the negation of x ≤ y

For every number x, there is a number y which is smaller that x

## Quiz

| P   | Q   | P -> Q | P ∧ Q | ¬P ∧ Q | P ∧ Q -> P | (P ∧ (Q v ¬P)) ∧ ¬Q |
| --- | --- | ------ | ----- | ------ | ---------- | ------------------- |
| T   | T   | T      | T     | F      | T          | F                   |
| T   | F   | F      | F     | F      | T          | F                   |
| F   | T   | T      | F     | T      | T          | F                   |
| F   | F   | T      | F     | F      | T          | F                   |
