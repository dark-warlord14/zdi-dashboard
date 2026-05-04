# ZDI-25-651: (Pwn2Own) Red Hat Enterprise Linux CBS Packet Scheduling Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-651
- **ZDI-CAN:** ZDI-CAN-27159
- **Date:** 2025-07-24
- **CVE:** CVE-2025-38350
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Red Hat
- **Affected Products:** Enterprise Linux
- **Credit:** Gerrard Tai of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-651/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Red Hat Enterprise Linux. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of hfsc_class objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Red Hat has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=103406b38c600fec1fe375a77b27d87e314aea09

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2025-07-24 - Coordinated public release of advisory
- 2025-07-24 - Advisory Updated
