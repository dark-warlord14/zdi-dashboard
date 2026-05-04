# ZDI-24-1319: Autodesk Navisworks Freedom DWF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1319
- **ZDI-CAN:** ZDI-CAN-24496
- **Date:** 2024-10-02
- **CVE:** CVE-2024-7672
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** Navisworks Freedom
- **Credit:** Vladislav Berghici
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1319/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk Navisworks Freedom. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2024-0015

## Disclosure Timeline

- 2024-06-26 - Vulnerability reported to vendor
- 2024-10-02 - Coordinated public release of advisory
- 2024-10-02 - Advisory Updated
