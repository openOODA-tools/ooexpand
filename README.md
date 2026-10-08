# ooexpand: Sovereign POSIX Tab Expander & Indentation Auditor

<div align="center">

```
================================================================================
                                ooexpand
               Sovereign openOODA TAB EXPANDER
================================================================================
```

**Sovereign POSIX Tab Expander, Whitespace Visualizer, and Indentation Auditor**  
*Converts tab characters to spaces with custom tab-stop positions, visual alignment, and indentation hygiene analysis.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure native [openOODA](https://github.com/openOODA) (`.oo`).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Version: 0.2.0](https://img.shields.io/badge/version-0.2.0-blue.svg)](https://github.com/openOODA-tools/ooexpand/releases/tag/v0.2.0)
[![Architecture: x86_64](https://img.shields.io/badge/Arch-x86__64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64)
```bash
curl -fsSL https://openooda-tools.github.io/ooexpand/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (PKGBUILD)
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/ooexpand/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/ooexpand/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
ooexpand-uninstall
# or: curl -fsSL https://openooda-tools.github.io/ooexpand/uninstall.sh | bash
```

---

## 2. CLI Usage & Capabilities

```
usage: ooexpand [options] [FILE]...

Convert tab characters to spaces with custom tab-stop positions and alignment.

POSIX Options:
  -i, --initial         do not convert tabs after non blanks
  -t, --tabs=N          have tabs N characters apart, not 8
  -t, --tabs=LIST       use comma-separated list of explicit tab positions

Sovereign Diagnostic & Inspection Extensions:
      --visualize       render column ruler and highlight tab locations
      --audit           audit indentation hygiene for mixed whitespace and errors
  -j, --json            output formatted as structured JSON Lines stream
  -D, --demo            synthetic multi-scenario code showcase
      --mcp             run as Model Context Protocol (MCP) stdio server
      --test            run internal substrate anchor verification tests
  -h, --help            display this help and exit
  -v, --version         output version information and exit
```

---

## 3. Whitespace & Indentation Auditing

`ooexpand` features built-in static analysis heuristics to detect indentation anomalies and mixed whitespace:
* **Space Before Tab:** Detects spaces preceding tab characters in leading indentation (inconsistent alignment defect).
* **Mixed Indentation:** Identifies lines with discordant mixtures of tabs and space sequences.
* **Trailing Tabs:** Identifies redundant trailing tab characters at end-of-line.

---

## 4. Model Context Protocol (MCP) Stdio Server

When invoked with `--mcp`, `ooexpand` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

| Tool | Description |
| :--- | :--- |
| `expand_text` | Convert tabs to spaces with custom tab stops and initial-only indentation rules |
| `expand_file` | Read code samples or file buffers and expand tab alignment |
| `expand_analyze` | Audit indentation hygiene and report defect coordinates |
| `expand_visualize` | Render text with visual column ruler and tab marker indicators |
| `expand_demo` | Multi-scenario sovereign tab expansion showcase |

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
