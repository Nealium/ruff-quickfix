-- File:        ~/.config/nvim/python_lint.lua
-- Author:      Neal Joslin
-- Date:        2024-08-17
-- Email:       neal@joslin.io
-- Description: user defined functions file example

-- Python Make Helper
function OptRuffErrorFmt()
    vim.opt.errorformat = [[%f:%l:%c:%t:%m]]
end
function OptPylintErrorFmt()
    vim.opt.errorformat =
        [[%A%f:%l:%c:%t: %m,%A%f:%l: %m,%A%f:(%l): %m,%-Z%p^%.%#,%-G%.%#]]
end

-- Python Make
vim.api.nvim_create_user_command("Ruff", function()
    vim.opt.makeprg = [[ruff-quickfix %]]
    OptRuffErrorFmt()
    vim.g.python_make_type = 0
end, {})
vim.api.nvim_create_user_command("Pylint", function()
    vim.opt.makeprg =
        [[pylint --output-format=text --msg-template="{path}:{line}:{column}:{C}: [{symbol}] {msg}" --reports=no %]]
    OptPylintErrorFmt()
    vim.g.python_make_type = 1
end, {})

-- Python Directory Make
vim.api.nvim_create_user_command("Druff", function()
    local _errorformat = vim.opt.errorformat
    OptRuffErrorFmt()
    vim.g._cexpr = vim.fn.system({ "ruff-quickfix", vim.fn.expand("%:p:h") })
    vim.cmd([[:cexpr g:_cexpr]])
    vim.opt.errorformat = _errorformat
end, {})
vim.api.nvim_create_user_command("Dpylint", function()
    local _errorformat = vim.opt.errorformat
    OptPylintErrorFmt()
    vim.g._cexpr = vim.fn.system({
        "pylint",
        "--output-format=text",
        "--msg-template='{path}:{line}:{column}:{C}: [{symbol}] {msg}'",
        "--reports=no",
        vim.fn.expand("%:p:h"),
    })
    vim.cmd([[:cexpr g:_cexpr]])
    vim.opt.errorformat = _errorformat
end, {})

-- Python Project Make
vim.api.nvim_create_user_command("Pruff", function()
    local _errorformat = vim.opt.errorformat
    OptRuffErrorFmt()
    vim.g._cexpr = vim.fn.system({ "ruff-quickfix", vim.fn.getcwd() })
    vim.cmd([[:cexpr g:_cexpr]])
    vim.opt.errorformat = _errorformat
end, {})
vim.api.nvim_create_user_command("Ppylint", function()
    local _errorformat = vim.opt.errorformat
    OptPylintErrorFmt()
    vim.g._cexpr = vim.fn.system({
        "pylint",
        "--output-format=text",
        "--msg-template='{path}:{line}:{column}:{C}: [{symbol}] {msg}'",
        "--reports=no",
        vim.fn.getcwd(),
    })
    vim.cmd([[:cexpr g:_cexpr]])
    vim.opt.errorformat = _errorformat
end, {})

