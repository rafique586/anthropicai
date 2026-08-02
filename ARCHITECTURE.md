# Architecture

This repository is a single ~12-line Python script (`main.py`) that makes one synchronous call to the Anthropic Messages API and prints the result. There is no module structure, no internal components, and no data flow beyond "build client → send one request → print response" — too small to warrant a dedicated architecture document. If this repo grows into a multi-file project, this document should be expanded to reflect the real structure at that point.
