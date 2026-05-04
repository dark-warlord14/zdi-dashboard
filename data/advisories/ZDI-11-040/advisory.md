# ZDI-11-040: (0Day) Microsoft Office Excel 2003 Invalid Object Type Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-040
- **ZDI-CAN:** ZDI-CAN-811
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0980
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw occurs when parsing a document with a malformed Excel document. When parsing an office art object, the application will add the malformed object to a linked list. After this addition, the application will process each element in the linked list. When handling the object in question, the application will explicitly trust a function pointer off of this object. If an attacker can substitute an object of their choosing in place of this function pointer, code execution under the context of the application can be achieved.

## Additional Details

Patched April 12, 2011 http://www.microsoft.com/technet/security/bulletin/ms11-021.mspx

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
