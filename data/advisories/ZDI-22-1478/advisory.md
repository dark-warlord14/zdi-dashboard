# ZDI-22-1478: Delta Industrial Automation InfraSuite Device Master Device-Gateway Service Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1478
- **ZDI-CAN:** ZDI-CAN-17439
- **Date:** 2022-10-27
- **CVE:** CVE-2022-41778
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1478/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists exists within the Device-Gateway service, which listens on TCP port 3100 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-298-07

## Disclosure Timeline

- 2022-06-06 - Vulnerability reported to vendor
- 2022-10-27 - Coordinated public release of advisory
