# ZDI-20-657: (Pwn2Own) Schneider Electric EcoStructure Operator Terminal Expert ZIP Path Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-657
- **ZDI-CAN:** ZDI-CAN-10280
- **Date:** 2020-05-14
- **CVE:** CVE-2020-7495
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Operator Terminal Expert
- **Credit:** Sharon Brizinov, Amir Preminger of Claroty Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-657/
## Vulnerability Details

The vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric EcoStructure Operator Terminal Expert. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists with the handling of ZIP files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.se.com/ww/en/download/document/SEVD-2020-133-04/

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-05-14 - Coordinated public release of advisory
