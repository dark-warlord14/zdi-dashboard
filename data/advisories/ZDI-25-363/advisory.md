# ZDI-25-363: Trend Micro Apex One Virus Scan Engine Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-363
- **ZDI-CAN:** ZDI-CAN-24973
- **Date:** 2025-06-11
- **CVE:** CVE-2025-49156
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-363/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Furthermore, the product is vulnerable only if configured by an administrator to take a non-default malware remediation action. The specific flaw exists within the VsapiNT.sys kernel module. By creating a symbolic link, an attacker can abuse the driver to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019917

## Disclosure Timeline

- 2024-08-14 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
