# ZDI-11-218: Adobe Acrobat Reader tesselate.x3d Multimedia Playing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-218
- **ZDI-CAN:** ZDI-CAN-999
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2095
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-218/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application explicitly trusting a string's length embedded within a particular file that is loaded by the tesselate.x3d plugin. The application will duplicate an arbitrarily sized string from the file into a statically sized buffer located on the stack. This can lead to code execution under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-16.html

## Disclosure Timeline

- 2010-11-29 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
