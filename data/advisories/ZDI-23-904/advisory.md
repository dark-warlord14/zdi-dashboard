# ZDI-23-904: Delta Electronics InfraSuite Device Master APRunning Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-904
- **ZDI-CAN:** ZDI-CAN-20606
- **Date:** 2023-07-10
- **CVE:** CVE-2023-34316
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-904/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Delta Electronics InfraSuite Device Master. Authentication is required to exploit this vulnerability. The specific flaw exists within the gateway endpoint, which listens on TCP ports 80 and 443 by default. The issue results from improper access control. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-180-01

## Disclosure Timeline

- 2023-05-03 - Vulnerability reported to vendor
- 2023-07-10 - Coordinated public release of advisory
