# ZDI-23-490: KeySight N8844A Data Analytics Web Service Unmarshal Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-490
- **ZDI-CAN:** ZDI-CAN-19603
- **Date:** 2023-05-01
- **CVE:** CVE-2023-1967
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** KeySight
- **Affected Products:** N8844A Data Analytics Web Service
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-490/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of KeySight N8844A Data Analytics Web Service. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Unmarshal function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

KeySight has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-115-01

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
