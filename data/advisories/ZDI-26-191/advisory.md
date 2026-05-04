# ZDI-26-191: (Pwn2Own) Linux Kernel nf_tables Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-191
- **ZDI-CAN:** ZDI-CAN-17443
- **Date:** 2026-03-16
- **CVE:** CVE-2022-32250
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Keith Yeo (@kyeojy)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-191/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of nft_objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://ubuntu.com/security/CVE-2022-32250#notes

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
