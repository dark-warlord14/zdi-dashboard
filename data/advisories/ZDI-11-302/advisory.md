# ZDI-11-302: Adobe Reader U3D TIFF Resource Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-302
- **ZDI-CAN:** ZDI-CAN-1197
- **Date:** 2011-10-26
- **CVE:** CVE-2011-2432
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-302/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within because Adobe Reader X includes an old version of libtiff. Adobe can be tricked in using this library by parsing a specially crafted PDF file containing U3D data. Due to the old version of libtiff Adobe Reader is vulnerable to the issue described in CVE-2006-3459 which can be leveraged to execute remote code under the context of the user running the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
