# autoRsync
A tool for connecting compatible devices to internal Rsync framework for data preservation


Requirements: 
- Currently requires volumes to be mounted to system that autoRsync is being run on, ssh capability soon
- ```requirements.txt``` needs to be installed before use

Supported OS's:
- Linux (x86 and ARM)
- MacOS (x86 and ARM)
- Windows (x86 only)
- FreeBSD

Installation: 
- ```pip3 install -r requirements.txt```
- ```python3 autoRsync.py```


Testing:
- Built with both PyTest and Rust for complete code coverage.
- Covers functionality for all four supported operating systems as well as both ARM and x86 platforms.
- Will eventually call an existing S3 container for proper testing

Upcoming (in no particular order):

- Automated syncing with cron
- Progress bar, general user friendliness
- SSH Support
- Full test coverage with Pytest and Rust
- Code coverage reports via Codecov

Contributing:
- Please send a pull request with any changes or updates that you may find necessary
