# ZDI-23-1754: Delta Electronics InfraSuite Device Master Device-DataCollect Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1754
- **ZDI-CAN:** ZDI-CAN-21771
- **Date:** 2023-11-30
- **CVE:** CVE-2023-47207
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1754/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Device-DataCollect service, which listens on TCP port 3000 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-331-01

## Disclosure Timeline

- 2023-07-18 - Vulnerability reported to vendor
- 2023-11-30 - Coordinated public release of advisory
