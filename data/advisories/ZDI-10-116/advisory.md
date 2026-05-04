# ZDI-10-116: Adobe Reader CLOD Progressive Mesh Continuation Resolution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-116
- **ZDI-CAN:** ZDI-CAN-721
- **Date:** 2010-06-30
- **CVE:** CVE-2010-2202
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe, Adobe
- **Affected Products:** Acrobat, Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-116/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat and Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when the application parses a PDF file containing a malformed CLOD Progressive Mesh Continuation Resolution Update. Specific values can cause a memory corruption during floating point operations which can be subsequently leveraged to achieve arbitrary code execution under the privileges of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-15.html

## Disclosure Timeline

- 2010-03-31 - Vulnerability reported to vendor
- 2010-06-30 - Coordinated public release of advisory
