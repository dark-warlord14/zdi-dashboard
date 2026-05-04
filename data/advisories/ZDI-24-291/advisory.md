# ZDI-24-291: Adobe Bridge PS File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-291
- **ZDI-CAN:** ZDI-CAN-22653
- **Date:** 2024-03-13
- **CVE:** CVE-2024-20752
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Bridge
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-291/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Bridge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PS files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/bridge/apsb24-15.html

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2024-03-13 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
