# ZDI-20-265: D-Link DAP-1330 HNAP Incorrect Implementation of Authentication Algorithm Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-265
- **ZDI-CAN:** ZDI-CAN-9554
- **Date:** 2020-02-21
- **CVE:** CVE-2020-8861
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1330
- **Credit:** chung96vn - Security Researcher of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-265/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DAP-1330 Wi-Fi range extenders. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HNAP login requests. The issue results from the lack of proper handling of cookies. An attacker can leverage this vulnerability to execute arbitrary code on the router.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10155

## Disclosure Timeline

- 2020-01-03 - Vulnerability reported to vendor
- 2020-02-21 - Coordinated public release of advisory
