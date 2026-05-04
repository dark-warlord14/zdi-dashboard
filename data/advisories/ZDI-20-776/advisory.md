# ZDI-20-776: (Pwn2Own) ICONICS Genesis64 fwxserver Deserialization Denial-Of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-776
- **ZDI-CAN:** ZDI-CAN-10267
- **Date:** 2020-06-30
- **CVE:** CVE-2020-12007
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** ICONICS
- **Affected Products:** Genesis64
- **Credit:** Yehuda Anikster of Claroty Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-776/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of ICONICS Genesis64. Authentication is not required to exploit this vulnerability. The specific flaw exists with the handling of serialized objects. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-170-03

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-06-30 - Coordinated public release of advisory
