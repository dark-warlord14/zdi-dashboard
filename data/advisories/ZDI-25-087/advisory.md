# ZDI-25-087: NVIDIA Container Toolkit mount_files Time-Of-Check Time-Of-Use Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-087
- **ZDI-CAN:** ZDI-CAN-26525
- **Date:** 2025-02-19
- **CVE:** CVE-2025-23359
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** NVIDIA
- **Affected Products:** Container Toolkit
- **Credit:** Dre Cura of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-087/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of NVIDIA Container Toolkit. An attacker must first obtain the ability to execute code within a container in order to exploit this vulnerability. The specific flaw exists within the mount_files function. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the host.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5616

## Disclosure Timeline

- 2025-02-11 - Vulnerability reported to vendor
- 2025-02-19 - Coordinated public release of advisory
- 2025-02-19 - Advisory Updated
