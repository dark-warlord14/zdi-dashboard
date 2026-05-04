# ZDI-20-455: Adobe After Effects TIF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-455
- **ZDI-CAN:** ZDI-CAN-10068
- **Date:** 2020-04-15
- **CVE:** CVE-2020-3809
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** After Effects
- **Credit:** Mat Powell & Michael DePlante of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-455/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe After Effects. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIF files. Crafted data in a TIF file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/after_effects/apsb20-21.html

## Disclosure Timeline

- 2019-12-31 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
