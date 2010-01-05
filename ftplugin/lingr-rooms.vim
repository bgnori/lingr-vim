if exists("b:did_ftplugin")
    finish
endif

setlocal statusline=lingr-rooms
set buftype=nofile
set noswapfile
set bufhidden=hide
setlocal foldcolumn=0

function! s:select_room()
    python <<EOM
# coding=utf-8
bufnum, lnum, col, off = vim.eval('getpos(".")')
lingr_vim.select_room_by_lnum(int(lnum))
vim.eval('setpos(".", [%s, %s, %s, %s])' % (bufnum, lnum, col, off))
EOM
endfunction

nnoremap <buffer> <silent> <Plug>(lingr-vim-select-room)
            \ :<C-u>call <SID>select_room()<CR>
nmap <buffer> <silent> <CR> <Plug>(lingr-vim-select-room)

let b:undo_ftplugin = 'setlocal statusline<'
            \ . '| set buftype&'
            \ . '| set swapfile&'
            \ . '| set bufhidden&'
            \ . '| setlocal foldcolumn<'
            \ . '| setlocal modifiable<'
            \ . '| nunmap <buffer> <CR>'

let b:did_ftplugin = 1
