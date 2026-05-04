# ZDI-23-1518: (0Day) D-Link DIR-X3260 prog.cgi Incorrect Implementation of Authentication Algorithm Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1518
- **ZDI-CAN:** ZDI-CAN-21100
- **Date:** 2023-10-04
- **CVE:** CVE-2023-44420
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-X3260
- **Credit:** Nicholas Zubrisky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1518/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DIR-X3260 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the prog.cgi executable. The issue results from an incorrect implementation of the authentication algorithm. An attacker can leverage this vulnerability to bypass authentication on the device.

## Additional Details

05/17/23 – ZDI reported the vulnerability to the vendor. 08/25/23 – ZDI asked for an update. 08/30/23 – The vendor states the fix is still under development. 09/29/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 10/04/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-05-17 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
