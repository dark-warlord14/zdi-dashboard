# ZDI-23-1283: NETGEAR Orbi 760 SOAP API Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1283
- **ZDI-CAN:** ZDI-CAN-20524
- **Date:** 2023-08-30
- **CVE:** CVE-2023-41183
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** Orbi 760
- **Credit:** Xin'an Zhou and Zhiyun Qian
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1283/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR Orbi 760 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the SOAP API. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065734/Security-Advisory-for-Authentication-Bypass-on-the-RBR760-PSV-2023-0052

## Disclosure Timeline

- 2023-03-22 - Vulnerability reported to vendor
- 2023-08-30 - Coordinated public release of advisory
