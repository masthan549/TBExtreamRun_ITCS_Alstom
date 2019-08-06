@echo on
set tcfname=%1
set tcfpath=%2
set cfile=%3
set ldrapath1=%4

start /wait/B %ldrapath1%\Contbrun.exe >%tcfpath%\"%tcfname%_log.txt" 2>&1 "%cfile%" -tcf=%tcfpath%\%tcfname% -delete_results -ibox=l -regress -unit_publish_to=%tcfpath% -quit

