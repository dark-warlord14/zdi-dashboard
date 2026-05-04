# ZDI-23-1034: Triangle MicroWorks SCADA Data Gateway get_config Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1034
- **ZDI-CAN:** ZDI-CAN-20797
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39466
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Uri Katz of Claroty Team82
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1034/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Triangle MicroWorks SCADA Data Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists within the get_config endpoint. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose sensitive information.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-04-06 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
