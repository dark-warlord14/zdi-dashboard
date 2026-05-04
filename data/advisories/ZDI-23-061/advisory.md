# ZDI-23-061: Adobe Acrobat Reader DC resetForm Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-061
- **ZDI-CAN:** ZDI-CAN-19240
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21608
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Ashfaq Ansari and Krishnakant Patil - HackSys Inc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-061/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the resetForm method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb23-01.html

## Disclosure Timeline

- 2022-11-04 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
