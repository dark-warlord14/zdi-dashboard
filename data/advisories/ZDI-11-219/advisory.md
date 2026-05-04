# ZDI-11-219: Adobe Acrobat Reader 3difr.x3d Multimedia Playing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-219
- **ZDI-CAN:** ZDI-CAN-998
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2094
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-219/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application explicitly trusting a string's length embedded within a particular file loaded by the 3difr.x3d component. The application will duplicate an arbitrarily sized string into a statically sized buffer located on the stack. This can lead to code execution under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-16.html

## Disclosure Timeline

- 2010-11-29 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
