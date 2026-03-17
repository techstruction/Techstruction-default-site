# Techstruction Base Site

A professional, high-end digital engineering and rapid prototyping platform.

## 🚀 Project Overview
This repository contains the core Techstruction site, designed with a focus on aesthetic excellence and robust digital engineering. It is currently configured for migration to Hostinger.

## 🏗️ Technical Architecture (3-Layer System)
The project follows a modular 3-layer architecture for reliability and deterministic execution:

1.  **Layer 1: Directive (What to do)**
    - SOPs and high-level instructions located in `directives/`.
    - Defines goals, inputs, and orchestration steps.
2.  **Layer 2: Orchestration (Decision making)**
    - AI-driven routing that interprets directives and calls the appropriate execution tools.
3.  **Layer 3: Execution (Doing the work)**
    - Deterministic Python scripts in `execution/` that handle the actual "heavy lifting" (API calls, data processing, file operations).

## 📂 Repository Structure
- `index.html`, `style.css`, `script.js`: Core landing page and aesthetics.
- `directives/`: Standard Operating Procedures (Markdown).
- `execution/`: Python-based deterministic tools.
- `frontend-design/`: Distinctive UI components and design experiments.
- `public/`: Assets and public-facing files.

## 🛠️ Current Status & Migration
- **Status**: Versioned and ready for installation.
- **Git Sync**: Connected to [Techstruction-default-site](https://github.com/techstruction/Techstruction-default-site.git).
- **Branch**: `main`

## 📝 Further Development
- **Deployment**: Connect this repository to Hostinger via Git or FTP.
- **Aesthetics**: Continue using the `frontend_factory.py` tool to iterate on the "Luxury Noir" and other high-end designs.
- **Verification**: Use `execution/bootstrap_tester.py` to ensure the 3-layer architecture is intact after environment changes.
