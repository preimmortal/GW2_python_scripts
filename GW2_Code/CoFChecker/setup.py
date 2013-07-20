from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('cofcheck.py', 'Console')
]

setup(name='cofservers',
      version = '1.0',
      description = 'Find Open Citadel of Flame Servers',
      options = dict(build_exe = buildOptions),
      executables = executables)
