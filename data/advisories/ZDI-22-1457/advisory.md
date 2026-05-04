# ZDI-22-1457: Linux Kernel nftables Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1457
- **ZDI-CAN:** ZDI-CAN-18540
- **Date:** 2022-10-21
- **CVE:** CVE-2022-42432
- **CVSS:** 5.1
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Gwangun Jung at THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1457/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the nft_osf_eval function. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://patchwork.ozlabs.org/project/netfilter-devel/patch/20220907082618.1193201-1-pablo@netfilter.org/

## Disclosure Timeline

- 2022-09-06 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
