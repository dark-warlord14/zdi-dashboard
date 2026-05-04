# ZDI-23-069: Adobe InDesign Font Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-069
- **ZDI-CAN:** ZDI-CAN-19354
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21588
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** InDesign
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-069/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe InDesign. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of embedded fonts. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/indesign/apsb23-07.html

## Disclosure Timeline

- 2022-10-28 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
