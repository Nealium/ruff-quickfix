{ pkgs ? import <nixpkgs> {} }:

with pkgs;

python312Packages.buildPythonPackage {
  pname = "ruff-quickfix";
  version = "0.1.1";
  pyproject = true;

  src = ./.;

  nativeBuildInputs = [
    python312Packages.poetry-core
    ruff
  ];

  propagatedBuildInputs = with python312Packages; [
    click 
  ];
}
