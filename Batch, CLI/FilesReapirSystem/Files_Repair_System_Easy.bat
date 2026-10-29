@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title Files repair system

:: --- НАСТРОЙКИ ---
set "max_folders=7"       :: всего папок на починку
set "files_per_folder=42" :: всего файлов на починку
set "seconds_per_file=20" :: время починки одного файла (сек)
:: ----------------

:: Считаем общее количество файлов и примерное время
set /a "total_files=%max_folders% * %files_per_folder%"
set /a "total_seconds=%total_files% * %seconds_per_file%"
set /a "total_minutes=%total_seconds% / 60"
set /a "remaining_seconds=%total_seconds% %% 60"

:: Экран-заставка с планом
cls
echo Files Repair System:
echo.
echo Directory: "C:\Program Files (x86)\Microsoft Visual Studio\Installer"
echo Folders to process: %max_folders%
echo Files to repair: %total_files%
echo Estimated time: %total_minutes% min %remaining_seconds% sec
echo.
echo Starting in 5 seconds...
timeout /t 5 /nobreak >nul

set "last_folder=1"
set "last_file=1"

:: Основной цикл: папки -> файлы
for /L %%f in (1,1,%max_folders%) do (
    for /L %%i in (1,1,%files_per_folder%) do (
        set "num_folder=%%f"
        set "num_file=%%i"

        cls
        echo Directory: "C:\Program Files (x86)\Microsoft Visual Studio\Installer"
        echo.
        echo Folder: #!num_folder!, file: #!num_file!:
        echo.
        echo Initialization of the file...
        timeout /t 3 /nobreak >nul

        :: Анимация пульсации точек (каждую секунду)
        for /L %%k in (1,1,%seconds_per_file%) do (
            cls
            echo Directory: "C:\Program Files (x86)\Microsoft Visual Studio\Installer"
            echo.
            echo Folder: #!num_folder!, file: #!num_file!:
            echo.

            set /a "dot_count=(%%k - 1) %% 4"
            if !dot_count!==0 (
                echo This process may take some time.
                echo Please wait. Repairing
            ) else if !dot_count!==1 (
                echo This process may take some time.
                echo Please wait. Repairing.
            ) else if !dot_count!==2 (
                echo This process may take some time.
                echo Please wait. Repairing..
            ) else (
                echo This process may take some time.
                echo Please wait. Repairing...
            )

            timeout /t 1 /nobreak >nul
        )

    )
)

:: Финальный экран со статистикой
cls
echo Files are repared!
echo.
echo Total folders processed: %max_folders%
echo Total files repaired: %total_files%
pause
endlocal
