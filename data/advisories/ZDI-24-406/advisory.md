# ZDI-24-406: Adobe After Effects AEP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-406
- **ZDI-CAN:** ZDI-CAN-22173
- **Date:** 2024-04-26
- **CVE:** CVE-2023-48633
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** After Effects
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-406/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe After Effects. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of AEP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/after_effects/apsb23-75.html

## Disclosure Timeline

- 2023-09-20 - Vulnerability reported to vendor
- 2024-04-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
