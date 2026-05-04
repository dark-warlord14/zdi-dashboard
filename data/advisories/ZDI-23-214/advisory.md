# ZDI-23-214: NETGEAR CAX30S SSO Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-214
- **ZDI-CAN:** ZDI-CAN-18227
- **Date:** 2023-03-07
- **CVE:** CVE-2022-43654
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** CAX30S
- **Credit:** Fiseha and Robera
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-214/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR CAX30S routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the token parameter provided to the sso.php endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065527/Security-Advisory-for-Pre-Authentication-Command-Injection-on-Some-Cable-Modem-Routers-PSV-2022-0208

## Disclosure Timeline

- 2022-09-22 - Vulnerability reported to vendor
- 2023-03-07 - Coordinated public release of advisory
