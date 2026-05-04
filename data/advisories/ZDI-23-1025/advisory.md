# ZDI-23-1025: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway Missing Authentication Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1025
- **ZDI-CAN:** ZDI-CAN-20501
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39457
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1025/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Triangle MicroWorks SCADA Data Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists due to the lack of user authentication. The issue results from missing authentication in the default system configuration. An attacker can leverage this vulnerability to execute arbitrary code in the context of root.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
