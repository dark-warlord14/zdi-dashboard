# ZDI-23-839: NETGEAR RAX30 cmsCli_authenticate Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-839
- **ZDI-CAN:** ZDI-CAN-19918
- **Date:** 2023-06-08
- **CVE:** CVE-2023-34285
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Stefan Schiller (Sonar)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-839/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within a shared library used by the telnetd service, which listens on TCP port 23 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065696/RAX30-Firmware-Version-1-0-11-96-Hot-Fix

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
