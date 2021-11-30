## Cpp Content Structure

### cpp struct member
```tpl
{tvpair};
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
