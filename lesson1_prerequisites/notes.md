# Introduction to Logic

Notes referenced from [Introduction to Logic (written by Patrick Suppes)](<http://web.mit.edu/gleitz/www/Introduction%20to%20Logic%20-%20P.%20Suppes%20(1957)%20WW.pdf>)

## Chapter 1: The Sentential Connectives

## Negation and Conjunction

1. Negation - Sugar does _not_ causes tooth decay, **-P**
1. Conjunction - Mary loves John and John loves mary, **P & Q**

## Disjunction

1. Non-Exclusive Disjunction - the disjuntion of two sentenses is true if at least one of the sentences is true
   > Eg. Legal: Before any such work is done or any such materials are furnished, the Lessee and any contractor or other person engaged to do such work and/or furnish such materials shall funish such bond or bonds as the Lessor may reasonably require ...
1. Exclusive Disjunction - The disjunction of two sentences if true if and only if at least one of the sentenses is true, but not both, **P ∨ Q**

   > Thus a father tells his child, "You may go to the movies or you may go to the circus this Saturday but not both"

## Implication: Conditional Sentences

1. _If_ Mary loves John, _then_ John loves Mary.

   - In Mathematical Logic, sentence (1) is true if the sentence 'Mary loves John' is false, regardless of the truth or falsity of the sentence 'John loves Mary'
   - The sentence following 'if' is the _antecedent_ or _hypothesis_, 'Mary loves John'
   - The sentence following 'then' is the _consequent_ of _conclusion_, 'John loves Mary'
   - The rule of usage is then: A conditional sentence is false if the antecedent is true and the consequent is false; otherwise it is true.

   1. Intuitive objections to this rule could be made on two counts:
      1. It can be maintained that implication is not a truth-fucntional connective but that there should be some sort of definite connection between the antecedent and the consequent of a conditional senstence
      1. The wrong stipulation has been made in calling any implication true when its antecedent is false, but paricular examples argue for our rule

1. If poetry is for the young, then 3 + 8 = 11

   - Accoding to this usage, sentence (2) is true, since the consequent is true

1. Ithe there are approximately one hundred milliion husbands in the United States, then there are approximately one hundred million wives in the United States

   - Its hard to imagine anyone denying the truth of (3) for the case where the consequent if true, consider the modification in sentence 4 ()

1. If there are approximately one hundred million husbands in the United States, then the number of husbands in this country is greater than the number in France

   - I (3) and (4) are admitted as true, then the truth-functional rule for conditional sentences with false antecedents is fixed
   - By choosing slightly different examples a case could be made for considering any implication false when its antecedent is false, for instance, suppose the we replace (3) with (5)

1. If there are approximately one hundred million husbands in the United States, then there is exactly one wife in the Unted States.
   - Within our truth-functional framework it might be maintained that an implication with false antecedent and false consequent is false, since it may be plausibly arged that in ordinary usage, (5) is fals
   - The truth-functional demand sentences like (5) be counted as true has no undesirable effects, since conditional sentences whose antecedents and consequents are unrelated and whose antecedents are false play no serious role in systematice arguments

As a mater of notation, the conditonal sentence formed from any two sentences P and Q is written, **P ⇒ Q**

We shall write **P ⇒ Q**, for:

1. **P** only if **Q**, 'John dates Mary only if Elizabeth is mad at him'
1. **Q** if **P**, ✅ 'If Elizabeth is mad at him then John dates Mary'
   - ⛔ Don't mistake for 'If John dates Mary then Elizabeth is mad at him'
1. **Q** provided that **P**
1. **P** is a sufficient condition for **Q**
1. **Q** is a necessary condition for **P**

## Equivalence: Biconditional Sentences

We use th words 'If and only if' to obtain from two sentences a biconditional sentence.

1. Biconditional - also called _equivalence_, the two sentences connected by 'if and only id' are called the _left_ and _right_ member of the equivalence

The bicontional:

1. **P** if and only if **Q**, has the same meaning as sentence below
1. **P** if **Q**, and **P** only if **Q**, is equivalent to below
1. If **P** then **Q**, and if **Q** then **P**

Thus the rule: A biconditional sentence is true if and only if its two members are either both true of both false. As a mattr of notation, we write **P ⇔ Q**

## Grouping and Parantheses

1. If Showboat wins the race, the Shotless and Ursula will show
   - Symbolized by **S ⇒ (H & U)**
   - If **S** the **H** and **U8**
   - **P ⇔ Q & R** means **P ⇔ (Q & R)**

The convention is '⇒' and '⇔' dominate '&' and '∨' On the other hand, under this convention it is not clear what: - **P & Q ∨ R** or **P ⇔ Q ⇒ R**

## Truth Tables and Tautologies

Our truth-functional rules of negation, conjucntion, disjunction, implication and equivalence summarized in tabular form

Negation
| P | -P|
|---|---|
|T | F |
|F | T |

Conjunction
|PQ| P & Q |
|--|-----|
|TT|T|
|TF|F|
|FT|F|
|FF|F|

Disjunction
|PQ| P ∨ Q |
|--|-----|
|TT|T|
|TF|T|
|FT|T|
|FF|F|

Implication
|PQ| P ⇒ Q |
|--|-----|
|TT|T|
|TF|F|
|FT|T|
|FF|T|

Equivalence
|PQ| P ⇔ Q |
|--|-----|
|TT|T|
|TF|F|
|FT|F|
|FF|T|

1. Tautological- whether **P** is true or false, **P ∨ -P** is true and hence a tautology ✅
   | P | -P | P ∨ -P |
   |---|----|--------|
   | T | F | T |
   | F | T | T |

   - The idea of the derived truth table is that a sentence is a tautology if it is tru for all combinations of possible truth values of its component atomic sentences
   - For instance, to show that **P ∨ Q ⇒ P** is not a tautology ⛔
     | P | Q | P ∨ Q | P ∨ Q ⇒ P |
     |---|---|-------|-----------|
     | T | T | T | T |
     | T | F | T | T |
     | F | T | T | F |
     | F | F | F | T |
   - When we take as our formal definition, A sentence is a tautology if and only if the result of replacing any of its component atomic sentences (in all occurences) by other atomic sentences is always a true sentence

- If there are are _n_ distinct component atomic sentences there are 2^n possible cobination of truth values and this 2^n rows to the truth table
- A statement which is not a tautology may become one upon the substitution of compound sentences for atomic sentences or substitution of the same sentence for distinct atomic sentences inthe original statement
- A statement which is a tautology remains so when any sentences are substituted for its component atomic sentences in all occurences

1. Tautological Implication - A sentence **P** is said to tautologically imply a sentence **Q** if and only if the conditional **P ⇒ Q** is a tautology
1. Tautological equivalent - If two sentences are tautologically equivalent, they express essentially the same facts, and consequently their roles in inference are nealy identical

   - By way of example, let **A** be 'Aristotle was left-handed' and **L** be 'Leibniz was left-handed'. Then the sentence **A & -L** is tautologically equivalent to the sentence **-(-A ∨ L)**
   - To see this, we may use truth tables
     | A | L | -A | -L | -A ∨ L | -(-A ∨ L) | A & -L |
     |---|---|----|----|--------|-----------|--------|
     | T | T | F | F | T | F | F |
     | T | F | F | T | F | T | T |
     | F | T | T | F | T | F | F |
     | F | F | T | T | T | F | F |

     - The test is clear, The columns corresponding to the tow sentences must agree row for row in their entries in order for the two sentnces to be tautologically equivalent
     - Column 6 and 7 of the table, **-(-A ∨ L)** is tautologically equivalent to **A & -L**

   - It is worth remarking that **P** and **Q** are tautologically equivalent when and only when the biconditional **P ⇔ Q** is a tautology
