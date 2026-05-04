# ZDI-22-1488: Delta Industrial Automation InfraSuite Device Master APRunning Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1488
- **ZDI-CAN:** ZDI-CAN-17641
- **Date:** 2022-10-27
- **CVE:** CVE-2022-41629
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1488/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Delta Industrial Automation InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the gateway endpoint, which listens on TCP ports 80 and 443 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-298-07

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2022-10-27 - Coordinated public release of advisory
