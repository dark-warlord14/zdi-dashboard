# ZDI-08-002: Citrix Metaframe Presentation Server IMA Service Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-002
- **ZDI-CAN:** ZDI-CAN-212
- **Date:** 2008-01-17
- **CVE:** CVE-2008-0356
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Citrix
- **Affected Products:** Metaframe Server
- **Credit:** Eric DETOISIEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-002/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Citrix Presentation Server. Authentication is not required to exploit this vulnerability. The specific flaw resides in the Independent Management Architecture service, ImaSrv.exe, which listens by default on TCP port 2512 or 2513. The process trusts a user-suppled value as a parameter to a memory allocation. By supplying a specific value, an undersized heap buffer may be allocated. Subsequently, an attacker can then overflow that heap buffer by sending an overly large packet leading to arbitrary code execution in the context of the SYSTEM user.

## Additional Details

Citrix has issued an update to correct this vulnerability. More details can be found at: http://support.citrix.com/article/CTX114487

## Disclosure Timeline

- 2007-07-20 - Vulnerability reported to vendor
- 2008-01-17 - Coordinated public release of advisory
