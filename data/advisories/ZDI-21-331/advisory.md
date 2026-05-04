# ZDI-21-331: Microsoft Windows CInteractionTrackerMarshaler Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-331
- **ZDI-CAN:** ZDI-CAN-12484
- **Date:** 2021-03-17
- **CVE:** CVE-2021-26900
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea (@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-331/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within DirectComposition. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-26900

## Disclosure Timeline

- 2020-12-04 - Vulnerability reported to vendor
- 2021-03-17 - Coordinated public release of advisory
- 2021-03-17 - Advisory Updated
