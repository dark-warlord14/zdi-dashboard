# ZDI-26-050: GIMP ICO File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-050
- **ZDI-CAN:** ZDI-CAN-28599
- **Date:** 2026-01-30
- **CVE:** CVE-2026-0797
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-050/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ICO files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GIMP has issued an update to correct this vulnerability. More details can be found at: https://gitlab.gnome.org/GNOME/gimp/-/commit/69cc6b1a6645dc9c4d7b484483dbe6a84b922b9c

## Disclosure Timeline

- 2025-12-24 - Vulnerability reported to vendor
- 2026-01-30 - Coordinated public release of advisory
- 2026-01-30 - Advisory Updated
