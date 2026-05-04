# ZDI-23-894: NETGEAR RAX30 UPnP Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-894
- **ZDI-CAN:** ZDI-CAN-20429
- **Date:** 2023-06-30
- **CVE:** CVE-2023-35722
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-894/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of UPnP port mapping requests. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065699/Security-Advisory-for-Pre-Authentication-Command-Injection-on-the-RAX30-PSV-2023-0046

## Disclosure Timeline

- 2023-03-08 - Vulnerability reported to vendor
- 2023-06-30 - Coordinated public release of advisory
