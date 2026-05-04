# ZDI-19-351: Adobe Bridge CC PNG File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-351
- **ZDI-CAN:** ZDI-CAN-7585
- **Date:** 2019-04-15
- **CVE:** CVE-2019-7134
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Bridge
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-351/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Bridge CC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PNG files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/bridge/apsb19-25.html

## Disclosure Timeline

- 2018-11-21 - Vulnerability reported to vendor
- 2019-04-15 - Coordinated public release of advisory
