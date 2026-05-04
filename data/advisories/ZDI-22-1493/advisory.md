# ZDI-22-1493: D-Link DIR-1935 ConfigFileUpload Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1493
- **ZDI-CAN:** ZDI-CAN-16141
- **Date:** 2022-11-03
- **CVE:** CVE-2022-43619
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-1935
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1493/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-1935 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of ConfigFileUpload requests to the web management portal. The issue results from the lack of proper validation of a user-supplied string before using it as a format specifier. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10310

## Disclosure Timeline

- 2022-06-14 - Vulnerability reported to vendor
- 2022-11-03 - Coordinated public release of advisory
