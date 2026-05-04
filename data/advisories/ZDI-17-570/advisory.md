# ZDI-17-570: Adobe Reader DC URL Parsing Insufficient Verification of Data Authenticity Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-570
- **ZDI-CAN:** ZDI-CAN-4369
- **Date:** 2017-08-08
- **CVE:** CVE-2017-3115
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Fernando Munoz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-570/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within URL parsing. The issue results from the lack of proper validation of user-supplied data which can allow for spoofing URL requests. An attacker can leverage this vulnerability to leak sensitive information.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-24.html

## Disclosure Timeline

- 2017-01-09 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
