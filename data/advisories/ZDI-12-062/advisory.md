# ZDI-12-062: Samba NDR PULL LSA TrustDomainInfoControllers Heap Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-062
- **ZDI-CAN:** ZDI-CAN-1538
- **Date:** 2012-04-18
- **CVE:** CVE-2012-1182
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Samba
- **Affected Products:** 3.6.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-062/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samba. Authentication is not required to exploit this vulnerability. The specific flaw exists within Samba's handling of a NDR PULL LSA TrustDomainInfoControllers request. By sending a specially crafted packet, it is possible to cause Samba to use a different size for memory allocation than it uses for a memory copy loop. This can result in memory corruption, and may be exploited by an attacker to gain remote code execution.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: http://www.samba.org/samba/security/CVE-2012-1182

## Disclosure Timeline

- 2011-10-20 - Vulnerability reported to vendor
- 2012-04-18 - Coordinated public release of advisory
