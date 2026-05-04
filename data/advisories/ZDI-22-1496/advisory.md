# ZDI-22-1496: D-Link DIR-1935 SetStaticRouteIPv6Settings Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1496
- **ZDI-CAN:** ZDI-CAN-16145
- **Date:** 2022-11-03
- **CVE:** CVE-2022-43624
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-1935
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1496/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-1935 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of SetStaticRouteIPv6Settings requests to the web management portal. When parsing subelements within the StaticRouteIPv6List element, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10310

## Disclosure Timeline

- 2022-06-30 - Vulnerability reported to vendor
- 2022-11-03 - Coordinated public release of advisory
