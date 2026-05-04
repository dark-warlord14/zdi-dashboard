# ZDI-21-797: Microsoft Windows CLDFLT Integer Underflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-797
- **ZDI-CAN:** ZDI-CAN-13282
- **Date:** 2021-07-15
- **CVE:** CVE-2021-31969
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-797/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the cldflt.sys driver. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-31969

## Disclosure Timeline

- 2021-03-10 - Vulnerability reported to vendor
- 2021-07-15 - Coordinated public release of advisory
