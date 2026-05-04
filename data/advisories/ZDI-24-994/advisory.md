# ZDI-24-994: Linux Kernel QXL VGA Driver Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-994
- **ZDI-CAN:** ZDI-CAN-20940
- **Date:** 2024-07-29
- **CVE:** CVE-2023-39198
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-994/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the QXL VGA driver. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.redhat.com/show_bug.cgi?id=2218332

## Disclosure Timeline

- 2023-05-19 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
