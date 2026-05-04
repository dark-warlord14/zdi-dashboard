# ZDI-20-1429: D-Link DAP-1860 uhttpd Authentication Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1429
- **ZDI-CAN:** ZDI-CAN-10894
- **Date:** 2020-12-15
- **CVE:** CVE-2020-27865
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1860
- **Credit:** chung96vn of Vietnam Cyber Security Center
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1429/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-1860 WiFi extenders. Authentication is not required to exploit this vulnerability. The specific flaw exists within the uhttpd service, which listens on TCP port 80 by default. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the device.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10197

## Disclosure Timeline

- 2020-07-01 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
