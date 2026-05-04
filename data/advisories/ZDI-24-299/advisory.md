# ZDI-24-299: Linux Kernel nft_exthdr_ipv6_eval Stack-based Buffer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-299
- **ZDI-CAN:** ZDI-CAN-21951
- **Date:** 2024-03-28
- **CVE:** CVE-2023-52628
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Alex Birnberg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-299/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the nft_exthdr_ipv6_eval function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?h=v6.1.67&id=d9ebfc0f21377690837ebbd119e679243e0099cc

## Disclosure Timeline

- 2023-09-05 - Vulnerability reported to vendor
- 2024-03-28 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
