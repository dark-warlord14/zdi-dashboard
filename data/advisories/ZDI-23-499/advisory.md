# ZDI-23-499: (Pwn2Own) NETGEAR RAX30 soap_serverd Stack-based Buffer Overflow Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-499
- **ZDI-CAN:** ZDI-CAN-19839
- **Date:** 2023-05-01
- **CVE:** CVE-2023-27368
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-499/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the soap_serverd binary. When parsing SOAP message headers, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065619/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2022-0348

## Disclosure Timeline

- 2023-01-26 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
