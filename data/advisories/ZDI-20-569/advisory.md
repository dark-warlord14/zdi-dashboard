# ZDI-20-569: Adobe Bridge TIF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-569
- **ZDI-CAN:** ZDI-CAN-10018
- **Date:** 2020-04-30
- **CVE:** CVE-2020-9553
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Bridge
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-569/
## Vulnerability Details

This vulnerability allows attackers to disclose sensitive information on affected installations of Adobe Bridge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/bridge/apsb20-19.html

## Disclosure Timeline

- 2019-12-27 - Vulnerability reported to vendor
- 2020-04-30 - Coordinated public release of advisory
