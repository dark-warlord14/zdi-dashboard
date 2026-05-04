# ZDI-19-960: Advantech WISE-PaaS/RMM NodeRed Server Missing Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-960
- **ZDI-CAN:** ZDI-CAN-8891
- **Date:** 2019-11-01
- **CVE:** CVE-2019-13547
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WISE-PaaS/RMM
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-960/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WISE-PaaS/RMM. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NodeRed Server, which listens on TCP port 1880 by default. The issue results from the lack of authentication prior to allowing alterations to the system configuration. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-304-01

## Disclosure Timeline

- 2019-07-11 - Vulnerability reported to vendor
- 2019-11-01 - Coordinated public release of advisory
