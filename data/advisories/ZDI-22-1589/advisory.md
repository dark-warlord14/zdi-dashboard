# ZDI-22-1589: Microsoft Windows Output Protection Manager Integer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1589
- **ZDI-CAN:** ZDI-CAN-17568
- **Date:** 2022-11-15
- **CVE:** CVE-2022-41092
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** namnp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1589/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Output Protection Manager. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41092

## Disclosure Timeline

- 2022-07-11 - Vulnerability reported to vendor
- 2022-11-15 - Coordinated public release of advisory
- 2022-11-24 - Advisory Updated
