## Main Work Flows

1. factorization
   dispatch input into parts
2. transformation
   transform parts from cpp form into golang form
   recursion
3. composition
   composite the golang parts into outputs

## Cpp Content Structure

### cpp struct member
```tpl
{whites}{tvpair};
```

### cpp function declaration
```tpl
{whites}{type} {function}({tvpair list});
```

### cpp tvpair list
```python
", ".join([tvpair])
```

### cpp tvpair
```
{type} {variable}
```

### cpp function
```python
"_".join([word])
```
### cpp type
```python
"_".join([word]){*}?
```

### cpp variable
```python
"_".join([word])
```

## Golang Content Structure
### golang struct member
```tpl
{whites}{tvpair}
```

### golang interface methods
```
{whites}{function}({tvpair list}) {type}
```

### golang tvpair list
```python
", ".join([tvpair])
```

### golang tvpair
```
{variable} {type}
```

### golang function
```python
"".join([FirstUp(word)])
```

### golang type
```python
{*}?{word}"".join([firstUp(word)][1:])
```

### golang variable

public:
```python
"".join([firstUp(word)])
```

private:
```python
{word}"".join([firstUp(word)][1:])
```
