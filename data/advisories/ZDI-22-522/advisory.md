# ZDI-22-522: (Pwn2Own) NETGEAR R6700v3 readycloud_control.cgi Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-522
- **ZDI-CAN:** ZDI-CAN-15762
- **Date:** 2022-03-23
- **CVE:** CVE-2022-27645
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700v3
- **Credit:** Xin'an Zhou, Xiaochen Zou, Zhiyun Qian (from the team NullRiver)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-522/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR R6700v3 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within readycloud_control.cgi. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064722/Security-Advisory-for-Sensitive-Information-Disclosure-on-Some-Routers-and-Fixed-Wireless-Products-PSV-2021-0325

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
