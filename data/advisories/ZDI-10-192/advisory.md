# ZDI-10-192: Adobe Acrobat Reader ICC mluc Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-192
- **ZDI-CAN:** ZDI-CAN-719
- **Date:** 2010-10-06
- **CVE:** CVE-2010-3622
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-192/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required in that a target must be coerced into opening a file or visiting a web page. The specific flaw exists within the ACE.dll module responsible for parsing ICC streams. Within the 'desc' tag there exists an embedded 'mluc' data structure. The code within ACE performs arithmetic on the second DWORD from the mluc structure and a value from the desc structure. The resulting integer is used for an allocation of a heap-based buffer. An attacker can forge these values to force the process to under-allocate this buffer and later overflow it during a copy operation. This leads to remote code execution under the context of the user running the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-21.html

## Disclosure Timeline

- 2010-06-23 - Vulnerability reported to vendor
- 2010-10-06 - Coordinated public release of advisory
