# ZDI-24-440: Delta Electronics InfraSuite Device Master ActiveMQ Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-440
- **ZDI-CAN:** ZDI-CAN-22502
- **Date:** 2024-05-13
- **CVE:** CVE-2023-46604
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-440/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Apache ActiveMQ broker, which listens on TCP port 61616 by default. The issue results from the use of a vulnerable version of Apache ActiveMQ. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-130-03

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-05-13 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
