# ZDI-22-053: Open Design Alliance (ODA) Drawings Explorer JPG File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-053
- **ZDI-CAN:** ZDI-CAN-14727
- **Date:** 2022-01-13
- **CVE:** CVE-2022-23095
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Open Design Alliance (ODA)
- **Affected Products:** Drawings Explorer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-053/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Open Design Alliance (ODA) Drawings Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPG files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Open Design Alliance (ODA) has issued an update to correct this vulnerability. More details can be found at: https://www.opendesign.com/security-advisories

## Disclosure Timeline

- 2021-07-30 - Vulnerability reported to vendor
- 2022-01-13 - Coordinated public release of advisory
