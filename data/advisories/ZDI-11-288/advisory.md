# ZDI-11-288: Microsoft Internet Explorer Select Element Insufficient Type Checking Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-288
- **ZDI-CAN:** ZDI-CAN-1300
- **Date:** 2011-10-15
- **CVE:** CVE-2011-1999
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ivan Fratric http://ifsec.blogspot.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer 8. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application verifies arguments for a certain operation performed on an element. When parsing one of the operands of a method, the application will pass the argument straight to a method that will use the variant as an index. Due to bypassing the argument check, an aggressor can set the index to point to data outside the bounds of the array. This can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms11-081

## Disclosure Timeline

- 2011-06-29 - Vulnerability reported to vendor
- 2011-10-15 - Coordinated public release of advisory
