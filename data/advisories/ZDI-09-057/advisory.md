# ZDI-09-057: Microsoft Remote Desktop Client Arbitrary Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-057
- **ZDI-CAN:** ZDI-CAN-301
- **Date:** 2009-08-11
- **CVE:** CVE-2009-1133
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Remote Desktop
- **Credit:** wushi of team509 and the SureRun Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-057/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft's Remote Desktop Client. Authentication is not required to exploit this vulnerability. The specific flaw exists within mstscax.dll when parsing packets from an RDP server. A design flaw in the client allows a malicious RDP server to write to arbitrary memory inside the connecting processes memory space. By hosting a malicious RDP server, an attacker can execute arbitrary code on any client that attempts to connect to it. Privileges gained depend on which user is running the client.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-044.mspx

## Disclosure Timeline

- 2008-04-07 - Vulnerability reported to vendor
- 2009-08-11 - Coordinated public release of advisory
