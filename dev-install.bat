xcopy actions %APPDATA%\krita\actions /Y

del %APPDATA%\krita\pykrita\TenBrushSizesPlugin /Q
xcopy TenBrushSizesPlugin.desktop %APPDATA%\krita\pykrita /Y
xcopy TenBrushSizesPlugin %APPDATA%\krita\pykrita\TenBrushSizesPlugin\ /Y
