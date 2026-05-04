# ZDI-23-1163: NETGEAR RAX30 Telnet CLI passwd Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1163
- **ZDI-CAN:** ZDI-CAN-20009
- **Date:** 2023-08-22
- **CVE:** CVE-2023-40478
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1163/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the telnet CLI service, which listens on TCP port 23. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065649/Security-Advisory-for-Post-authentication-Buffer-Overflow-on-the-RAX30-PSV-2023-0002

## Disclosure Timeline

- 2023-01-04 - Vulnerability reported to vendor
- 2023-08-22 - Coordinated public release of advisory
