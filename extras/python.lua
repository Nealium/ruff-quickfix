-- File:        ~/.config/nvim/after/ftplugin/python.lua
-- Author:      Neal Joslin
-- Date:        2024-08-17
-- Email:       neal@joslin.io
-- Description: ftplugin file example

if vim.g.python_make_type == 0 then
    vim.opt.makeprg = [[ruff-quickfix %]]
    vim.opt.errorformat = [[%f:%l:%c:%t:%m]]
elseif vim.g.python_make_type == 1 then
    vim.bo.makeprg =
        [[pylint --output-format=text --msg-template="{path}:{line}:{column}:{C}: [{symbol}] {msg}" --reports=no %]]
    vim.bo.errorformat =
        [[%A%f:%l:%c:%t: %m,%A%f:%l: %m,%A%f:(%l): %m,%-Z%p^%.%#,%-G%.%#]]
end
