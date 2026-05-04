# ZDI-20-267: D-Link Multiple Routers HNAP PrivateLogin Incorrect Implementation of Authentication Algorithm Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-267
- **ZDI-CAN:** ZDI-CAN-9470
- **Date:** 2020-02-24
- **CVE:** CVE-2020-8863
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** Multiple Routers
- **Credit:** chung96vn - Security Researcher of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-267/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DIR-867, DIR-878, and DIR-882 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HNAP login requests. The issue results from the lack of proper implementation of the authentication algorithm. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the router.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10157

## Disclosure Timeline

- 2019-12-23 - Vulnerability reported to vendor
- 2020-02-24 - Coordinated public release of advisory
