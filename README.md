# DeclarationCpp2Go
A small tool script that convert the C++ declaration to Golang. It **DO NOT** generate runnable golang script. 

[![github workflow](https://img.shields.io/github/workflow/status/RyoJerryYu/DeclarationCpp2Go/Python/main?logo=github)](https://github.com/RyoJerryYu/DeclarationCpp2Go/actions?query=branch%3Amain) [![codecov](https://codecov.io/gh/RyoJerryYu/DeclarationCpp2Go/branch/main/graph/badge.svg?token=PJ9OR1N7JI)](https://codecov.io/gh/RyoJerryYu/DeclarationCpp2Go)
 
### Usage

```bash
$ python main_funcs.py path/to/your/input.file > path/to/your/output.file
$ python main_members.py path/to/your/input.file > path/to/your/output.file
```

### How will it works like

It convert: 
- C++ structs and classes members to Golang struct
  - remove the semicolon end of a line
  - convert the member variable name from snake_case to PascalCase
  - NOT convert the format of type names
  - exchange the position of each types and variables
  - move the `*` mark to the left of the type name
- C++ classes methods to Golang Interfaces
  - remove the semicolon end of a line
  - convert the parameter name from snake_case to camelCase
  - convert the function name from snake_case to PascalCase
  - NOT convert the format of type names
  - move the return type names from the head to the end
  - move the type names right of their variables
  - move the `*` mark to the left of the type name
  - remove the return type `void`

Maybe more in future.
