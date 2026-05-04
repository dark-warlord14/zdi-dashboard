# ZDI-23-1033: Triangle MicroWorks SCADA Data Gateway Use of Hard-coded Cryptograhic Key Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1033
- **ZDI-CAN:** ZDI-CAN-20615
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39465
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Uri Katz of Claroty Team82
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1033/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Triangle MicroWorks SCADA Data Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TmwCrypto class. The issue results from the usage of a hard-coded cryptograhic key and the usage of a hard-coded certificate. An attacker can leverage this vulnerability to disclose sensitive information.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-04-06 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
