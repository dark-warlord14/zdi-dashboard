# ZDI-24-821: Linux Kernel TIPC Message Reassembly Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-821
- **ZDI-CAN:** ZDI-CAN-23852
- **Date:** 2024-06-20
- **CVE:** CVE-2024-36886
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Sam Page (sam4k)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-821/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with TIPC bearer enabled are vulnerable. The specific flaw exists within the processing of fragmented TIPC messages. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/080cbb890286cd794f1ee788bbc5463e2deb7c2b

## Disclosure Timeline

- 2024-04-25 - Vulnerability reported to vendor
- 2024-06-20 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
