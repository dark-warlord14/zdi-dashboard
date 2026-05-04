# ZDI-22-807: Microsoft Visual Studio VSIX Auto Update Deserialization of Untrusted Data Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-807
- **ZDI-CAN:** ZDI-CAN-15294
- **Date:** 2022-06-01
- **CVE:** CVE-2022-24513
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** Nils Ole Timm (@firzen14)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-807/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Visual Studio. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the VSIX Auto Update task. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24513

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2022-06-01 - Coordinated public release of advisory
