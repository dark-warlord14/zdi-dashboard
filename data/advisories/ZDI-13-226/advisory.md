# ZDI-13-226: HP PCM+ SNAC Registration Server UpdateDomainControllerServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-226
- **ZDI-CAN:** ZDI-CAN-1743
- **Date:** 2013-09-11
- **CVE:** CVE-2013-4811
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** PCM Plus
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-226/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP PCM Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UpdateDomainControllerServlet. This servlet improperly sanitizes the 'adCert' argument allowing the remote attacker could upload a .jsp file. This can result in remote code execution under the context of the SYSTEM user.

## Disclosure Timeline

- 2013-02-15 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
