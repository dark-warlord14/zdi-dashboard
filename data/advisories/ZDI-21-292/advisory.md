# ZDI-21-292: SAP 3D Visual Enterprise Viewer HPGL File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-292
- **ZDI-CAN:** ZDI-CAN-12116
- **Date:** 2021-03-15
- **CVE:** CVE-2021-27588
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-292/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of HPGL files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in SAP 3D Visual Enterprise Viewer 9.0 FP10 MP2

## Disclosure Timeline

- 2020-11-13 - Vulnerability reported to vendor
- 2021-03-15 - Coordinated public release of advisory
