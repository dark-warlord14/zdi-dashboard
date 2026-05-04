# ZDI-21-324: Siemens Solid Edge Viewer ZIP Path Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-324
- **ZDI-CAN:** ZDI-CAN-11983
- **Date:** 2021-03-16
- **CVE:** CVE-2021-22651
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-324/
## Vulnerability Details

The vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ZIP files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-035-01

## Disclosure Timeline

- 2020-11-11 - Vulnerability reported to vendor
- 2021-03-16 - Coordinated public release of advisory
