@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title File Repair System - Spinner

:: --- НАСТРОЙКИ ---
set "max_folders=3"
set "files_per_folder=10"
set "seconds_per_file=15"
:: ----------------

set /a "total_files=%max_folders% * %files_per_folder%"
set /a "total_seconds=%total_files% * %seconds_per_file%"
set /a "total_minutes=%total_seconds% / 60"
set /a "remaining_seconds=%total_seconds% %% 60"

cls
echo Files Repair System:
echo.
echo Directory: "C:\Program Files (x86)\Microsoft Visual Studio\Installer"
echo Folders to process: %max_folders%
echo Files to repair: %total_files%
echo Estimated time: %total_minutes% min %remaining_seconds% sec
echo.

for /L %%t in (3,-1,1) do (
    cls
    echo Files Repair System:
    echo.
    echo Directory: "C:\Program Files (x86)\Microsoft Visual Studio\Installer"
    echo Folders to process: %max_folders%
    echo Files to repair: %total_files%
    echo Estimated time: %total_minutes% min %remaining_seconds% sec
    echo.
    echo Starting in %%t seconds...
    ping -n 2 127.0.0.1 >nul
)

set "last_folder_name="
set "last_file_name="
set /a "file_counter=0"
set /a "errors_count=0"
set /a "warnings_count=0"

for /L %%f in (1,1,%max_folders%) do (
    set /a "r1=!random! %% 5"
    if !r1!==0 set "current_folder_name=Data_Core_v1"
    if !r1!==1 set "current_folder_name=Sys_Engine_dev"
    if !r1!==2 set "current_folder_name=Backup_Sensor_old"
    if !r1!==3 set "current_folder_name=Log_Adapter_test"
    if !r1!==4 set "current_folder_name=Config_Driver_prod"

    for /L %%i in (1,1,%files_per_folder%) do (
        set /a "r2=!random! %% 6"
        if !r2!==0 set "current_file_name=report_001.dat"
        if !r2!==1 set "current_file_name=config_main.cfg"
        if !r2!==2 set "current_file_name=log_error.log"
        if !r2!==3 set "current_file_name=backup_full.zip"
        if !r2!==4 set "current_file_name=image_raw.png"
        if !r2!==5 set "current_file_name=script_run.bat"

        set "last_folder_name=!current_folder_name!"
        set "last_file_name=!current_file_name!"
        set /a "file_counter+=1"

        cls
        echo Directory: "C:\Program Files (x86)\Microsoft Visual Studio\Installer"
        echo.
        echo folder: !current_folder_name!
        echo file: !current_file_name!
        echo File !file_counter! of %total_files%
        echo.
        echo Initialization of the file...
        ping -n 1 127.0.0.1 >nul

        set /a "rnd_err=!random! %% 100"
        set "has_error=0"
        if !rnd_err! LSS 15 set "has_error=1"

        set /a "rnd_warn=!random! %% 100"
        set "warn_count_this_file=0"
        if !rnd_warn! LSS 50 (
            set "warn_count_this_file=0"
        ) else if !rnd_warn! LSS 85 (
            set "warn_count_this_file=1"
        ) else (
            set "warn_count_this_file=2"
        )

        if !has_error!==1 set /a "errors_count+=1"
        set /a "warnings_count+=!warn_count_this_file!"

        echo Processing...
        echo Please wait. Repairing...
        echo.
        
        for /L %%k in (1,1,%seconds_per_file%) do (
            cls
            echo Directory: "C:\Program Files (x86)\Microsoft Visual Studio\Installer"
            echo.
            echo folder: !current_folder_name!
            echo file: !current_file_name!
            echo File !file_counter! of %total_files%
            echo.
            
            :: --- СПИННЕР (| / - \) ---
            set /a "spin_idx=(%%k - 1) %% 4"
            if !spin_idx!==0 set "spinner=|"
            if !spin_idx!==1 set "spinner=/"
            if !spin_idx!==2 set "spinner=-"
            if !spin_idx!==3 set "spinner=\"
            :: -------------------------

            set /a "percent=(%%k * 100) / %seconds_per_file%"
            set /a "bars=(percent * 30) / 100"
            set /a "spaces=30 - bars"

            set "bar_str=["
            for /L %%b in (1,1,!bars!) do set "bar_str=!bar_str!#"
            for /L %%s in (1,1,!spaces!) do set "bar_str=!bar_str!-"
            set "bar_str=!bar_str!]  !percent!%%"

            :: Таймер ЧЧ:ММ:СС
            set /a "time_left=%seconds_per_file% - %%k"
            set /a "t_h=time_left / 3600"
            set /a "t_m=(time_left %% 3600) / 60"
            set /a "t_s=time_left %% 60"

            if !t_h! LSS 10 set "t_h=0!t_h!"
            if !t_m! LSS 10 set "t_m=0!t_m!"
            if !t_s! LSS 10 set "t_s=0!t_s!"

            echo [!spinner!]  Repairing file...
            echo.
            echo Progress: !bar_str!
            echo Time left: !t_h!:!t_m!:!t_s!
            echo.
            echo Errors: !errors_count!
            echo Warnings: !warnings_count!

            ping -n 1 127.0.0.1 >nul
        )
        
        echo.
        echo [File repaired]
        echo.
        ping -n 1 127.0.0.1 >nul
    )
)

cls
echo REPAIR COMPLETE
echo.
echo Directory: "C:\Program Files (x86)\Microsoft Visual Studio\Installer"
echo.
echo Total folders processed: %max_folders%
echo Total files repaired: %total_files%
echo.
echo Last folder: !last_folder_name!
echo Last file:   !last_file_name!
echo.
echo All systems stabilized.
echo System integrity: 100%
echo.
echo Final stats:
echo Errors: !errors_count!
echo Warnings: !warnings_count!
endlocal
