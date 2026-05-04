# ZDI-18-678: Adobe Acrobat XPS2PDF Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-678
- **ZDI-CAN:** ZDI-CAN-6180
- **Date:** 2018-07-16
- **CVE:** CVE-2018-5056
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro
- **Credit:** Pengsu Cheng of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-678/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within XPS2PDF.api. The issue results from the lack of proper validation of a user-supplied string before using it as a format specifier. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-21.html

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2018-07-16 - Coordinated public release of advisory
- 2018-07-16 - Advisory Updated
