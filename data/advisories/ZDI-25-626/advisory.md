# ZDI-25-626: (Pwn2Own) NVIDIA Container Toolkit Environment Variable Handling Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-626
- **ZDI-CAN:** ZDI-CAN-27193
- **Date:** 2025-07-21
- **CVE:** CVE-2025-23266
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** NVIDIA
- **Affected Products:** Container Toolkit
- **Credit:** Nir Ohfeld (@nirohfeld), Shir Tamari (@shirtamari)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-626/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of NVIDIA Container Toolkit. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of hooks. The issue results from the lack of restrictions on environment variables prior to spawning a hook process. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the host system.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5659

## Disclosure Timeline

- 2025-06-05 - Vulnerability reported to vendor
- 2025-07-21 - Coordinated public release of advisory
- 2025-07-21 - Advisory Updated
