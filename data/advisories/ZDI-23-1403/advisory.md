# ZDI-23-1403: Microsoft Azure DevOps Server MachinePropertyBag Deserialization of Untrusted Data Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1403
- **ZDI-CAN:** ZDI-CAN-20695
- **Date:** 2023-09-12
- **CVE:** CVE-2023-38155
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure DevOps Server
- **Credit:** Mikhail Shcherbakov (@yu5k3)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1403/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Azure DevOps Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the MachinePropertyBag class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-38155

## Disclosure Timeline

- 2023-05-05 - Vulnerability reported to vendor
- 2023-09-12 - Coordinated public release of advisory
