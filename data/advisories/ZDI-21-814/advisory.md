# ZDI-21-814: Schneider Electric C-Bus Toolkit Missing Authentication Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-814
- **ZDI-CAN:** ZDI-CAN-12592
- **Date:** 2021-07-19
- **CVE:** CVE-2021-22784
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** C-Bus Toolkit
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-814/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Schneider Electric C-Bus Toolkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the C-Gate 2 Service, which listens on TCP port 20023. A crafted webpage can be used to enable remote access. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-194-01

## Disclosure Timeline

- 2021-03-18 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
