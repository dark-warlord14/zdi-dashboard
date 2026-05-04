# ZDI-21-129: Siemens Comfort Panel Telnet Service Missing Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-129
- **ZDI-CAN:** ZDI-CAN-12046
- **Date:** 2021-02-04
- **CVE:** CVE-2020-15798
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Comfort Panel
- **Credit:** Ta-Lun Yen of TXOne IoT/ICS Security Research Labs (Trend Micro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-129/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Comfort Panel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the telnet service, which listens on TCP port 22 by default. The issue results from the lack of authentication prior to allowing remote connections. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-033-02

## Disclosure Timeline

- 2020-09-30 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
