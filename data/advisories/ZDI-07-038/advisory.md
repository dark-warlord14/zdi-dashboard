# ZDI-07-038: Microsoft Internet Explorer Prototype Dereference Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-038
- **ZDI-CAN:** ZDI-CAN-168
- **Date:** 2007-06-12
- **CVE:** CVE-2007-1751
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sam Thomas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-038/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The flaw is specifically exposed when a prototype variable points to a table cell and then that table cell is removed. This results in an invalid pointer dereference which can be leveraged to result in arbitrary code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-033.mspx

## Disclosure Timeline

- 2007-02-15 - Vulnerability reported to vendor
- 2007-06-12 - Coordinated public release of advisory
