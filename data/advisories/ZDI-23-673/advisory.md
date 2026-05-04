# ZDI-23-673: Delta Electronics InfraSuite Device Master Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-673
- **ZDI-CAN:** ZDI-CAN-19054
- **Date:** 2023-05-17
- **CVE:** CVE-2023-1138
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-673/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Delta Electronics InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Device-Gateway service, which listens on TCP port 80 by default. The issue results from improper access control. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-02

## Disclosure Timeline

- 2022-11-01 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
