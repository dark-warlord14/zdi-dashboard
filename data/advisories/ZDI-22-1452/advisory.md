# ZDI-22-1452: Linux Kernel Net Scheduler Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1452
- **ZDI-CAN:** ZDI-CAN-18231
- **Date:** 2022-10-21
- **CVE:** CVE-2022-3586
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Gwnaun Jung at THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1452/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of CAKE queueing disciplines. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilties to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/linux-fs.git/commit/?h=rxrpc-ringless-2&id=9efd23297cca530bb35e1848665805d3fcdd7889

## Disclosure Timeline

- 2022-08-23 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
