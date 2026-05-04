# ZDI-10-174: Hewlett-Packard Data Protector DtbClsLogin Utf8cpy Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-174
- **ZDI-CAN:** ZDI-CAN-581
- **Date:** 2010-09-13
- **CVE:** CVE-2010-3007
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Data Protector
- **Credit:** AbdulAziz Hariri of Insight Technologies
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-174/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Data Protector. Authentication is not required to exploit this vulnerability. The specific flaw exists within the function DtbClsLogin defined in the module dpwindtb.dll on Windows and libdplindtb.so on Linux. This function takes user supplied input and copies it directly to a stack buffer. By providing a large enough string this buffer can be overrun and may result in arbitrary code execution dependent on the underlying operating system.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02498535

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-09-13 - Coordinated public release of advisory
