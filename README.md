# FastAPI Template

This template provides a setup for a FastAPI project.

## Dependencies

Please install the following dependencies:

| Dependencies                                    | Description                            |
| ----------------------------------------------- | -------------------------------------- |
| [Python 3.13+](https://www.python.org)          | Programming language                   |
| [uv](https://docs.astral.sh/uv)                 | Package manager for Python             |
| [mkcert](https://github.com/FiloSottile/mkcert) | HTTPS certificate generator            |
| [just](https://just.systems)                    | Command runner                         |
| [ls-lint](https://ls-lint.org)                  | Linting tool for directories and files |
| [typos-cli](https://github.com/crate-ci/typos)  | Spell checker                          |

## Commands

The following commands are available:

### Installing

This command will install Python dependencies.

```sh
just i
```

### Upgrading

This command will upgrade Python dependencies.

```sh
just up
```

### Formatting

This command will format the code.

```sh
just fmt
```

### Linting

This command will lint the code.

```sh
just lint
```

### Checking

This command will do formatting and linting.

```sh
just check
```

### Development (HTTPS)

This command will start the development server in HTTPS mode.

```sh
just cert
just dev
```

### Development (HTTP)

This command will start the development server in HTTP mode.

```sh
just http
```

### Production

This command will build the code and start the production server.

```sh
just start
```

### Cleaning

This command will clean the unnecessary files.

```sh
just clean
```

This command will clean all unnecessary files including the `.venv` directory.

```sh
just clean-all
```
