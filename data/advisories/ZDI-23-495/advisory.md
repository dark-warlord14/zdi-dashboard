# ZDI-23-495: NETGEAR RAX30 rex_cgi JSON Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-495
- **ZDI-CAN:** ZDI-CAN-19355
- **Date:** 2023-05-01
- **CVE:** CVE-2023-27361
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Rocco Calvi (@TecR0c) and Steven Seeley of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-495/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of JSON data. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065625/Security-Advisory-for-Post-Authentication-Buffer-Overflow-on-the-RAX30-PSV-2022-0302

## Disclosure Timeline

- 2022-11-23 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
