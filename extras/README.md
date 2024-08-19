# ruff-quickfix extras

These are extra files demonstrating using `ruff-quickfix` in conjunction with
with pylint. The user commands are slightly more complex than the ones shown in
the README. I have also included a standalone version of the `ruff-quickfix`
command.

## Conjunction

### Neovim

1. Copy `python.lua` to `~/.config/nvim/after/ftplugin/python.lua`
2. Copy `python_lint.lua` to `~/.config/nvim/python_lint.lua`
3. include `python_lint` in main `init.lua` file with ~`require("python_lint")`
    * specifics might be slightly different

### Vim

1. Copy `python.vim` to `~/.vim/ftplugin/python.vim`
2. Copy `python_lint.vim` to `~/.vim/python_lint.vim`
3. include `python_lint` in main `vimrc` file with ~`source ~/.vim/python_lint.vim`

**Note:** If on windows replace `.vim` with `vimfiles` for all paths

### Usage

Run `:Pylint` and `:Ruff` to toggle between the two linters

## Standalone

1. Copy file somewhere in your PATH, `~/.local/bin` is usually a good spot
2. Run `chmod +x {path_to_file}`, `chmod +x ~/.local/bin/ruff-quickfix`
3. Validate with `ruff-quickfix --help`
