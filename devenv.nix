{ pkgs, ... }:

{
  name = "ruff-qf";

  # https://devenv.sh/packages/
  packages = [ pkgs.git ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    package = pkgs.python312Full;
    poetry = {
      enable = true;
      activate.enable = true;
      install = {
        enable = true;
        allGroups = true;
        allExtras = true;
      };
    };
  };

  # https://devenv.sh/scripts/
  scripts.qf.exec = "poetry run ruff-quickfix";
  scripts.test.exec = "poetry run pytest";
  scripts.full_test.exec = "poetry run tox run";
  scripts.build.exec = "poetry build";

  # https://devenv.sh/outputs/
  outputs = {
    ruff-quickfix = pkgs.callPackage ./. {};
  };

  # NOTE: handle pre-commit outside of devenv. It seems to assume
  # everybody would be using devenv and thus it's safe to _not_ commit
  # the `.pre-commit-config.yaml` file. In my opinion this is counter to
  # the entire draw of pre-commit: developers can easily install the
  # same git hooks even if they are using different tools or flows
  enterShell = "poetry run pre-commit install";

  # See full reference at https://devenv.sh/reference/options/
}
