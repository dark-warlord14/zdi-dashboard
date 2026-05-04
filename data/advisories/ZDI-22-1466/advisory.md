# ZDI-22-1466: TP-Link TL-WR841N ated_tp Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1466
- **ZDI-CAN:** ZDI-CAN-17356
- **Date:** 2022-10-25
- **CVE:** CVE-2022-42433
- **CVSS:** 6.4
- **CVSS Vector:** AV:A/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR841N
- **Credit:** Cyrille Chatras
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1466/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link TL-WR841N routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the ated_tp service. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in firmware 220914.

## Disclosure Timeline

- 2022-07-19 - Vulnerability reported to vendor
- 2022-10-25 - Coordinated public release of advisory
