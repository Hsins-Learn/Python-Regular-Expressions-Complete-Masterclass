# 01. Methods and Objects

- [01. Methods and Objects](#01-methods-and-objects)
  - [The `re` Module](#the-re-module)
  - [Raw Strings](#raw-strings)
  - [Methods of The `re` Module](#methods-of-the-re-module)
    - [`re.compile()`](#recompile)
    - [`re.search()`](#research)
    - [`re.match()`](#rematch)
    - [`re.fullmatch()`](#refullmatch)
    - [`re.findall()`](#refindall)
    - [`re.split()`](#resplit)
    - [`re.sub()`](#resub)
    - [`re.subn()`](#resubn)
  - [`group()` and `groups()`](#group-and-groups)
  - [`start()`, `end()` and `span()`](#start-end-and-span)
  - [Optional Flags](#optional-flags)
  - [AttributeError](#attributeerror)

## The `re` Module

The `re` module is a built-in Python module that provides all the required functionality that we need for handling patterns and regular expressions. We can use `dir(re)` to have a quick overview of all the flags and methods available inside the module.

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## Raw Strings

We may already know the backslash `\` having a special meaning in some circumstances because they may indicate an escape character or escape sequence. e.g.

- `\n`: new line character
- `\t`: tab character
- `\U`: stands for Unicode

If we're going to access the folder under Windows platforms with given path `"C:\Users\tasks\new"`, the Python interpreter will trigger a `SyntaxError: (unicode error)`. However we can solve this issue by turning the regular string into a raw string by adding a lowercase `r`.

```python
# SyntaxError: (unicode error)
path = "C:\Users\tasks\new"

# Turn the regular string into a raw string
path = r"C:\Users\tasks\new"
```

Always use the raw strings with regular expression pattern in order to avoid any of issues above.

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## Methods of The `re` Module

### `re.compile()`

The `re.compile()` method will compile a regular expression pattern provided as a string into a regular expression object `re.Pattern`. And the `re.Pattern` objects can be handled using various other methods such as `re.match()` or ` re.search()`.

```python
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

pattern = re.compile(r"\d{4}")
result = re.findall(pattern, string)  # ['1998']
```

The `\d{n}` is called a special sequence and it will match `n` digits from 0 to 9 in the target string. Keep in mind that the `re.compile()` method is useful for defining and creating a regular expressions object initially and then using that object for multiple matches.

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

### `re.search()`

We can use the `re.search()` method to search given pattern segment in the target string and the `re.Match` object will be returned. The convenstion is to write the actual pattern here since we're not defining and compiling pattern beforehand.

```python
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# <re.Match object; span=(15, 18), match='600'>
result = re.search(r"\d{3}", string)
```

It's very important that the `re.search()` method will always match and return the first occurance of the pattern in the target string. Therefore although there're 3 different match groups in the target string, the `re.search()` will only match and return the first one and then it will stop its execution. If no match is found, the result is `None`.

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

### `re.match()`

The `re.match()` method matches only at the beginning of the target string, if no match is found it returns `None`.

```python
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# <re.Match object; span=(0, 3), match='The'>
result = re.match(r"\w{3}", string)
```

The `\w{n}` will match `n` non-empty characters in the target string. If we use `re.match(r"\w{4}", string)`, it will return `None` because the `re.match()` method only scans at the beginning of the target string.

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

### `re.fullmatch()`

The `re.fullmatch()` method returns a result only if the pattern matches the entire target string. If no match is found, it returns `None`.

```python
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# <re.Match object; span=(0, 285), match='The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February.'
result = re.fullmatch(r".{285}", string)
```

In regex syntax, the dot character `.` matches any character except the new line character `\n`. If the target string would have contained one or more new line characters, the match would not have been made since the special character excludes the new line.

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

### `re.findall()`

The `re.findall()` method unlikes other methods we've seen so far which have various limitations in scope. It will search and return all the matches that were found inside the target string according to the given pattern.

```python
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# ['600', '199', '600']
result = re.findall(r"\d{3}", string)

# []
result = re.findall(r"\d{9}", string)
```

Keep in mind that using this method, the target string is scanned from left to the right and the matches are returned in the order they were found as a list of strings. If no match is found, it returns empty list `[]`.

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

### `re.split()`

The `re.split()` method is similar with the `split()` method of `String` object but we can use the regex pattern instead of constant string.

```python
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# ['The', 'Euro', 'STOXX', '600', 'index,', 'which', 'tracks', 'all', 'stock', 'markets', 'across', 'Europe', 'including', 'the', 'FTSE,', 'fell', 'by', '11.48%', '–', 'the', 'worst', 'day', 'since', 'it', 'launched', 'in', '1998.', 'The', 'panic', 'selling', 'prompted', 'by', 'the', 'coronavirus', 'has', 'wiped', '£2.7tn', 'off', 'the', 'value', 'of', 'STOXX', '600', 'shares', 'since', 'its', 'all-time', 'peak', 'on', '19', 'February.']
result = re.split(r"\s", string)

# ['The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February.']
result = split(r"\s{3}", string)
```

If the specified pattern is not matched inside the target string, then the string is not splited so it will return a list contains just one element the target string itself.

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

### `re.sub()`

The `re.sub()` method is used for replacing one or more occurrences of certain pattern in the target string with another string. We can also set the maximum number of replacements that we wants to make inside the string by setting count parameter.

```python
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# 'The Euro INDEX 600 index, which tracks all stock markets across Europe including the INDEX, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of INDEX 600 shares since its all-time peak on 19 February.'
result = re.sub(r"[A-Z]{2,}", "INDEX", string)

# 'The Euro INDEX 600 index, which tracks all stock markets across Europe including the INDEX, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February.'
result = re.sub(r"[A-Z]{2,}", "INDEX", string, 2)
```

The `[A-Z]` or `[a-z]` are called character classes, where `[A-Z]` means any uppercase letter and `[a-z]`] means any lowercase letter. After that we haven't specified only the integer but also a comma right after it in a pair of curly brackets `{n,}`, this means that we expect the preceding pattern or character to repeat at least `n` times.

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

### `re.subn()`

The `re.subn()` method performs the same task as the `re.sub()` method but returns different objects. It returns a tuple consisting of the new version of the target string after all the replacements have been made and the number of replacement it has made.

```python
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# ('The Euro INDEX 600 index, which tracks all stock markets across Europe including the INDEX, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of INDEX 600 shares since its all-time peak on 19 February.', 3)
result = re.subn(r"[A-Z]{2,}", "INDEX", string)
```

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## `group()` and `groups()`

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## `start()`, `end()` and `span()`

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## Optional Flags

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## AttributeError

<br/>
<div align="right">
  <b><a href="#01-methods-and-objects">[ ↥ Back To Top ]</a></b>
</div>
<br/>