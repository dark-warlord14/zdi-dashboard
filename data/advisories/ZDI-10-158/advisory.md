# ZDI-10-158: IBM Lotus Notes Autonomy KeyView WK3 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-158
- **ZDI-CAN:** ZDI-CAN-639
- **Date:** 2010-08-23
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM, Autonomy
- **Affected Products:** KeyView
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-158/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Notes Email Client. User interaction is required to exploit this vulnerability in that the target must open a malicious email attachment. The specific flaw exists within the Lotus Notes file viewer utilizing the KeyView SDK to render a malformed .wk3 document. The application will mistrust a length used to allocate a buffer. Later, the application will use a differently calculated length in a copy used to initialize that buffer. This leads to a buffer overflow and can lead to code execution under the context of the application.

## Additional Details

Autonomy corrected the above issues in the patch releases of versions 10.10, 10.8, 10.4, 9.2, 7.4 of IDOL Keyview on February 28, 2010. IBM states: http://www-01.ibm.com/support/docview.wss?rs=463&uid=swg21440812

## Disclosure Timeline

- 2010-01-22 - Vulnerability reported to vendor
- 2010-08-23 - Coordinated public release of advisory
