# Broken Access Control 

## Core Concepts


### Session Management

 Session management maintains a user's authenticated state across multiple requests, allowing them to stay logged in without re-authenticating each time.
A session cookie identifies the logged-in user on every request.

---

### Access Control (Authorization)

 Access control is the process of determining whether an authenticated user is permitted to access a resource or perform a specific action.

---

# Types of Access Control

## 1. Vertical Access Control

Vertical access control restricts access to resources and functionality based on different privilege levels or roles within an application.

**Purpose:** Prevent lower-privileged users from accessing higher-privileged functionality.


### Broken Vertical Access Control

Occurs when a lower-privileged user gains access to functionality intended for a higher-privileged role.

---

## 2. Horizontal Access Control
Horizontal access control restricts users with the same privilege level from accessing each other's private resources.

**Purpose:** Ensure users can access only their own data.


### Broken Horizontal Access Control

Occurs when a user can access or modify another user's resources.


---

## 3. Context-Dependent Access Control

Context-dependent access control restricts actions based on the application's current state or the required sequence of operations.

**Purpose:** Ensure users follow the intended workflow.


### Broken Context-Dependent Access Control

Occurs when permission checks are enforced during some steps of a workflow but are missing from the final action, allowing users to bypass the intended process.


---

# Testing Approach

When testing for broken access control, ask three questions:

### Vertical

**Can a lower-privileged user access higher-privileged functionality?**

### Horizontal

**Can one user access another user's resources?**

### Context-Dependent

**Can I bypass the application's intended workflow?**

---

# Prevention

*  Deny access unless it is explicitly allowed.
* Perform permission checks in a single, consistent authorization layer.
*  Never rely on client-side data (URLs, cookies, hidden fields, or JavaScript) for authorization decisions.
*  Grant users only the minimum permissions required to perform their tasks.

---
