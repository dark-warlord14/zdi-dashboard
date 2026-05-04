# ZDI-11-075: Adobe Acrobat Reader rt3d.dll Multimedia Playing Arbitrary Memory Overwite Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-075
- **ZDI-CAN:** ZDI-CAN-1003
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0606
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-075/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the rt3d.dll component explicitly trusting a length embedded within a particular file in order to calculate the length of a buffer. The application will then duplicate an arbitrarily sized string into a statically sized buffer located on the stack. This can lead to code execution under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-03.html

## Disclosure Timeline

- 2010-11-29 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
