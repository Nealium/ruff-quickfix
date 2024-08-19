<!-- markdownlint-disable MD033 MD041 MD024 -->
<div align="center">

# ruff-quickfix

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge)](https://python-poetry.org/)

![Python 3.8](http://img.shields.io/badge/python-3.8-3776AB.svg)
![Python 3.9](http://img.shields.io/badge/python-3.9-3776AB.svg)
![Python 3.10](http://img.shields.io/badge/python-3.10-3776AB.svg)
![Python 3.11](http://img.shields.io/badge/python-3.11-3776AB.svg)
![Python 3.12](http://img.shields.io/badge/python-3.12-3776AB.svg)

</div>

This is a simple wrapper for the Python linter [ruff](https://github.com/astral-sh/ruff)
that allows it to be easily used with (neo)vim's quickfix.

**Why?** I like Vim's quickfix and find it more useful in some situations over
using an LSP. Also this is an excuse to learn publishing.

![Screenshot](screenshot.png)

## Config

### Neovim

* **Location:** `~/.config/nvim/after/ftplugin/python.lua`

``` lua
vim.opt.makeprg = [[ruff-quickfix %]]
vim.opt.errorformat = [[%f:%l:%c:%t:%m]]
```

### Vim

* Linux: `~/.vim/ftplugin/python.lua`
* Windows: `~/.vimfiles/ftplugin/python.lua`

```vim
setlocal makeprg=ruff-quickfix\ %
setlocal errorformat=%f:%l:%c:%t:%m
```

## Usage

The command can be manually called from any Python file by calling the ex
command `:make`, which will lint your current buffer. I would recommend the
plugin [vim-qf](https://github.com/romainl/vim-qf) for some quickfix niceties.

## Advanced Usage

The main benefit of using the quickfix with a linter is that you can do more
wider scope lints, example: the entire project, and have **all**
errors in a single quickfix! This requires making custom user commands

### Neovim

```lua
-- Current directory of focused buffer `:Druff`
vim.api.nvim_create_user_command("Druff", function()
    local _errorformat = vim.opt.errorformat
    vim.opt.errorformat = [[%f:%l:%c:%t:%m]]
    vim.g._cexpr = vim.fn.system({ "ruff-quickfix", vim.fn.expand("%:p:h") })
    vim.cmd([[:cexpr g:_cexpr]])
    vim.opt.errorformat = _errorformat
end, {})

-- Current working directory, "project wide" `:Pruff`
vim.api.nvim_create_user_command("Pruff", function()
    local _errorformat = vim.opt.errorformat
    vim.opt.errorformat = [[%f:%l:%c:%t:%m]]
    vim.g._cexpr = vim.fn.system({ "ruff-quickfix", vim.fn.getcwd() })
    vim.cmd([[:cexpr g:_cexpr]])
    vim.opt.errorformat = _errorformat
end, {})
```

### Vim

```vim
" Current Directory of focused buffer `:Druff`
function! s:DirRuffMake()
    let l:_errorformat = &errorformat
    set errorformat=%f:%l:%c:%t:%m
    cexpr system( "ruff-quickfix " .. expand("%:p:h") )
    let &errorformat = l:_errorformat 
endfunction
command Druff call s:DirRuffMake()

-- Current working directory, "project wide" `:Pruff`
function! s:ProjectRuffMake()
    let l:_errorformat = &errorformat
    set errorformat=%A%f:%l:%c:%t:\ %m,%A%f:%l:\ %m,%A%f:(%l):\ %m,%-Z%p^%.%#,%-G%.%#
    cexpr system( "pylint --output-format=text --msg-template='{path}:{line}:{column}:{C}: [{symbol}] {msg}' --reports=no " .. expand("%:p:h") )
    let &errorformat = l:_errorformat 
endfunction
command Pruff call s:ProjectRuffMake()
```

## Extras

Inside the extras directory you will find files that allow you to easily toggle
between pylint and ruff, as well as a standalone file of ruff-quickfix.
