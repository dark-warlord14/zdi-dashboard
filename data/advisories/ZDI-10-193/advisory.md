# ZDI-10-193: Adobe Acrobat Reader Multimedia Playing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-193
- **ZDI-CAN:** ZDI-CAN-868
- **Date:** 2010-10-06
- **CVE:** CVE-2010-3632
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-193/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application explicitly trusting a string's length embedded within a particular file format. The application will duplicate an arbitrarily sized string into a statically sized buffer located on the stack. This can lead to code execution under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-21.html

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2010-10-06 - Coordinated public release of advisory
