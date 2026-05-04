# ZDI-13-225: HP PCM+ SNAC Registration Server UpdateCertificatesServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-225
- **ZDI-CAN:** ZDI-CAN-1742
- **Date:** 2013-09-11
- **CVE:** CVE-2013-4812
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** PCM Plus
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-225/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP PCM Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UpdateCertificatesServlet. This servlet improperly sanitizes the 'fileName' argument allowing the remote attacker could upload a .jsp file. This can result in remote code execution under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03897409

## Disclosure Timeline

- 2013-02-15 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
