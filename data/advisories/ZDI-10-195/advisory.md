# ZDI-10-195: SAP BusinessObjects Crystal Reports Server CMS.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-195
- **ZDI-CAN:** ZDI-CAN-787
- **Date:** 2010-10-12
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SAP
- **Affected Products:** Crystal Reports
- **Credit:** AbdulAziz Hariri Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-195/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP Crystal Reports. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CMS.exe process which listens by default on several TCP ports above 1024. When parsing a GIOP request, the process trusts a user-supplied 32-bit value and allocates a buffer on the heap. The process then proceeds to copy the string following this value from the packet until it finds a NULL byte. By crafting a specifically sized packet a remote attacker can overflow the buffer and gain code execution under the context of the SYSTEM user.

## Additional Details

A solution was provided via SAP note 1509604 https://service.sap.com/sap/support/notes/1509604

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
