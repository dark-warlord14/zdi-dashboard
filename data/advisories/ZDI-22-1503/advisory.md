# ZDI-22-1503: D-Link DIR-1935 HNAP Incorrect Comparison Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1503
- **ZDI-CAN:** ZDI-CAN-16152
- **Date:** 2022-11-03
- **CVE:** CVE-2022-43621
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-1935
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1503/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DIR-1935 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HNAP login requests. The issue results from an incorrectly implemented comparison. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10310

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2022-11-03 - Coordinated public release of advisory
