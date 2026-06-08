# How password hashing works

- When you sign up a password even before it is saved it undergoes a process called hashing 
- Hashing is the process of transorming a password into fixed length of random values which cannot be reversed back into the password 

---

## What happens when you login 

- After you enter the password it undergoes hashing and that value is compared with the hased value stored in the server

---

## Hashing properties 

1. Deterministic 
  - same input should give same output 

2. Fast computation 
  - Hashing should be quick to compute

3. Avalance effect
  - small change in input should bring great change in output

4. Preimage resistance 
  - hash value shouldnot be computationally reversable

5. Collision resistance 
  - two different input shouldnt have same output
  - It is mathematically not possible but a good hash function reduces the probability

---

## Problem in hashing 
- Piegon hole principle ( hash collision):
  Since hash value consists of fixed length the output is limited while the input is not.
  So some input chould hace same output

## Additional security 
### Salting 
 - Salting refers to the process of adding a random value to input even before it undergoes hashing 
 - It prevents identical passwords from having identical hashes

 ---

## Rainbow table 
- It is a table consisting of common password and their hash values