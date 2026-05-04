# ZDI-18-463: Adobe Acrobat Pro DC URL Parsing Insufficient Verification of Data Authenticity Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-463
- **ZDI-CAN:** ZDI-CAN-5810
- **Date:** 2018-05-15
- **CVE:** CVE-2018-4979
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** AbdulAziz Hariri - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-463/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within URL parsing. The issue results from the lack of proper validation of user-supplied data which can allow for spoofing URL requests. An attacker can leverage this vulnerability to disclose sensitive information.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-09.html

## Disclosure Timeline

- 2018-03-06 - Vulnerability reported to vendor
- 2018-05-15 - Coordinated public release of advisory
- 2018-05-15 - Advisory Updated
