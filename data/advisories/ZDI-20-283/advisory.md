# ZDI-20-283: Microsoft Windows Printer Device Context Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-283
- **ZDI-CAN:** ZDI-CAN-9875
- **Date:** 2020-03-12
- **CVE:** CVE-2020-0887
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** CodeUmbra
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-283/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of surface objects during print jobs. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0887

## Disclosure Timeline

- 2019-12-26 - Vulnerability reported to vendor
- 2020-03-12 - Coordinated public release of advisory
