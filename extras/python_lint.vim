" File:        ~/vimfiles/python_lint.vim
" Author:      Neal Joslin
" Date:        2024-08-17
" Email:       neal@joslin.io
" Description: user defined functions file example

" Python Make
function! s:RuffMake()
    setlocal makeprg=ruff-quickfix\ %
    setlocal errorformat=%f:%l:%c:%t:%m
    let g:python_make_type = 0
endfunction
function! s:PylintMake()
    setlocal makeprg=pylint\ --output-format=text\ --msg-template=\"{path}:{line}:{column}:{C}:\ [{symbol}]\ {msg}\"\ --reports=no\ %
    setlocal errorformat=%A%f:%l:%c:%t:\ %m,%A%f:%l:\ %m,%A%f:(%l):\ %m,%-Z%p^%.%#,%-G%.%#
    let g:python_make_type = 1
endfunction

command Ruff call s:RuffMake()
command Pylint call s:PylintMake()

" Python Directory Make
function! s:DirRuffMake()
    let l:_errorformat = &errorformat
    set errorformat=%f:%l:%c:%t:%m
    cexpr system( "ruff-quickfix " .. expand("%:p:h") )
    let &errorformat=l:_errorformat
endfunction
function! s:DirPylintMake()
    let l:_errorformat = &errorformat
    set errorformat=%A%f:%l:%c:%t:\ %m,%A%f:%l:\ %m,%A%f:(%l):\ %m,%-Z%p^%.%#,%-G%.%#
    cexpr system( "pylint --output-format=text --msg-template='{path}:{line}:{column}:{C}: [{symbol}] {msg}' --reports=no " .. expand("%:p:h") )
    let &errorformat = l:_errorformat 
endfunction

command Druff call s:DirRuffMake()
command Dpylint call s:DirPylintMake()

" Python Project Make
function! s:ProjectRuffMake()
    let l:_errorformat = &errorformat
    set errorformat=%f:%l:%c:%t:%m
    cexpr system( "ruff-quickfix " .. getcwd() )
    let &errorformat=l:_errorformat
endfunction
function! s:ProjectPylintMake()
    let l:_errorformat = &errorformat
    set errorformat=%A%f:%l:%c:%t:\ %m,%A%f:%l:\ %m,%A%f:(%l):\ %m,%-Z%p^%.%#,%-G%.%#
    cexpr system( "pylint --output-format=text --msg-template='{path}:{line}:{column}:{C}: [{symbol}] {msg}' --reports=no " .. getcwd() )
    let &errorformat = l:_errorformat 
endfunction

command Pruff call s:ProjectRuffMake()
command Ppylint call s:ProjectPylintMake()

