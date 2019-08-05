@echo on
set "tcfname=ProcessMsgs.tcf"
set "tcfpath=C:\SCM\IWP\VPM-3 DO-WCM\Software Engineering\V&V\Unit Test\VPM_3 AB Exec\Unit Test Scripts\mmb.c"
set "cfile=C:\SCM\IWP\VPM-3 DO-WCM\Software Engineering\VPM_3 AB Exec\Code\services\os\mmb.c"
set "ldrapath1=C:\LDRA_Toolsuite"

start /wait/B %ldrapath1%\Contbrun.exe >"%tcfpath%"\"%tcfname%_log.txt" 2>&1 "%cfile%" -tcf="%tcfpath%\%tcfname%" -delete_results -ibox=l -regress -unit_publish_to="C:\SCM\IWP\VPM-3 DO-WCM\Software Engineering\V&V\Unit Test\VPM_3 AB Exec\Unit Test Scripts\mmb.c" -quit

