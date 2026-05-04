# ZDI-11-041: (0Day) Microsoft Office Excel Office Art Object Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-041
- **ZDI-CAN:** ZDI-CAN-829
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0979
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-041/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way the application parses an Office Art record within a Microsoft Excel Document. Specifically, when parsing an office art object record, if an error occurs, the application will add a stray reference to an element which is part of a linked list. When receiving a window message, the application will proceed to navigate this linked list. This will access a method from the malformed object which can lead to code execution under the context of the application.

## Additional Details

Patched April 12, 2011 http://www.microsoft.com/technet/security/bulletin/ms11-021.mspx

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
