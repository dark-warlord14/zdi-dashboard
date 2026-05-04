# ZDI-20-257: Microsoft Windows Service Tracing Arbitrary File Move Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-257
- **ZDI-CAN:** ZDI-CAN-9538
- **Date:** 2020-02-20
- **CVE:** CVE-2020-0668
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Clment Labro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-257/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Tracing functionality used by the Routing and Remote Access service. The issue results from the lack of proper permissions on registry keys that control this functionality. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0668

## Disclosure Timeline

- 2019-11-28 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
- 2020-03-09 - Advisory Updated
