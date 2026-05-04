# ZDI-21-1242: NETGEAR R6260 setupwizard.cgi Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1242
- **ZDI-CAN:** ZDI-CAN-14107
- **Date:** 2021-10-28
- **CVE:** CVE-2021-34980
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6260
- **Credit:** STARLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1242/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6260 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the setupwizard.cgi page. When parsing the SOAP_LOGIN_TOKEN environment variable, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064262/Security-Advisory-for-Vertical-Privilege-Escalation-on-Some-Routers-PSV-2021-0150?article=000064262

## Disclosure Timeline

- 2021-06-16 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory
- 2021-10-28 - Advisory Updated
