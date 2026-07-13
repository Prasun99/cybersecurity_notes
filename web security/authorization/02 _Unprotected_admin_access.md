# Unprotected admin functionality

## Vulnerability
* The application doesnot enforce access control on admin endpoint  

## Broken assumption
* If they dont know the exact URL they cant access the admin 

## Flaw
* Server never checks session role on that route 

## How hackers exploit it 
1. Firstly they find the admin url(via brute force) 
2. Since there is no need of credentials they can access the admin panel with no difficulty

## Mitigation 
* Use access control protection 
