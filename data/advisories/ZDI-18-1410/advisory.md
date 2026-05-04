# ZDI-18-1410: Schneider Electric GUIcon GD1 File Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1410
- **ZDI-CAN:** ZDI-CAN-6965
- **Date:** 2018-12-14
- **CVE:** CVE-2018-7815
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** GUIcon
- **Credit:** rgod and mdm of 9SG Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1410/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric GUIcon. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of a GD1 file. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-347-01

## Disclosure Timeline

- 2018-07-27 - Vulnerability reported to vendor
- 2018-12-14 - Coordinated public release of advisory
