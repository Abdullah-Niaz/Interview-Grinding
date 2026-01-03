## Python Language Semantics m

### 1. Name Binding and the LEGB Rule

In Python, **variables are names bound to objects**, not containers that store values.
A name is simply a reference to an object that exists somewhere in memory.

```python
x = 10
```

Here, `x` is bound to the integer object `10`. The integer does not live inside `x`.

---

### Name Lookup Order. LEGB

When Python evaluates a name, it searches scopes in the following order:

1. **Local**. Inside the current function.
2. **Enclosing**. Inside any outer functions (non-global).
3. **Global**. At the module level.
4. **Built-in**. Names provided by Python itself, such as `len`, `print`, `range`.

---

### Example

```python
x = 10

def outer():
    x = 20
    def inner():
        print(x)
    inner()

outer()
```

**Output**

```
20
```

**Why this happens**

* `inner()` looks for `x`.
* There is no local `x` inside `inner`.
* Python checks the enclosing scope `outer`.
* `x = 20` is found there, so it is used.

This demonstrates the **Enclosing** part of LEGB.

---

### Assignment vs Reading. Critical Rule

This is the most important semantic rule juniors misunderstand.

* **Reading a name** follows LEGB.
* **Assigning to a name** creates a **local binding by default**.

Example:

```python
x = 10

def func():
    x = 5
    print(x)

func()
print(x)
```

Output:

```
5
10
```

* `x = 5` creates a new local `x`.
* The global `x` is untouched.

---

### Why `global` and `nonlocal` Exist

#### `global`

Used when you want to bind a name at the module scope.

```python
x = 10

def func():
    global x
    x = 20

func()
print(x)
```

Output:

```
20
```

#### `nonlocal`

Used to rebind a name in an enclosing (but non-global) scope.

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()
```

Output:

```
20
```

Without `nonlocal`, `x = 20` would create a new local variable inside `inner`.

---

### Common Junior Mistakes

1. **Thinking variables live inside functions**
   Incorrect. Objects live independently. Functions only create scopes for name lookup.

2. **Assuming assignment updates an outer variable automatically**
   Incorrect. Assignment creates a new local binding unless `global` or `nonlocal` is used.

3. **Confusing mutation with rebinding**
   This works without `global`:

   ```python
   def func(lst):
       lst.append(4)
   ```

   This does not:

   ```python
   def func(lst):
       lst = [1, 2, 3]
   ```

   * `append` mutates the existing object.
   * `lst = ...` rebinds the name locally.

---

### Interview-Level Summary

* Python uses **name binding**, not variable storage.
* Name resolution follows **LEGB**, always.
* **Reading** a name does not change scope.
* **Assignment** defines scope unless explicitly overridden.
* `global` and `nonlocal` change where bindings occur, not where objects live.

