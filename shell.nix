with import <nixpkgs> { };

mkShell {
  name = "ruff-qf-dev";

  buildInputs = [
    ruff
    poetry
    python312
    python312Packages.click 
    python312Packages.mypy
    python312Packages.pytest
    python312Packages.pytest-click
    python312Packages.pytest-cov
    python312Packages.pytest-mock
    python312Packages.tox
    pre-commit
  ];
}
