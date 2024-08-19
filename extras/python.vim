" File:        ~/vimfiles/ftplugin/python.vim
" Author:      Neal Joslin
" Date:        2024-08-17
" Email:       neal@joslin.io
" Description: ftplugin file example

if g:python_make_type == 0
    setlocal makeprg=ruff-quickfix\ %
    setlocal errorformat=%f:%l:%c:%t:%m
elseif g:python_make_type == 1
    setlocal makeprg=pylint\ --output-format=text\ --msg-template=\"{path}:{line}:{column}:{C}:\ [{symbol}]\ {msg}\"\ --reports=no\ %
    setlocal errorformat=%A%f:%l:%c:%t:\ %m,%A%f:%l:\ %m,%A%f:(%l):\ %m,%-Z%p^%.%#,%-G%.%#
endif
