# ZDI-23-1026: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway Use of Hard-coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1026
- **ZDI-CAN:** ZDI-CAN-20509
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39458
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Team ECQ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1026/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Triangle MicroWorks SCADA Data Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of certificates. The service uses a hard-coded default SSL certificate. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
