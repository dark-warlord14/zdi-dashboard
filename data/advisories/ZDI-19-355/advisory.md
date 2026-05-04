# ZDI-19-355: Adobe Bridge CC PDF File Parsing Unexpected Sign Extension Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-355
- **ZDI-CAN:** ZDI-CAN-7766
- **Date:** 2019-04-15
- **CVE:** CVE-2019-7137
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Bridge
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-355/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Bridge CC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in an unexpected sign extension before reading memory. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/bridge/apsb19-25.html

## Disclosure Timeline

- 2019-01-03 - Vulnerability reported to vendor
- 2019-04-15 - Coordinated public release of advisory
