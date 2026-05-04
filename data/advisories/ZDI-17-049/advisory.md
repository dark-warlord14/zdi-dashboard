# ZDI-17-049: Brocade Network Advisor FileReceiveServlet Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-049
- **ZDI-CAN:** ZDI-CAN-4023
- **Date:** 2017-01-20
- **CVE:** CVE-2016-8204
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Brocade
- **Affected Products:** Network Advisor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Brocade Network Advisor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FileReceiveServlet servlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Brocade has issued an update to correct this vulnerability. More details can be found at: https://www.brocade.com/content/dam/common/documents/content-types/security-bulletin/brocade-security-advisory-2016-012.pdf

## Disclosure Timeline

- 2016-10-17 - Vulnerability reported to vendor
- 2017-01-20 - Coordinated public release of advisory
