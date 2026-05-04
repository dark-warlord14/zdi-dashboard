# ZDI-20-495: Intel Wi-Fi Link Driver Netwtw06 Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-495
- **ZDI-CAN:** ZDI-CAN-9376
- **Date:** 2020-04-15
- **CVE:** CVE-2020-0558
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Intel
- **Affected Products:** Wi-Fi Link Driver
- **Credit:** Haikuo Xie ,Ying Wang of Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-495/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Intel Wi-Fi Link Driver. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of 802.11 frames. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Intel has issued an update to correct this vulnerability. More details can be found at: https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00338.html

## Disclosure Timeline

- 2019-12-03 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
