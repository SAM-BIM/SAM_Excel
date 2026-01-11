[![Build (Windows)](https://github.com/SAM-BIM/SAM_Excel/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/SAM-BIM/SAM_Excel/actions/workflows/build.yml)
[![Installer (latest)](https://img.shields.io/github/v/release/SAM-BIM/SAM_Deploy?label=installer)](https://github.com/SAM-BIM/SAM_Deploy/releases/latest)

# SAM_Excel

<a href="https://github.com/SAM-BIM/SAM">
  <img src="https://github.com/SAM-BIM/SAM/blob/master/Grasshopper/SAM.Core.Grasshopper/Resources/SAM_Small.png"
       align="left" hspace="10" vspace="6">
</a>

**SAM_Excel** is part of the **SAM (Sustainable Analytical Model) Toolkit** —  
an open-source collection of tools designed to help engineers create, manage,
and process analytical building models for energy and environmental analysis.

This repository provides **integration utilities between SAM, Rhino Grasshopper, and Microsoft Excel**,
enabling analytical data to be exchanged between parametric workflows
and spreadsheet-based environments.

The integration supports using Excel as a lightweight interface for
data input, inspection, and post-processing within SAM-based workflows.

Welcome — and let’s keep the open-source journey going. 🤝

---

## Features

- Exchange of data between SAM analytical models and Excel
- Integration with Grasshopper-based parametric workflows
- Support for spreadsheet-driven input and output
- Lightweight inspection and post-processing of analytical results

---

## Resources
- 📘 **SAM Wiki:** https://github.com/SAM-BIM/SAM/wiki  
- 🧠 **SAM Core:** https://github.com/SAM-BIM/SAM  
- 🦏 **Rhino / Grasshopper:** https://www.rhino3d.com/  
- 📊 **Microsoft Excel:** https://www.microsoft.com/excel  

---

## Installing

To install **SAM** using the Windows installer, download and run the  
[latest installer](https://github.com/SAM-BIM/SAM_Deploy/releases/latest).

Alternatively, you can build the toolkit from source using Visual Studio.  
See the main repository for details:  
👉 https://github.com/SAM-BIM/SAM

---

## Development notes

- Target framework: **.NET / C#**
- Excel integration follows SAM-BIM data and modelling conventions
- Grasshopper components provide the primary interaction layer
- New or modified `.cs` files must include the SPDX header from `COPYRIGHT_HEADER.txt`

---

## Licence

This repository is free software licensed under the  
**GNU Lesser General Public License v3.0 or later (LGPL-3.0-or-later)**.

Each contributor retains copyright to their respective contributions.  
The project history (Git) records authorship and provenance of all changes.

See:
- `LICENSE`
- `NOTICE`
- `COPYRIGHT_HEADER.txt`
