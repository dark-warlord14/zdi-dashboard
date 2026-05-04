# ZDI-23-1010: Adtran SR400ac ping Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1010
- **ZDI-CAN:** ZDI-CAN-20525
- **Date:** 2023-07-28
- **CVE:** CVE-2023-38120
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adtran
- **Affected Products:** SR400ac
- **Credit:** ther3d0ne - https://thered0ne.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1010/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adtran SR400ac routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the ping command, which is available over JSON-RPC. A crafted host parameter can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed at SmartOS 12.1.3.1 https://supportcommunity.adtran.com/t5/Security-Advisories/ADTSA-2023001-Residential-Gateway-amp-Service-Delivery-Gateway/ta-p/38495

## Disclosure Timeline

- 2023-05-05 - Vulnerability reported to vendor
- 2023-07-28 - Coordinated public release of advisory
