# ZDI-23-498: (Pwn2Own) NETGEAR RAX30 libcms_cli Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-498
- **ZDI-CAN:** ZDI-CAN-19838
- **Date:** 2023-05-01
- **CVE:** CVE-2023-27367
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-498/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the libcms_cli module. The issue results from the lack of proper validation of a user-supplied command before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065619/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2022-0348

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
