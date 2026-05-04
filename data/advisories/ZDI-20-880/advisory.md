# ZDI-20-880: D-Link DIR-842 HNAP GetCAPTCHAsetting Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-880
- **ZDI-CAN:** ZDI-CAN-10083
- **Date:** 2020-07-20
- **CVE:** CVE-2020-15632
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-842
- **Credit:** chung96vn - Security Researcher of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-880/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DIR-842 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of HNAP GetCAPTCHAsetting requests. The issue results from the lack of proper handling of sessions. An attacker can leverage this vulnerability to execute arbitrary code in the context of the device.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10184

## Disclosure Timeline

- 2020-03-15 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
